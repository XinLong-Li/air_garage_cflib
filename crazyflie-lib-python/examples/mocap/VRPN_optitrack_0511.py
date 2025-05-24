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

pose_file = None
# URI to the Crazyflie to connect to
uri = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

URI = 'radio://0/80/2M/E7E7E7E7E7'

# True: send position and orientation; False: send position only
send_full_pose = True

# When using full pose, the estimator can be sensitive to noise in the orientation data when yaw is close to +/- 90
# degrees. If this is a problem, increase orientation_std_dev a bit. The default value in the firmware is 4.5e-3.
orientation_std_dev = 4.5e-3

# Duration,x^0,x^1,x^2,x^3,x^4,x^5,x^6,x^7,y^0,y^1,y^2,y^3,y^4,y^5,y^6,y^7,z^0,z^1,z^2,z^3,z^4,z^5,z^6,z^7,yaw^0,yaw^1,yaw^2,yaw^3,yaw^4,yaw^5,yaw^6,yaw^7
perching = [
    [
6.33577,-0.893,0,0,0,0.00952812,-0.00320814,0.000388167,-1.65088e-05,0.066,0,0,0,-5.20417e-18,2.05998e-18,-2.84603e-19,1.2282e-20,0.79,0,0,0,-0.000600072,0.000268562,-4.0317e-05,2.0325e-06,0,0,0,0,0,0,0,0
],
    [
1.15246,0.05,0.148113,-0.021554,-0.00295152,-0.363794,0.567811,-0.32282,0.0652522,0.066,7.61766e-17,-1.68093e-17,-9.67909e-18,-4.44089e-16,8.88178e-16,-6.66134e-16,1.66533e-16,0.79,0.00394818,-0.00022183,0.00215153,0.135855,-0.320495,0.244779,-0.062642,0,0,0,0,0,0,0,0
],
    [
1.4035,0.12,-6.99738e-05,0.00427007,0.00768509,0.166585,-0.23262,0.117364,-0.0210835,0.066,-2.62762e-17,3.55132e-18,7.38633e-18,2.22045e-16,-2.22045e-16,1.11022e-16,0,0.79,-0.0245914,-0.0132351,-0.00239316,-0.139667,0.26655,-0.164667,0.0341315,0,0,0,0,0,0,0,0
],
    [
1.11351,0.2,0.0933366,-0.00588084,-0.0131599,-0.119053,0.129709,-0.0311934,-0.00378209,0.066,9.44811e-18,-1.17366e-17,-2.09397e-18,-2.22045e-16,4.44089e-16,0,0,0.74,-0.00347952,0.0144062,-0.00560331,0.182011,-0.410978,0.316082,-0.0824656,0,0,0,0,0,0,0,0
],
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


def run_sequence(cf: Crazyflie, trajectory_id, duration,start_pos):
    commander = cf.high_level_commander
    x, y, z = start_pos

    commander.takeoff(0.2, 2.0)
    commander.go_to(x=x, y=y, z=z, yaw=0.0, duration_s=6.0)

    time.sleep(13.0)
    relative =  False
    # relative = True
    traj_start_time = time.time()
    commander.start_trajectory(trajectory_id, 1.0, relative)
    time.sleep(duration)
    commander.land(0.0, 2.0)
    time.sleep(2)
    commander.stop()
    with open(pose_file, 'a', newline='', encoding='utf-8') as cb_file:
        traj_start_time_tracker = csv.writer(cb_file)
        traj_start_time_tracker.writerow([traj_start_time])




def pose_callback(data):
    '''
    callback function for the crazyflie pose subscriber

    data: the pose data from the mocap system, ROS message type is geometry_msgs/PoseStamped
    '''
    t = time.time()
    global pose_file  # Declare pose_file as global to modify the global variable
    pose = [data.pose.position.x, data.pose.position.y, data.pose.position.z, data.pose.orientation]
    send_extpose_quat(cf, pose[0], pose[1], pose[2], pose[3]) # x, y, z, quat
    with open(pose_file, 'a', newline='', encoding='utf-8') as cb_file:
        pose_writer = csv.writer(cb_file)
        pose_writer.writerow([t, pose[0], pose[1], pose[2], pose[3].x, pose[3].y, pose[3].z, pose[3].w])

def hover(scf: SyncCrazyflie):
    with PositionHlCommander(scf, 
                             x = -0.893,
                             y =  0.066,
                             z =  0.033,
                             default_velocity=0.2,
                             default_height=0.82 ) as pc:
        time.sleep(5)
        pc.go_to(x=-0.893, y=0.066, z=0.82, yaw=0.0, duration_s=5.0)
        time.sleep(8)
        pc.go_to(x=0.238, y=0.066, z=0.78, yaw=0.0, duration_s=5.0)
        time.sleep(8)

def hover2(scf:SyncCrazyflie,start_pos=[0,0,0],end_pos=[0,0,0]):
    cf= scf.cf
    # x, y, z = start_pos
    # x_end, y_end, z_end = end_pos
    cf.high_level_commander.takeoff(0.5, 2.0)
    time.sleep(10.0)
    # cf.high_level_commander.go_to(x=x, y=y, z=z, yaw=0.0, duration_s=6.0)
    # time.sleep(10.0)
    # cf.high_level_commander.go_to(x=x_end, y=y_end, z=z_end, yaw=0.0, duration_s=6.0) 
    # time.sleep(10.0)
    cf.high_level_commander.land(absolute_height_m=0.0, duration_s=2.0) #absolute height is the final height
    time.sleep(2.0)
    cf.high_level_commander.stop()



if __name__ == '__main__':
    print(f"{time.time():.4f} : Start the program")
    cflib.crtp.init_drivers()

    pose_file = os.path.join('mocap_data', datetime.now().strftime('%Y%m%d_%H_%M_%S') + '.csv')
    with open(pose_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['t', 'x', 'y', 'z', 'qx', 'qy', 'qz', 'qw'])

    pose_file_collection = 'mocap_data_description.md'
    with open(pose_file_collection, 'a', encoding='utf-8') as file:
        file.write(f'\n`{pose_file}`\n')

    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        cf = scf.cf
        trajectory_id = 1
        start_pos = [-0.893, 0.066, 0.790]
        # end_pos = [0.283, 0.066, 0.78]
        # start_pos = [-0.893, 0.066, 0.78]

        rospy.init_node('cf_lxl_node', anonymous=True)
        rospy.Subscriber("/vrpn_client_node/cf_lxl/pose", PoseStamped, pose_callback)

        adjust_orientation_sensitivity(cf)
        activate_kalman_estimator(cf)
        # activate_mellinger_controller(cf)
        duration = upload_trajectory(cf, trajectory_id, perching)
        print('The sequence is {:.1f} seconds long'.format(duration))
        reset_estimator(cf)
        # hover2(scf,start_pos,end_pos)
        run_sequence(cf, trajectory_id, duration,start_pos)
        # hover2(scf)
        print(f"{time.time():.4f} : landed")
