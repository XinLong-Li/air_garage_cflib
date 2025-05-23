20240616_17_03_22.csv <br>
20240616_17_11_21.csv <br>
20240625_22_00_22.csv <br>
20240625_22_14_05.csv <br>
20240625_22_42_47.csv <br>
20240625_22_46_50.csv <br>
20240625_22_48_30.csv <br>
mocap_data/20240810_15_04_26.csv # <br>
mocap_data/20240810_15_45_11.csv <br>
mocap_data/20240810_17_36_56.csv <br>
mocap_data/20240810_17_42_39.csv <br>
mocap_data/20240810_17_49_46.csv <br>
mocap_data/20240810_17_54_57.csv <br>
mocap_data/20240810_17_58_29.csv # 10 centimeter high, go through the tunnel <br>
mocap_data/20240810_23_32_34.csv # 10 centimeter high, go through the tunnel <br>
mocap_data/20240811_00_06_23.csv <br>
mocap_data/20240811_00_09_47.csv <br>
mocap_data/20240811_00_13_46.csv <br>
mocap_data/20240811_00_18_00.csv # set 5 centimeter high, go through the tunnel, start point is (1.5,y,z=0.03) <br>
mocap_data/20240811_00_55_50.csv <br>
mocap_data/20240811_01_00_15.csv <br>
mocap_data/20240811_01_14_19.csv <br>
mocap_data/20240811_01_15_48.csv # set 5 cm high, 8 building blocks high(1.428*8), not collide with the ceiling <br>
mocap_data/20240811_01_18_04.csv # set 5 cm high, 4 building blocks high(1.428*4=5.712 cm), collide with the ceiling, delay 3 seconds after takeoff <br>
mocap_data/20240811_01_38_40.csv <br>
mocap_data/20240811_01_41_35.csv # set 6 cm high, 4 building blocks high(1.428*4=5.712 cm), collide with the ceiling, delay 4 seconds after takeoff <br>

mocap_data/20240811_01_43_45.csv # set 5 cm high, 4 building blocks high(1.428*4=5.712 cm), collide with the ceiling, delay 4 seconds after takeoff <br>

mocap_data/20240811_01_46_20.csv <br>
mocap_data/20240814_13_49_19.csv # set 50 cm high, without ceiling, calibrate the position tracking system <br>
mocap_data/20240814_20_48_21.csv <br>
mocap_data/20240814_20_56_53.csv <br>
mocap_data/20240814_21_01_15.csv <br>
mocap_data/20240814_21_10_38.csv <br>
mocap_data/20240814_21_19_13.csv <br>
mocap_data/20240814_22_15_07.csv <br>
mocap_data/20240814_22_16_49.csv <br>
mocap_data/20240814_22_22_07.csv <br>
mocap_data/20240814_22_24_52.csv <br>
mocap_data/20240814_23_40_43.csv <br>
mocap_data/20240814_23_44_03.csv <br>
mocap_data/20240814_23_52_49.csv <br>
mocap_data/20240815_00_27_14.csv <br>
mocap_data/20240815_00_29_10.csv # set 50 cm high, without ceiling, calibrate the position tracking system <br>
mocap_data/20240815_00_39_35.csv <br>
mocap_data/20240815_00_45_16.csv <br>
mocap_data/20240815_14_26_14.csv <br>
mocap_data/20240815_19_57_56.csv # set 50 cm high, no delay <br>
mocap_data/20240815_19_58_50.csv # set 50 cm high, no delay <br>
mocap_data/20240815_20_00_27.csv # set 50 cm high, no delay <br>

# The following data is collected by using PositionHLCommander class

mocap_data/20240815_22_05_06.csv <br>
mocap_data/20240815_23_59_15.csv <br>
mocap_data/20240816_00_03_47.csv <br>

## Spiral ascent flight test

mocap_data/20240816_00_11_25.csv # the first spiral ascent flight test <br>
mocap_data/20240816_00_22_16.csv # a successful spiral ascent flight <br>
mocap_data/20240820_00_10_33.csv <br>
## Minimum Height Hover Test

`mocap_data/20240821_16_36_54.csv` <br>
`mocap_data/20240821_16_44_07.csv` <br>
`mocap_data/20240821_17_07_06.csv` <br>

`mocap_data/20240821_17_23_10.csv` <br>
`mocap_data/20240821_17_31_39.csv` <br>
`mocap_data/20240821_17_48_25.csv` <br>
`mocap_data/20240821_17_57_21.csv` <br>
`mocap_data/20240821_18_01_45.csv` <br>
`mocap_data/20240821_18_05_12.csv` # set 0.5m，real height is 0.56m <br>
`mocap_data/20240822_17_29_40.csv` # set 0.44m，real height is 0.498m <br>
`mocap_data/20240822_17_35_39.csv` # set 0.44m，real height is 0.497m <br>

`mocap_data/20240822_17_48_07.csv` <br>
`mocap_data/20240822_17_52_59.csv` <br>
`mocap_data/20240822_17_56_30.csv` <br>
`mocap_data/20240822_17_58_56.csv` <br>
`mocap_data/20240822_18_03_19.csv` <br>

### Found the z tracking error cause: Overshoot

起飞后，延时了20s，发现是z轴的超调需要时间来消除，在延时14秒的时候基本达到了期望高度。也就是说，延时14s的时候基本达到了设定高度，会有+-5mm的波动，如果更换其他高度，跟踪时间可能会有所不同。

`mocap_data/20240822_18_09_53.csv` <br>
`mocap_data/20240822_18_23_29.csv` <br>

## 8 blocks, the ceiling height is 8*14.28mm=114.24mm, set 114.24mm/2=57.12mm high

`mocap_data/20240822_21_31_06.csv` # 8 blocks, set 0.057m high, a fail flight, didn't take off <br>
`mocap_data/20240822_21_32_29.csv` # 8 blocks, set 0.057m high, a successful flight <br>
`mocap_data/20240822_21_35_34.csv` # 8 blocks, set 0.057m high, a successful flight <br>
`mocap_data/20240822_21_38_32.csv` # 8 blocks, set 0.057m high, a fail flight, didn't take off, doubt the blocks blocked the mocap system <br>

`mocap_data/20240822_21_43_50.csv` # 8 blocks, set 0.057m high, a successful flight <br>
`mocap_data/20240822_21_49_06.csv` # no ceiling, set 0.057m high, a successful flight <br>
`mocap_data/20240822_21_53_18.csv` # no ceiling, set 0.057m high, a successful flight <br>

## 6 blocks, the ceiling height is 6*14.28mm=85.68mm, set 85.68mm/2=42.84mm high

`mocap_data/20240822_22_02_30.csv` # set 0.042m high, a successful flight <br>
`mocap_data/20240822_22_14_56.csv` # set 0.042m high, a successful flight <br>
`mocap_data/20240822_22_17_21.csv` # set 0.042m high, a successful flight <br>
`mocap_data/20240822_22_21_06.csv` # no ceiling, a successful flight <br>
`mocap_data/20240822_22_22_43.csv` # no ceiling, a successful flight <br>
`mocap_data/20240822_22_25_44.csv` # no ceiling, a successful flight <br>

## 4 blocks, the ceiling height is 4*14.28mm=57.12mm, set 57.12mm/2=28.56mm high

`mocap_data/20240822_22_37_19.csv` # set 0.028m high, didn't take off totally, the initial height is 0.028 <br>
`mocap_data/20240822_22_48_12.csv` # set 0.028m high, didn't take off totally, the initial height is 0.028 <br>
`mocap_data/20240822_22_50_52.csv` <br>
`mocap_data/20240822_22_52_35.csv` # set 0.035m high, didn't take off totally <br>
`mocap_data/20240822_22_54_22.csv` # set 0.035m high, didn't take off totally <br>
`mocap_data/20240822_22_59_51.csv` # set 0.035m high, didn't take off totally <br>
`mocap_data/20240822_23_05_30.csv` # set 0.04 high, didn't take off totally, because the mocap lost the crazyflie capture due to the low height, the acrylic board is too close to the marker. <br>

`mocap_data/20240822_23_09_12.csv` # set 0.04 high, collide with the ceiling
`mocap_data/20240822_23_31_19.csv` # set 0.035 high, collide with the ceiling
`mocap_data/20240822_23_34_04.csv`
`mocap_data/20240822_23_36_10.csv`
`mocap_data/20240822_23_37_03.csv` # set 0.03 high, didn't take off totally
`mocap_data/20240822_23_40_33.csv`
`mocap_data/20240822_23_43_14.csv`
`mocap_data/20240822_23_49_00.csv` # set 0.35 high, didn't take off totally
`mocap_data/20240822_23_50_54.csv` # set 0.04 high, collide with the ceiling

# Test on the table

## Hover on the table

### Set the offset height to 0.04m, The table height is 0.789m, The actual height is 0.789+0.04=0.829m

Each time the crazyflie take off from the same position(0.0, 0.0, 0.789).The following three data are collected during this condition. <br>
The max overshoot is 0.02m, setting the SET_DELAY value to 15s is enough to converge to the set height. <br>

`mocap_data/20240823_16_23_49.csv`
`mocap_data/20240823_16_34_07.csv` # set the SET_DELAY = 15 <br>
`mocap_data/20240823_16_48_25.csv` # set the SET_DELAY = 20 <br>
`mocap_data/20240823_17_13_29.csv` # failed to take off,set the SET_DELAY = 20 <br>
`mocap_data/20240823_17_17_04.csv` #  set the SET_DELAY = 20 <br>

## Set the offset height to 0.02m, set the SET_DELAY = 15

`mocap_data/20240823_17_25_20.csv` # no ceiling, set 0.02m high, a successful flight <br>
`mocap_data/20240823_17_35_08.csv` # with 4 blocks high ceiling, set 0.02m high, sucked to the ceiling <br>

## Set the offset height to 0.01m, set the SET_DELAY = 15

`mocap_data/20240823_17_42_02.csv` # with 4 blocks high ceiling, better than 0.02m, but still sucked to the ceiling <br>

### 5 blocks,hover
Take off two slow

`mocap_data/20240823_17_47_21.csv` # with ceiling , a successful flight <br>
`mocap_data/20240823_19_27_09.csv` # with ceiling , a successful flight <br>
`mocap_data/20240823_19_37_29.csv` with ceiling, good at begin, sucked to the ceiling at last <br>

## Land into the tunnel

Take off from an outside position (-0.204,-0.002,0.791), and land into the tunnel. <br>

`mocap_data/20240823_20_17_17.csv` with ceiling, sucked to the ceiling at last, the `OFFSET_HEIGHT` is 0.02m <br>
`mocap_data/20240823_22_50_12.csv` <br>
`mocap_data/20240823_22_51_47.csv` with ceiling, sucked to the ceiling at last, the `OFFSET_HEIGHT` is 0.01m <br>

## Pass through the tunnel,(take off then pass though the tunnel)


`mocap_data/20240823_23_23_04.csv` with ceiling，  <br>
`mocap_data/20240823_23_32_30.csv` crashed into the ceiling, the `OFFSET_HEIGHT` is 0.01m, the speed is 0.5m/s <br>

`mocap_data/20240823_23_47_49.csv` collided with the ceiling, the `OFFSET_HEIGHT` is 0.01m, the speed is 1m/s <br>

`mocap_data/20240823_23_51_06.csv` same as the last data <br>

`mocap_data/20240823_23_53_34.csv` increase the blocks from 5 to 6, the `OFFSET_HEIGHT` is 0.01m, the speed is 1m/s, perfect pass through the tunnel <br>

`mocap_data/20240823_23_58_03.csv` as perfect as the last data <br>

## Pass through the tunnel, (Land form high then pass through the tunnel)

Both of the following data are collected from very successful flights. <br>

`mocap_data/20240824_00_08_07.csv` First,take off from the table with a relative height 0.2m, then down 0.19m, then go through the tunnel <br>
`mocap_data/20240824_00_11_24.csv` First, take off from the table with a relative height 0.2m, then down 0.18m, then go through the tunnel <br>

# Test my firmware

## Without Ceiling Hovering

`mocap_data/20240827_16_07_17.csv` # set TAKEOFF_HEIGHT to 0.1m, delay is 10s <br>
`mocap_data/20240827_16_14_58.csv` # set TAKEOFF_HEIGHT to 0.1m, delay is 10s <br>
`mocap_data/20240827_16_23_24.csv` # set TAKEOFF_HEIGHT to 0.1m, delay is 15s <br>
`mocap_data/20240827_16_38_21.csv` # set TAKEOFF_HEIGHT to 0.05m, delay is 15s <br>
`mocap_data/20240827_16_41_48.csv` # set TAKEOFF_HEIGHT to 0.02m, delay is 15s <br>
`mocap_data/20240827_17_07_08.csv` # set TAKEOFF_HEIGHT to 0.01m, delay is 15s <br>

## With Ceiling Hovering (The ceiling height is 5 blocks)

Set TAKEOFF_HEIGHT to 0.01m, delay is 15s. <br> 

`mocap_data/20240827_18_45_10.csv` # a successful flight <br>
`mocap_data/20240827_18_46_05.csv` # sucked to the ceiling. <br>
`mocap_data/20240827_18_48_44.csv` # no collision deduced from the data <br>
`mocap_data/20240827_18_49_29.csv` # sucked to the ceiling. <br>
`mocap_data/20240827_18_56_52.csv` # a successful flight <br>

### Recollect some data with the same start point, approximately (0.001,0.001,0.791): <br>

`mocap_data/20240827_19_49_47.csv` # a successful flight <br>
`mocap_data/20240827_19_51_43.csv` # sucked to the ceiling <br>
`mocap_data/20240827_19_54_41.csv` # a successful flight <br>
`mocap_data/20240827_19_56_47.csv` # a successful flight <br>

## Now it‘s my firmware.

`mocap_data/20240827_20_44_37.csv` # Oh, no, it seems can't fly. <br>
`mocap_data/20240827_20_46_01.csv` # yes, bad news. <br>

### Bad news
`mocap_data/20240906_15_58_48.csv` # can't fly <br>
`mocap_data/20240906_16_04_39.csv` # Can fly, set NO_GROUND_EFFECT TRUE, set NO_CEILING_EFFECT TRUE  <br>
`mocap_data/20240906_16_17_55.csv` # can't fly, set NO_GROUND_EFFECT TRUE, set NO_CEILING_EFFECT FALSE <br>

### Enable the GE effect and the CE effect

`mocap_data/20240907_15_21_48.csv` # successful flight, without ceiling <br>
`mocap_data/20240907_15_45_03.csv` # with ceiling sucked to the ceiling and then recover.  <br>
`mocap_data/20240907_15_52_28.csv` # same as the last one <br>
`mocap_data/20240907_15_57_13.csv` # same, shit <br>

### if (dist_to_ceiling <= 0.1f * PROPELLER_RADIUS) ce_coefficient = 4.37f;

`mocap_data/20240907_16_06_12.csv` # same, shit <br>

### if (dist_to_ceiling <= 0.5f * PROPELLER_RADIUS) ce_coefficient = 1.21f;

`mocap_data/20240907_22_22_14.csv` # same shit <br>
`mocap_data/20240907_22_27_02.csv` # same shit, 但是有个中间被吸在天花板后恢复的情况，这是因为ce系数更新太慢了？ <br>

### Damn it, 前面忘记了把 NO_CEILING_EFFECT 设置为 FALSE

`mocap_data/20240907_23_15_20.csv` # Good, 没有撞墙。 <br>
`mocap_data/20240907_23_24_55.csv` # Good <br>

### Now Begin Collect some data with Ceiling, with my firmware

`mocap_data/20240907_23_31_17.csv` # 起始点是原点<br>
`mocap_data/20240907_23_32_12.csv` # 非原点<br>
`mocap_data/20240907_23_33_13.csv` # 非原点<br>
`mocap_data/20240907_23_43_25.csv` # 原点（好像有那么一霎那碰到顶了？）<br>
`mocap_data/20240907_23_44_50.csv` # 原点（好像有那么一霎那碰到顶了？）<br>
`mocap_data/20240907_23_47_39.csv` # 原点（没有碰到）<br>


`mocap_data/20250511_00_18_33.csv`
`mocap_data/20250511_00_35_35.csv`
`mocap_data/20250511_00_36_51.csv`
`mocap_data/20250511_00_59_11.csv`
`mocap_data/20250511_01_04_12.csv`
`mocap_data/20250511_15_06_14.csv`
`mocap_data/20250511_15_08_09.csv`
`mocap_data/20250511_15_08_19.csv`
`mocap_data/20250511_15_08_31.csv`
`mocap_data/20250511_15_09_34.csv`
`mocap_data/20250511_15_12_58.csv`
`mocap_data/20250511_15_19_33.csv`
`mocap_data/20250511_16_48_04.csv`
`mocap_data/20250511_16_50_22.csv`
`mocap_data/20250511_17_00_05.csv`
`mocap_data/20250511_17_05_17.csv`
`mocap_data/20250511_17_07_23.csv`
`mocap_data/20250511_17_11_22.csv`
`mocap_data/20250511_17_12_16.csv`
`mocap_data/20250511_17_13_50.csv`
`mocap_data/20250511_17_14_25.csv`
`mocap_data/20250511_17_15_12.csv`
`mocap_data/20250511_17_18_03.csv`
`mocap_data/20250511_17_19_26.csv`
`mocap_data/20250511_17_22_15.csv`
`mocap_data/20250511_17_23_18.csv`
`mocap_data/20250511_17_25_16.csv`
`mocap_data/20250511_17_26_15.csv`
`mocap_data/20250511_17_28_00.csv`
`mocap_data/20250511_17_28_55.csv`
`mocap_data/20250511_17_30_10.csv`
`mocap_data/20250511_17_31_30.csv`
`mocap_data/20250511_20_57_56.csv`
`mocap_data/20250511_21_03_15.csv`
`mocap_data/20250511_21_05_12.csv`
`mocap_data/20250511_21_15_37.csv`
`mocap_data/20250511_22_58_43.csv`
`mocap_data/20250511_23_02_27.csv`
`mocap_data/20250511_23_03_35.csv`
`mocap_data/20250511_23_05_19.csv`
`mocap_data/20250512_13_54_44.csv`
`mocap_data/20250512_13_58_46.csv`
`mocap_data/20250512_14_01_00.csv`
`mocap_data/20250512_14_03_08.csv`
`mocap_data/20250512_14_04_00.csv`
`mocap_data/20250512_14_06_20.csv`
`mocap_data/20250512_14_09_46.csv`
`mocap_data/20250512_14_25_20.csv`


`mocap_data/20250520_20_38_30.csv`
`mocap_data/20250520_20_40_30.csv`
`mocap_data/20250520_20_45_26.csv`
`mocap_data/20250520_21_08_06.csv`
`mocap_data/20250520_21_19_34.csv`
`mocap_data/20250520_21_38_21.csv`
`mocap_data/20250520_21_38_48.csv`
`mocap_data/20250520_21_38_52.csv`
`mocap_data/20250520_21_38_59.csv`
`mocap_data/20250520_21_41_41.csv`
`mocap_data/20250520_21_43_44.csv`
`mocap_data/20250520_21_46_20.csv`
`mocap_data/20250520_21_48_16.csv`
`mocap_data/20250520_22_09_58.csv`
`mocap_data/20250520_22_10_53.csv`
`mocap_data/20250520_22_12_13.csv`
`mocap_data/20250520_22_14_25.csv`
`mocap_data/20250520_22_35_20.csv`
`mocap_data/20250520_22_47_11.csv`
`mocap_data/20250520_22_57_20.csv`
`mocap_data/20250520_23_06_15.csv`
`mocap_data/20250520_23_37_08.csv`
`mocap_data/20250520_23_38_19.csv`
`mocap_data/20250520_23_50_34.csv`


`mocap_data/20250521_00_17_57.csv`
`mocap_data/20250521_12_38_09.csv`
`mocap_data/20250521_13_16_03.csv`
`mocap_data/20250521_13_17_08.csv`
`mocap_data/20250521_13_18_27.csv`
`mocap_data/20250521_13_19_41.csv`
`mocap_data/20250521_13_20_10.csv`
`mocap_data/20250521_13_20_40.csv`
`mocap_data/20250521_13_21_38.csv`
`mocap_data/20250521_13_22_12.csv`
`mocap_data/20250521_13_23_18.csv`
`mocap_data/20250521_14_05_57.csv`
`mocap_data/20250521_14_07_02.csv`
`mocap_data/20250521_14_07_59.csv`
`mocap_data/20250521_14_08_45.csv`
`mocap_data/20250521_14_13_56.csv`
`mocap_data/20250521_14_14_56.csv`
`mocap_data/20250521_14_16_49.csv`
`mocap_data/20250521_14_18_24.csv`
`mocap_data/20250521_14_19_14.csv`
`mocap_data/20250521_14_20_38.csv`
`mocap_data/20250521_14_24_22.csv`
`mocap_data/20250521_14_33_19.csv`
`mocap_data/20250521_14_44_09.csv`
`mocap_data/20250521_14_54_19.csv`
`mocap_data/20250521_14_56_48.csv`
`mocap_data/20250521_14_57_59.csv`
`mocap_data/20250521_14_58_41.csv`
`mocap_data/20250521_15_00_47.csv`
`mocap_data/20250521_15_00_50.csv`
`mocap_data/20250521_15_01_01.csv`
`mocap_data/20250521_15_33_24.csv`
`mocap_data/20250521_15_36_02.csv`
`mocap_data/20250521_15_37_31.csv`
`mocap_data/20250521_15_39_07.csv`
`mocap_data/20250521_15_42_15.csv`
`mocap_data/20250521_15_44_24.csv`

# Polynomial Trajectory

机库中心: (0.05,0.066,0.774)
起点位置：(-0.893,0.066,0.033)

## Start from higher position

高处出发。

### Group 1

#### Waypoint 1: perching_high.csv

-0.893, 0.066, 1.027
 0.10 , 0.066, 0.82
 0.283, 0.066, 0.775


#### Trajectory 1

Duration,x^0,x^1,x^2,x^3,x^4,x^5,x^6,x^7,y^0,y^1,y^2,y^3,y^4,y^5,y^6,y^7,z^0,z^1,z^2,z^3,z^4,z^5,z^6,z^7,yaw^0,yaw^1,yaw^2,yaw^3,yaw^4,yaw^5,yaw^6,yaw^7
3.38247,-0.893,0,0,0,0.111153,-0.0685307,0.0152793,-0.00120355,0.066,0,0,0,0,0,0,0,1.027,0,0,0,-0.0181182,0.0103519,-0.00216054,0.000161263,0,0,0,0,0,0,0,0
1.26592,0.1,0.32647,-0.0804616,-0.0248528,-0.143913,0.10595,0.0164133,-0.0179147,0.066,-9.83866e-19,2.26481e-18,2.08726e-18,0,0,0,0,0.82,-0.0784136,0.0195877,0.00583061,0.0191149,0.00363967,-0.0229884,0.00858619,0,0,0,0,0,0,0,0


`mocap_data/20250521_19_59_59.csv` # 撞顶
`mocap_data/20250521_20_14_33.csv` # 撞顶
`mocap_data/20250521_20_16_29.csv` # 撞顶

下面这两个其实证明了，GE和CE系数是其作用的。

`mocap_data/20250521_20_28_54.csv` # total thrust 除以1.2，起飞不了
`mocap_data/20250521_20_32_40.csv` # total thrust 不除1.2，可以起飞

`mocap_data/20250521_20_46_42.csv` # 测试了起点其实无所谓，起飞点乱放的


### Groupe 2

上一个轨迹不行，删除了，重新来。

#### Waypoint 2: perching_high2.csv

-0.893, 0.066, 1.027
 0.10 , 0.066, 0.82
 0.283, 0.066, 0.83

经过这个实验发现原来桌子高是0.745米，机库顶高是0.835米，之前因为每次路径的跟踪误差都是向下累积的，所以设置入库高度为0.82也没关系，实际高度可能不到0.8，但0.83已经撞到顶了。

#### Trajectory 2

Duration,x^0,x^1,x^2,x^3,x^4,x^5,x^6,x^7,y^0,y^1,y^2,y^3,y^4,y^5,y^6,y^7,z^0,z^1,z^2,z^3,z^4,z^5,z^6,z^7,yaw^0,yaw^1,yaw^2,yaw^3,yaw^4,yaw^5,yaw^6,yaw^7
3.37784,-0.893,0,0,0,0.114114,-0.0708452,0.015889,-0.00125772,0.066,0,0,0,0,0,0,0,1.027,0,0,0,-0.0445073,0.0303141,-0.0072213,0.000594561,0,0,0,0,0,0,0,0
1.34227,0.1,0.322539,-0.0790731,-0.024756,-0.181627,0.206919,-0.0682611,0.00504767,0.066,0,0,0,0,0,0,0,0.82,-0.000281228,0.0253503,0.00024869,-0.0312964,0.0137918,0.00445928,-0.00260871,0,0,0,0,0,0,0,0

`mocap_data/20250521_20_58_11.csv` # 撞顶

## Group 3

这里由于z轴的跟踪误差累积，所以要把waypoint设置的高一下，当前0.787入库是撞击到地板了。

### Waypoint 3: perching_high3.csv

这个虽然是perching_high3.csv，但后来删除了。
同时这里还把落点x轴的坐标由原来的0.283改成了0.2
把三个点改为了四个点，增加了一段平飞距离。

-0.893, 0.066, 1.027
 0.050, 0.066, 0.787
 0.100, 0.066, 0.787
 0.200, 0.066, 0.745

### Trajectory 3

3.44402,-0.893,0,0,0,0.102307,-0.0595023,0.012276,-0.000888289,0.066,0,0,0,0,0,0,0,1.027,0,0,0,-0.0491191,0.0332541,-0.0078859,0.000646801,0,0,0,0,0,0,0,0
0.628224,0.05,0.173272,-0.157897,0.00724174,-1.51745,5.55459,-6.72572,2.79517,0.066,-5.25344e-19,-9.88427e-19,-9.47205e-19,0,0,0,0,0.787,-0.00420265,0.0281928,0.00978374,0.111276,-0.910207,1.42168,-0.688103,0,0,0,0,0,0,0,0
1.14476,0.1,0.0584859,0.064172,0.00306906,0.75792,-1.8707,1.47074,-0.384082,0.066,6.39972e-18,9.8147e-18,-8.66741e-18,0,0,0,0,0.787,-0.017121,-0.0389822,-0.00438043,-0.314956,0.806194,-0.640691,0.168111,0,0,0,0,0,0,0,0


`mocap_data/20250522_13_48_00.csv` # 撞击地板入口
`mocap_data/20250522_13_49_11.csv` # 撞击地板入口

## Group 4

这里的第四个waypoint的z轴坐标比实际的要低一些。理论上无人机能到达的最低高度就是0.745+0.03m=0.775m了。但这次实验取得了极好的效果。也就是说因为最后一段轨迹z轴上由于需要较大的向下的加速度，所以z方向上的升力需要小一些。

同时这里的另一个点是降落点的位置靠近机库的入口了，这样由于无人机前两副螺旋桨由于突然遭受CE、GE造成的pitch变负（绕y轴顺时针选择），刚好实现了X轴上的减速效果。所以应该让入库时的X轴方向速度变大一些，这样不用因为为了抵消这个减速效果而增加后两副螺旋桨的升力（这怎么实现呢？）。

由于实际轨迹时一个凸弧线，那我设计一个凹弧线的轨迹是不是就可以了。

关于Pitch的正负定义，我使用右手的机体坐标系来定义的，X轴正方向指向前方，Y轴正方向指向左方，Z轴正方向指向上方。pitch角是绕着Y轴旋转的角度，使用右手螺旋定则来定义pitch角度，当无人机水平的时候，pitch角是0度的；当大拇指方向与Y轴正方向同向时，pitch记为正，此时无人机机头下腑，向前加速；当大拇指指向Y轴负方向时，pitch角记为负，此时无人机机头上仰，向后减速。

### Waypoint 4: perching_high3.csv

-0.893, 0.066, 1.027
 0.050, 0.066, 0.800
 0.100, 0.066, 0.790
 0.200, 0.066, 0.745


### Trajectory 4

3.49302,-0.893,0,0,0,0.109423,-0.0655228,0.0139311,-0.00103691,0.066,0,0,0,-3.46945e-18,1.73472e-18,-4.33681e-19,2.71051e-20,1.027,0,0,0,-0.0341035,0.0218848,-0.00496734,0.000392832,0,0,0,0,0,0,0,0
0.566246,0.05,0.163667,-0.129135,0.00614192,-1.36924,4.98733,-6.02178,2.49382,0.066,2.12213e-17,-4.37707e-18,-1.88536e-17,-3.55271e-15,1.42109e-14,0,0,0.8,-0.0274406,0.0279616,0.00646577,0.234126,-1.25033,1.84974,-0.903173,0,0,0,0,0,0,0,0
1.16715,0.1,0.0647204,0.0645311,0.00321059,0.587235,-1.48298,1.16363,-0.300927,0.066,-1.79093e-17,-1.36199e-17,1.47046e-17,2.22045e-16,-4.44089e-16,2.22045e-16,-5.55112e-17,0.79,-0.0245541,-0.0323537,-0.00534537,-0.284042,0.719289,-0.562989,0.145272,0,0,0,0,0,0,0,0


当前的状态（打开CE和GE，X_ADVC = 0.15f,落点靠前，x=0.2）

`mocap_data/20250522_14_07_38.csv` # 好消息，实验成功了。
`mocap_data/20250522_14_50_03.csv`
`mocap_data/20250522_14_51_38.csv` # 这三个视频都挺完美的。

#### 对比实验

##### 把CE和GE都关闭了，相同的轨迹，看看会不会撞到天花板。

当前的状态（关闭CE和GE，X_ADVC = 0.15f,落点靠前，x=0.2）


`mocap_data/20250522_14_55_28.csv` # 好消息，对比实验成功了。对比非常明显，直接撞向天花板

`mocap_data/20250522_14_59_33.csv` # 坏消息，撞击了地板，没有撞击天花板，可能是跟踪误差太大了。正是因为撞击了地板，才没有撞倒天花板，当可以看到距离天花板比之前近多了。

`mocap_data/20250522_15_01_24.csv` # 坏消息，还是撞击了地板。钻到地里面了。

`mocap_data/20250522_15_04_15.csv` # 坏消息，安全入库了，但可以看出，入库后的振荡较多。距离天花板也比较近。

`mocap_data/20250522_15_08_02.csv` # 坏消息，还是成功了，而且还挺好的呢。难道和换了电池有关？（第二次回溯：这次虽然好，当应该是没有打开CE和GE时的好，以后可以画图对比一下）

##### 下面打开CE和GE，还是成功的，看不出什么区别了。（第二次回溯，这个说法是不对的，是有区别的，明显有CE和GE好很多。）

当前的状态（打开CE和GE，X_ADVC = 0.15f,落点靠前，x=0.2）

`mocap_data/20250522_15_10_04.csv` # 这个视频是和15：08的视频看不出太大区别。
`mocap_data/20250522_15_13_27.csv` # 撞到地板了，但还是比14：59的好。最后距离天花板的距离也比14：59的要远。所以还是有效果的。

`mocap_data/20250522_15_21_30.csv` # 这个看着很好，比关闭CE、GE的明显好
`mocap_data/20250522_15_23_43.csv` # 这个虽然和15：04的看着区别比较小，当我觉得还是这个好，后续可以画个图。
换了电池，换回原来的了？
`mocap_data/20250522_15_28_57.csv` # 成功入库，入库的时候轻微撞击到了地面。这个好像很好。

##### 下面在固件里减小X_ADVC，之前是0.15f，现在调整为0.0f（也换了电池）

当前的状态（打开CE和GE，X_ADVC = 0.00f,落点靠前，x=0.2）

这三个都有点冲过头，往回减速的感觉。晚会减速这个过程基本是不可能撞顶的，只要不减速过头了再回调，我感觉这是一个不错的策略。
虽然三个的安全裕度都很大，但感觉这个三个都停靠的不是很稳，第一个没有跳动，但后两个停下来的时候跳了一下。

`mocap_data/20250522_15_35_44.csv` # 成功入库，没有撞击地面。我绝的也挺完美的。
`mocap_data/20250522_15_38_44.csv` # 成功入库，没有撞击地面。
`mocap_data/20250522_15_40_43.csv` # 成功入库，没有撞击地面。

#### 下面讲X_ADVC调大，设置为0.032f，这样是实际大小，重复3次实验。其实0.00和0.032区别不大，这里的3厘米可能没影响。

当前的状态（打开CE和GE，X_ADVC = 0.032f,落点靠前，x=0.2）

`mocap_data/20250522_15_46_35.csv` # 很完美。距离地面很安全，但反弹有一点点高。
`mocap_data/20250522_15_49_08.csv` # 也挺不错的，停入多了，还回退了一点，就是视频没对好焦。
`mocap_data/20250522_15_53_02.csv` # 也挺不错的，轻微撞击地面。

##### 下面关闭CE和GE，看看会不会撞到天花板。

当前的状态（关闭CE和GE，X_ADVC = 0.032f,落点靠前，x=0.2）

我感觉是因为我的这个位置选的好，无人机入库后往前冲了一点，CE和GE导致的无人机往后退刚好实现了后退。如果继续最终落点位置靠后一点会怎样？

（第二次回溯，明显看到区别，这条轨迹选的好，实际上安全裕度比关闭CE和GE小很多）

`mocap_data/20250522_15_59_54.csv` # 也成功了，但可以看到，距离天花板比较近。
`mocap_data/20250522_16_02_02.csv` # 也成功了，但可以看到，距离天花板比较近。
`mocap_data/20250522_16_05_54.csv` # 也成功了，感觉还挺完美的呢。其实很明显这里误差比较大了，可以做一张图对比一下。

###### 落点靠后，

当前的状态（关闭CE和GE，X_ADVC = 0.032f,落点靠后，x=0.3）

落点 x 的位置由 0.2 调整为 0.3

会不会和电池有关系呢？为什么后面这几次都撞击地面了？或在是落点改变了轨迹？我觉得是改变轨迹之后导致的。

`mocap_data/20250522_16_31_24.csv` # 果然，撞顶了

`mocap_data/20250522_16_35_58.csv` # 没撞顶，入库时撞击地面了，但最后距离天花板的有点近。比16：02的要近我感觉。

`mocap_data/20250522_16_38_40.csv` # 没撞顶，入库时撞击地面了，也有点近，但是没有比上一条近。

`mocap_data/20250522_16_40_33.csv` # 没撞顶，入库时撞击地面了，距离天花板距离有点近。

#### 下面打开CE和GE ：当前的状态（打开CE和GE，X_ADVC = 0.032f,落点靠后，x=0.3）

可以看到，距离天花板的距离比关闭了CE和GE的要远一些。说明还是有效果的。

`mocap_data/20250522_16_44_07.csv` # 飞太低了，被卡到地面上了。没进入。
`mocap_data/20250522_16_45_40.csv` # perfect，没撞倒地面也没撞倒顶。
`mocap_data/20250522_16_47_50.csv` # 撞倒地板了，但后面还不错
`mocap_data/20250522_16_51_03.csv` # 入库时好像有轻微的撞击地面，后面还不错。

#### 下面测试一下mixer的修改。

现在看这些个mixer感觉也不错欸，好像有效果啊，距离天花版的距离比关闭了CE和GE的要远一些。

`mocap_data/20250522_16_55_36.csv` # 入库撞到地板了，后面还不错，飞的过了，倒退了一点。
`mocap_data/20250522_17_03_40.csv` # 轻微撞倒地面，停的不是很稳定。没有一次性挺好，前面的也有类似问题。
`mocap_data/20250522_17_07_14.csv` # 没有撞倒地面，飞的比上一次好。

这两个是在8厘米高度下做的，也没有撞墙，四个黑色柱子
`mocap_data/20250522_17_11_20.csv` 有点撞顶了，前两副螺旋桨

`mocap_data/20250522_17_12_45.csv` 没有撞

## Middle Group

这个group的waypoints高度设置的太低了。deprecated

### Waypoint 5

-0.893, 0.066, 0.745
 0.050, 0.066, 0.745
 0.100, 0.066, 0.745
 0.300, 0.066, 0.745

### Trajectory 5

3.27915,-0.893,0,0,0,0.138713,-0.0880099,0.0198348,-0.00156663,0.066,0,0,0,6.93889e-18,-3.46945e-18,8.67362e-19,-5.42101e-20,0.745,0,0,0,2.22045e-16,-1.66533e-16,4.85723e-17,-3.90313e-18,0,0,0,0,0,0,0,0
0.580811,0.05,0.17164,-0.156186,0.00360198,-0.869287,3.04027,-3.26581,1.14988,0.066,-1.36527e-17,8.83661e-18,1.6294e-17,-3.55271e-15,1.42109e-14,0,0,0.745,-6.16719e-16,1.31251e-16,2.78753e-16,0,1.13687e-13,-2.27374e-13,1.13687e-13,0,0,0,0,0,0,0,0
1.62706,0.1,0.0563375,0.0688116,0.0225626,0.42182,-0.740903,0.408481,-0.0747813,0.066,3.02642e-17,-6.85664e-20,-1.94869e-17,-1.11022e-16,1.66533e-16,-5.55112e-17,1.38778e-17,0.745,8.44322e-16,4.08267e-16,-7.52968e-16,-3.55271e-15,5.32907e-15,-2.66454e-15,4.996e-16,0,0,0,0,0,0,0,0

### CE和GE都打开, 9厘米高度, mixer


`mocap_data/20250522_21_20_02.csv` # 高度太低，撞击到了地面

## Middle Group 2

### Waypoint 6

-0.893, 0.066, 0.780
 0.050, 0.066, 0.780
 0.100, 0.066, 0.780
 0.300, 0.066, 0.780

### Trajectory 6

3.27915,-0.893,0,0,0,0.138713,-0.0880099,0.0198348,-0.00156663,0.066,0,0,0,6.93889e-18,-3.46945e-18,8.67362e-19,-5.42101e-20,0.78,0,0,0,-1.38778e-16,1.11022e-16,-2.77556e-17,2.60209e-18,0,0,0,0,0,0,0,0
0.580811,0.05,0.17164,-0.156186,0.00360198,-0.869287,3.04027,-3.26581,1.14988,0.066,-1.36527e-17,8.83661e-18,1.6294e-17,-3.55271e-15,1.42109e-14,0,0,0.78,3.83196e-16,-5.9996e-17,-1.41936e-16,0,-1.13687e-13,0,0,0,0,0,0,0,0,0,0
1.62706,0.1,0.0563375,0.0688116,0.0225626,0.42182,-0.740903,0.408481,-0.0747813,0.066,3.02642e-17,-6.85664e-20,-1.94869e-17,-1.11022e-16,1.66533e-16,-5.55112e-17,1.38778e-17,0.78,-5.45719e-16,-3.43513e-16,5.91968e-16,2.66454e-15,-3.55271e-15,1.77636e-15,-3.33067e-16,0,0,0,0,0,0,0,0

`mocap_data/20250522_21_31_41.csv` # 撞击到顶了
关掉mixer试试

`mocap_data/20250522_21_50_15.csv` # 撞击到顶了，但比上次好了一些。


### Waypoint 7

我觉得当前的轨迹有点问题。下面这个点降低了最后一个落点的高度。

-0.893, 0.066, 0.780
 0.050, 0.066, 0.780
 0.100, 0.066, 0.780
 0.300, 0.066, 0.750

### Trajectory 7

3.27915,-0.893,0,0,0,0.139055,-0.0881752,0.0198529,-0.00156649,0.066,0,0,0,6.93889e-18,-3.46945e-18,8.67362e-19,-5.42101e-20,0.78,0,0,0,-0.00316048,0.00260276,-0.000718775,6.67754e-05,0,0,0,0,0,0,0,0
0.580811,0.05,0.166761,-0.159887,0.00364116,-0.195871,0.443534,0.307612,-0.559203,0.066,-1.42089e-17,4.17751e-18,1.11844e-17,-3.55271e-15,1.42109e-14,-1.42109e-14,7.10543e-15,0.78,0.00495906,-0.00110507,0.00176088,-0.0482745,-0.0132188,0.161707,-0.120779,0,0,0,0,0,0,0,0
1.60973,0.1,0.0552975,0.0679368,0.0229362,0.458203,-0.804868,0.446703,-0.082478,0.066,5.16119e-17,3.88964e-17,-4.25519e-17,-2.77556e-16,4.44089e-16,-2.22045e-16,3.46945e-17,0.78,-0.00822532,-0.0132575,-0.00237447,-0.0598755,0.108957,-0.061407,0.0114353,0,0,0,0,0,0,0,0

`mocap_data/20250522_22_06_40.csv` # 撞击到顶了，调整最后一个点的高度为0.75后的第一组数据，有改善，但不明显。
`mocap_data/20250522_22_15_41.csv` # 撞击到顶了，校正total thrust，除以1.1，有轻微改善

#### 减速距离提前了2个X_ADVC

`mocap_data/20250522_22_29_40.csv` # 撞击到顶了，减速距离提前了2个X_ADVC，有轻微改善。
`mocap_data/20250522_22_35_48.csv` # 没撞倒，但距离天花板很近
`mocap_data/20250522_22_42_33.csv` # 没撞倒，但距离天花板比较近

#### 接下来系数除以1.2

`mocap_data/20250522_23_02_18.csv` # 感觉该了系数还不行啊，还没有之前的好。
`mocap_data/20250522_23_03_59.csv` # 同前一次
`mocap_data/20250522_23_05_12.csv` # 这次可能没电了，没上桌，钻桌低下了。
`mocap_data/20250522_23_06_27.csv` # 这次乱飞起来了，直接上天。
`mocap_data/20250523_19_00_14.csv` # 撞击到顶了
`mocap_data/20250523_19_47_33.csv` # 撞击到顶了

#### 这个实验做着没有意义了，把1.2的除数去掉。

`mocap_data/20250523_20_00_11.csv` # 撞击到顶了，但比之前的好了一点
`mocap_data/20250523_20_02_00.csv` # 和上一次差不多

#### 把X_ADVC调小，设置为0.0f，这样是实际大小，重复3次实验。
