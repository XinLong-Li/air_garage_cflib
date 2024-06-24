"""
This script is used for read pose from optitrack through vrpn.
"""
import logging
import time

import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.crazyflie.extpos import Extpos  # use external positioning system
from cflib.positioning.position_hl_commander import PositionHlCommander

import numpy as np
import rospy
from geometry_msgs.msg import PoseStamped



URI = 'radio://0/80/2M/E7E7E7E701'

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

ITER_THRESHOLD = 30
MOVE_RESOLUTION = 0.05

cur_pose = np.zeros(7) # [x, y, z, qx, qy, qz, qw]

IS_POSE_UPDATED = False


def cf1_callback(data):
    """
    callback function of cf1 pose subscribe
    """
    global cur_pose # pylint: disable=global-statement
    global IS_POSE_UPDATED # pylint: disable=global-statement
    cur_pose[0] = data.pose.position.x
    cur_pose[1] = data.pose.position.y
    cur_pose[2] = data.pose.position.z
    cur_pose[3] = data.pose.orientation.x
    cur_pose[4] = data.pose.orientation.y
    cur_pose[5] = data.pose.orientation.z
    cur_pose[6] = data.pose.orientation.w
    IS_POSE_UPDATED = True
    # print('-----------------------------------------------')
    # print("cur_pose: ",cur_pose)


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    rospy.init_node('crazy_planner', anonymous=True)
    rate = rospy.Rate(50)
    rospy.Subscriber("/vrpn_client_node/cf1/pose", PoseStamped, cf1_callback)
   
    with SyncCrazyflie(URI) as scf:
        cf = scf.cf
        # ext_pose = Extpos(scf)
        # rd_pos = PositionHlCommander(scf)
        # int_pose = [0.0, 0.0, 0.0]
        # print("##############")

        # while not rospy.is_shutdown():
        #     print("enter loop")
        #     if(IS_POSE_UPDATED==True):
        #         IS_POSE_UPDATED = False
        #         cf.extpos.send_extpose(cur_pose[0], cur_pose[1], cur_pose[2], 
        #                             cur_pose[3], cur_pose[4], cur_pose[5], cur_pose[6])
        #         int_pos =rd_pos.get_position
        #         print('**************')
        #         print("int_pose: ",int_pos)
        #     # rate.sleep()

        # It takes off when the commander is created
        with MotionCommander(scf) as mc:
            print('Taking off!')
            time.sleep(0.1)

            # ext_pose = Extpos(cf)
            rd_pos = PositionHlCommander(cf)
            int_pose = [0.0, 0.0, 0.0]

            while not rospy.is_shutdown():
                if(IS_POSE_UPDATED):
                    cf.extpos.send_extpose(cur_pose[0], cur_pose[1], cur_pose[2],
                                          cur_pose[3], cur_pose[4], cur_pose[5], cur_pose[6])
                    int_pos =rd_pos.get_position
                    mc.forward(0.5)
                    mc.back(0.5)
                    print("Enter the while loop")
                rate.sleep()

        print('Landing')
    print("end")
