"""
This script is used to get the pose of the crazyflie 
in the optitrack mocap system through VRPN. Then 
forward the pose information to the crazyflie.
"""
import math
import time
import logging
from datetime import datetime

import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.positioning.position_hl_commander import PositionHlCommander

import numpy as np
import rospy
from geometry_msgs.msg import PoseStamped

from threading import Thread

from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.mem import MemoryElement
from cflib.crazyflie.mem import Poly4D
from cflib.crazyflie.syncLogger import SyncLogger
from cflib.utils import uri_helper
import os
import csv

filename = None
# URI to the Crazyflie to connect to
uri = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

URI = 'radio://0/80/2M/E7E7E7E7E7'

# True: send position and orientation; False: send position only
send_full_pose = True

# When using full pose, the estimator can be sensitive to noise in the orientation data when yaw is close to +/- 90
# degrees. If this is a problem, increase orientation_std_dev a bit. The default value in the firmware is 4.5e-3.
orientation_std_dev = 4.5e-3

# Duration,x^0,x^1,x^2,x^3,x^4,x^5,x^6,x^7,y^0,y^1,y^2,y^3,y^4,y^5,y^6,y^7,z^0,z^1,z^2,z^3,z^4,z^5,z^6,z^7,yaw^0,yaw^1,yaw^2,yaw^3,yaw^4,yaw^5,yaw^6,yaw^7
straight_line = [
    [1.60383,0,0,0,0,0.562414,-0.590316,0.230998,-0.0325465,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1.62329,0.5,0.581999,-7.80968e-16,-0.0539809,-0.0678949,-0.0773259,0.104529,-0.0263757,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

def wait_for_position_estimator(scf):
    print('Waiting for estimator to find position...')

    log_config = LogConfig(name='Kalman Variance', period_in_ms=500)
    log_config.add_variable('kalman.varPX', 'float')
    log_config.add_variable('kalman.varPY', 'float')
    log_config.add_variable('kalman.varPZ', 'float')

    var_y_history = [1000] * 10
    var_x_history = [1000] * 10
    var_z_history = [1000] * 10

    threshold = 0.001

    with SyncLogger(scf, log_config) as logger:
        for log_entry in logger:
            data = log_entry[1]

            var_x_history.append(data['kalman.varPX'])
            var_x_history.pop(0)
            var_y_history.append(data['kalman.varPY'])
            var_y_history.pop(0)
            var_z_history.append(data['kalman.varPZ'])
            var_z_history.pop(0)

            min_x = min(var_x_history)
            max_x = max(var_x_history)
            min_y = min(var_y_history)
            max_y = max(var_y_history)
            min_z = min(var_z_history)
            max_z = max(var_z_history)

            # print("{} {} {}".
            #       format(max_x - min_x, max_y - min_y, max_z - min_z))

            if (max_x - min_x) < threshold and (
                    max_y - min_y) < threshold and (
                    max_z - min_z) < threshold:
                break


def send_extpose_quat(cf, x, y, z, quat):
    """
    Send the current Crazyflie X, Y, Z position and attitude as a quaternion.
    This is going to be forwarded to the Crazyflie's position estimator.
    """
    if send_full_pose:
        cf.extpos.send_extpose(x, y, z, quat.x, quat.y, quat.z, quat.w)
    else:
        cf.extpos.send_extpos(x, y, z)


def reset_estimator(cf):
    cf.param.set_value('kalman.resetEstimation', '1')
    time.sleep(0.1)
    cf.param.set_value('kalman.resetEstimation', '0')

    # time.sleep(1)
    wait_for_position_estimator(cf)


def adjust_orientation_sensitivity(cf):
    cf.param.set_value('locSrv.extQuatStdDev', orientation_std_dev)


def activate_kalman_estimator(cf):
    cf.param.set_value('stabilizer.estimator', '2')

    # Set the std deviation for the quaternion data pushed into the
    # kalman filter. The default value seems to be a bit too low.
    cf.param.set_value('locSrv.extQuatStdDev', 0.06)


def activate_mellinger_controller(cf):
    cf.param.set_value('stabilizer.controller', '2')


def upload_trajectory(cf, trajectory_id, trajectory):
    trajectory_mem = cf.mem.get_mems(MemoryElement.TYPE_TRAJ)[0]
    trajectory_mem.trajectory = []

    total_duration = 0
    for row in trajectory:
        duration = row[0]
        x = Poly4D.Poly(row[1:9])
        y = Poly4D.Poly(row[9:17])
        z = Poly4D.Poly(row[17:25])
        yaw = Poly4D.Poly(row[25:33])
        trajectory_mem.trajectory.append(Poly4D(duration, x, y, z, yaw))
        total_duration += duration

    trajectory_mem.write_data_sync()
    cf.high_level_commander.define_trajectory(trajectory_id, 0, len(trajectory_mem.trajectory))
    return total_duration


def run_sequence(cf, trajectory_id, duration):
    commander = cf.high_level_commander

    commander.takeoff(0.15, 2.0)
    time.sleep(3.0)
    relative = True
    commander.start_trajectory(trajectory_id, 1.0, relative)
    time.sleep(duration)
    commander.land(0.0, 2.0)
    time.sleep(2)
    commander.stop()


def figure_eight_flight(commander, radius, steps, velocity, default_height = 0.5):
    """
    Perform a horizontal figure-eight flight.

    :param commander: The commander object that has the go_to method.
    :param radius: The radius of the figure-eight loops.
    :param steps: The number of steps to divide each loop into.
    :param velocity: The velocity of the movement.
    """
    for i in range(steps):
        angle = 2 * math.pi * (i / steps)
        x = radius * math.sin(angle)
        y = radius * math.sin(2 * angle)
        commander.go_to(x, y, default_height, velocity)
        time.sleep(0.1)  # Adjust sleep time as needed


def spiral_ascent(commander: PositionHlCommander, 
                  radius, height, turns, steps, velocity, initial_height = 0.5) -> None:
    """
    Perform a spiral ascent.

    :param commander: The commander object that has the go_to method.
    :param radius: The radius of the spiral.
    :param height: The total height to ascend.
    :param turns: The number of turns in the spiral.
    :param steps: The number of steps to divide the spiral into.
    :param velocity: The velocity of the movement.
    """
    for i in range(steps):
        angle = 2 * math.pi * turns * (i / steps)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        z = (height / steps) * i + initial_height
        commander.go_to(x, y, z, velocity)
        time.sleep(0.1)  # Adjust sleep time as needed

def move_straight(pc: PositionHlCommander, x, y, z, velocity):
    """
    Moves the object in a straight line to the specified coordinates.

    :param pc: The object that has the go_to method.
    :param x: The target x-coordinate.
    :param y: The target y-coordinate.
    :param z: The target z-coordinate.
    :param velocity: the velocity of the movement.
    """
    print(f"{time.time():.4f} : before moving to ({x}, {y}, {z})")
    pc.go_to(x, y, z, velocity)
    print(f"{time.time():.4f} : after moving to ({x}, {y}, {z})")


def pose_callback(data):
    '''
    callback function for the crazyflie pose subscriber
    '''
    t = time.time()
    global filename  # Declare filename as global to modify the global variable
    pose = [data.pose.position.x, data.pose.position.y, data.pose.position.z, data.pose.orientation]
    send_extpose_quat(cf, pose[0], pose[1], pose[2], pose[3]) # x, y, z, quat
    with open(filename, 'a', newline='', encoding='utf-8') as cb_file:
        pose_writer = csv.writer(cb_file)
        pose_writer.writerow([t, pose[0], pose[1], pose[2], pose[3].x, pose[3].y, pose[3].z, pose[3].w])

def land_on_elevated_surface():
    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        with PositionHlCommander(scf,
                                 default_height=0.5,
                                 default_velocity=0.2,
                                 default_landing_height=0.35,
                                 controller=PositionHlCommander.CONTROLLER_PID) as pc:
            # fly onto a landing platform at non-zero height (ex: from floor to desk, etc)
            pc.forward(1.0)
            pc.left(1.0)
            # land() will be called on context exit, gradually lowering to default_landing_height, then stopping motors


if __name__ == '__main__':
    print(f"{time.time():.4f} : Start the program")
    cflib.crtp.init_drivers()

    filename = os.path.join('mocap_data', datetime.now().strftime('%Y%m%d_%H_%M_%S') + '.csv')
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['t', 'x', 'y', 'z', 'qx', 'qy', 'qz', 'qw'])

    filename_collection = 'mocap_data_description.md'
    with open(filename_collection, 'a', encoding='utf-8') as file:
        file.write(f'`{filename}`\n')

    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        cf = scf.cf
        trajectory_id = 1

        rospy.init_node('cf_lxl_node', anonymous=True)
        rospy.Subscriber("/vrpn_client_node/cf_lxl_sm/pose", PoseStamped, pose_callback)

        adjust_orientation_sensitivity(cf)
        activate_kalman_estimator(cf)
        reset_estimator(cf)

        # print(f"{time.time():.4f} : start MotionCommander")
        # I have add a parameter 'velocity' to the original initialization function.
        # with MotionCommander(scf,0.5,0.1) as mc:
        #     print(f"{time.time():.4f} : taking off")
        #     # mc.forward(1.0,0.5) # This command can be used to execute a uniform speed trajectory.
        #     time.sleep(1)
        #     print(f"{time.time():.4f} : after sleeping 1 seconds")
        #     mc.move_distance(1.0, 0.0, 0.0, 0.5)
        #     print(f"{time.time():.4f} : after moving 1.0m")
        #     time.sleep(1)
        #     print(f"{time.time():.4f} : landing")

        X_INIT = 0.001
        Y_INIT = 0.001
        Z_INIT = 0.791
        TAKEOFF_HEIGHT = 0.01 # Height to take off from table plane
        OFFSET_HEIGHT = 0.01 # Height offset to table plane
        STABLE_DELAY = 15 # Time delay to stabilize after height change
        GARAGE_CENTER = (1, 0.0, Z_INIT) # Center of garage
        PARK_VEL = 1
        print(f"{time.time():.4f} : start PositionHlCommander")
        with PositionHlCommander(scf, X_INIT, Y_INIT, Z_INIT,
                                 default_velocity = 0.5,
                                 default_height = Z_INIT + TAKEOFF_HEIGHT,
                                 default_landing_height = Z_INIT) as pc:
            
            print(f"{time.time():.4f} : taking off")
            time.sleep(STABLE_DELAY)
            print(f"{time.time():.4f} : after sleeping {STABLE_DELAY} seconds")

            # pc.down(TAKEOFF_HEIGHT - OFFSET_HEIGHT,0.2)
            # time.sleep(STABLE_DELAY)
            # print(f"{time.time():.4f} : after sleeping {STABLE_DELAY} seconds")

            # pc.go_to(*GARAGE_CENTER, PARK_VEL)
            # print(f"{time.time():.4f} : after moving to {GARAGE_CENTER}")

            time.sleep(1)
        print(f"{time.time():.4f} : landed")
