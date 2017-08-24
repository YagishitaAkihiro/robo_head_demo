2017/8/25.26に行われる、JAXA 相模原キャンパス　で行われるデモ用のプログラムです。

dynamixelのMX-106を２個利用します。

[servo info]
id:1 tilt(上下)
id:2 pan (左右)

[依存関係]
・rospy
のみにしてるつもり。

[起動方法]
$sudo chmod 777 /dev/ttyUSB0
$roslaunch robo_head_demo controller_manager.launch
$roslaunch robo_head_demo start_tilt_controller.launch
$rosrun robo_head_demo demo.py(未調整)
windows側のnodeを叩く。
