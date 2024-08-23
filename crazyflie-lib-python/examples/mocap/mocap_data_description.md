20240616_17_03_22.csv
20240616_17_11_21.csv
20240625_22_00_22.csv
20240625_22_14_05.csv
20240625_22_42_47.csv
20240625_22_46_50.csv
20240625_22_48_30.csv
mocap_data/20240810_15_04_26.csv #
mocap_data/20240810_15_45_11.csv
mocap_data/20240810_17_36_56.csv
mocap_data/20240810_17_42_39.csv
mocap_data/20240810_17_49_46.csv
mocap_data/20240810_17_54_57.csv
mocap_data/20240810_17_58_29.csv # 10 centimeter high, go through the tunnel
mocap_data/20240810_23_32_34.csv # 10 centimeter high, go through the tunnel
mocap_data/20240811_00_06_23.csv
mocap_data/20240811_00_09_47.csv
mocap_data/20240811_00_13_46.csv
mocap_data/20240811_00_18_00.csv # set 5 centimeter high, go through the tunnel, start point is (1.5,y,z=0.03)
mocap_data/20240811_00_55_50.csv
mocap_data/20240811_01_00_15.csv
mocap_data/20240811_01_14_19.csv
mocap_data/20240811_01_15_48.csv # set 5 cm high, 8 building blocks high(1.428*8), not collide with the ceiling
mocap_data/20240811_01_18_04.csv # set 5 cm high, 4 building blocks high(1.428*4=5.712 cm), collide with the ceiling, delay 3 seconds after takeoff
mocap_data/20240811_01_38_40.csv
mocap_data/20240811_01_41_35.csv # set 6 cm high, 4 building blocks high(1.428*4=5.712 cm), collide with the ceiling, delay 4 seconds after takeoff

mocap_data/20240811_01_43_45.csv # set 5 cm high, 4 building blocks high(1.428*4=5.712 cm), collide with the ceiling, delay 4 seconds after takeoff

mocap_data/20240811_01_46_20.csv
mocap_data/20240814_13_49_19.csv # set 50 cm high, without ceiling, calibrate the position tracking system
mocap_data/20240814_20_48_21.csv
mocap_data/20240814_20_56_53.csv
mocap_data/20240814_21_01_15.csv
mocap_data/20240814_21_10_38.csv
mocap_data/20240814_21_19_13.csv
mocap_data/20240814_22_15_07.csv
mocap_data/20240814_22_16_49.csv
mocap_data/20240814_22_22_07.csv
mocap_data/20240814_22_24_52.csv
mocap_data/20240814_23_40_43.csv
mocap_data/20240814_23_44_03.csv
mocap_data/20240814_23_52_49.csv
mocap_data/20240815_00_27_14.csv
mocap_data/20240815_00_29_10.csv # set 50 cm high, without ceiling, calibrate the position tracking system
mocap_data/20240815_00_39_35.csv
mocap_data/20240815_00_45_16.csv
mocap_data/20240815_14_26_14.csv
mocap_data/20240815_19_57_56.csv # set 50 cm high, no delay
mocap_data/20240815_19_58_50.csv # set 50 cm high, no delay
mocap_data/20240815_20_00_27.csv # set 50 cm high, no delay

# The following data is collected by using PositionHLCommander class

mocap_data/20240815_22_05_06.csv
mocap_data/20240815_23_59_15.csv
mocap_data/20240816_00_03_47.csv

## Spiral ascent flight test

mocap_data/20240816_00_11_25.csv # the first spiral ascent flight test
mocap_data/20240816_00_22_16.csv # a successful spiral ascent flight
mocap_data/20240820_00_10_33.csv

# Minimum Height Hover Test


mocap_data/20240821_16_36_54.csv
mocap_data/20240821_16_44_07.csv
mocap_data/20240821_17_07_06.csv

mocap_data/20240821_17_23_10.csv
mocap_data/20240821_17_31_39.csv
mocap_data/20240821_17_48_25.csv
mocap_data/20240821_17_57_21.csv
mocap_data/20240821_18_01_45.csv
mocap_data/20240821_18_05_12.csv # set 0.5m，real height is 0.56m
mocap_data/20240822_17_29_40.csv # set 0.44m，real height is 0.498m
mocap_data/20240822_17_35_39.csv # set 0.44m，real height is 0.497m

mocap_data/20240822_17_48_07.csv
mocap_data/20240822_17_52_59.csv
mocap_data/20240822_17_56_30.csv
mocap_data/20240822_17_58_56.csv
mocap_data/20240822_18_03_19.csv
mocap_data/20240822_18_09_53.csv # 起飞后，延时了20s，发现是z轴的超调需要时间来消除，在延时14秒的时候基本达到了期望高度。
mocap_data/20240822_18_23_29.csv # 也就是说，延时14s的时候基本达到了设定高度，会有+-5mm的波动，如果更换其他高度，跟踪时间可能会有所不同。


## 8 blocks, the ceiling height is 8*14.28mm=114.24mm, set 114.24mm/2=57.12mm high

mocap_data/20240822_21_31_06.csv # 8 blocks, set 0.057m high, a fail flight, didn't take off
mocap_data/20240822_21_32_29.csv # 8 blocks, set 0.057m high, a successful flight
mocap_data/20240822_21_35_34.csv # 8 blocks, set 0.057m high, a successful flight
mocap_data/20240822_21_38_32.csv # 8 blocks, set 0.057m high, a fail flight, didn't take off, doubt the blocks blocked the mocap system

mocap_data/20240822_21_43_50.csv # 8 blocks, set 0.057m high, a successful flight
mocap_data/20240822_21_49_06.csv # no ceiling, set 0.057m high, a successful flight
mocap_data/20240822_21_53_18.csv # no ceiling, set 0.057m high, a successful flight

## 6 blocks,  the ceiling height is 6*14.28mm=85.68mm, set 85.68mm/2=42.84mm high

mocap_data/20240822_22_02_30.csv # set 0.042m high, a successful flight
mocap_data/20240822_22_14_56.csv # set 0.042m high, a successful flight
mocap_data/20240822_22_17_21.csv # set 0.042m high, a successful flight
mocap_data/20240822_22_21_06.csv # no ceiling, a successful flight
mocap_data/20240822_22_22_43.csv # no ceiling, a successful flight
mocap_data/20240822_22_25_44.csv # no ceiling, a successful flight

## 4 blocks, the ceiling height is 4*14.28mm=57.12mm, set 57.12mm/2=28.56mm high

mocap_data/20240822_22_37_19.csv # set 0.028m high, didn't take off totally, the initial height is 0.028
mocap_data/20240822_22_48_12.csv # set 0.028m high, didn't take off totally, the initial height is 0.028
mocap_data/20240822_22_50_52.csv
mocap_data/20240822_22_52_35.csv # set 0.035m high, didn't take off totally
mocap_data/20240822_22_54_22.csv # set 0.035m high, didn't take off totally
mocap_data/20240822_22_59_51.csv # set 0.035m high, didn't take off totally
mocap_data/20240822_23_05_30.csv # set 0.04 high, didn't take off totally, because the mocap lost the crazyflie capture due to the low height, the acrylic board is too close to the marker.

mocap_data/20240822_23_09_12.csv # set 0.04 high, collide with the ceiling
mocap_data/20240822_23_31_19.csv # set 0.035 high, collide with the ceiling
mocap_data/20240822_23_34_04.csv
mocap_data/20240822_23_36_10.csv
mocap_data/20240822_23_37_03.csv # set 0.03 high, didn't take off totally
mocap_data/20240822_23_40_33.csv
mocap_data/20240822_23_43_14.csv
mocap_data/20240822_23_49_00.csv # set 0.35 high, didn't take off totally
mocap_data/20240822_23_50_54.csv # set 0.04 high, collide with the ceiling
mocap_data/20240823_14_33_45.csv
mocap_data/20240823_14_37_35.csv
