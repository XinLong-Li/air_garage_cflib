# launch步骤

详情请看[这篇博客](https://blog.csdn.net/qq_35713188/article/details/124687603)

```shell
 
source devel/setup.bash

roslaunch vrpn_client_ros sample.launch  server:=192.168.254.21 #这里的IP地址是运行Motive主机的地址


#然后另外开启一个终端
rostopic list  #此时正常的话应该可以查看到目标位置信息了


#保存数据到文件中
rostopic echo 话题名 >>data.txt

```
