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
