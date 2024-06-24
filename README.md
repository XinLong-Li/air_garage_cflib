# air_garage_cflib
Parking a quadrotor into an air garage. This repository is based on the cflib from bitcrazy.

This repository is based on the `crazyflie-lib-python` from Bitcraze and the `optitrack_ws` . The `crazyflie-lib-python` is a Python library for controlling the Crazyflie 2.X nano quadcopter from Bitcraze, i.e. cflib. The `optitrack_ws` is a ROS workspace for the OptiTrack motion capture system.

The `src` directory contains the source code for the air garage project.



# ToDo (20240607)

1. 增加对动捕数据的记录代码，可以实时记录位置和姿态，记录速度，用来分析。
2. 修改底层控制器，并测试效果。目前已经可以从动捕获取到crazyflie的高度，可以测试CE和GE经典公式效果了。
当前的亚克力板高度是200mm，crazy螺旋桨的半径是23mm。后续考虑缩小点高度，缩小到在8R=8*23=184mm，或者6R=6*23=138mm。