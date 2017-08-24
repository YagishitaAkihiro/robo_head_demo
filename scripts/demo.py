#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64

class Demo():
      def __init__(self):
          rospy.init_node("demo")
          rospy.loginfo("start_node")
          self.pan_pub  = rospy.Publisher("/pan_controller/command", Float64, queue_size=1)
          self.tilt_pub = rospy.Publisher("/tilt_controller/command", Float64, queue_size=1)
          rospy.Subscriber("pan",  Float64, self.pan_cb,  queue_size=1)
          rospy.Subscriber("tilt", Float64, self.tilt_cb, queue_size=1)
         #rospy.Subscriber("pan_tilt", ----- , self.cb, queue_size=1)
          rospy.spin()

      def pan_cb(self,pan):
          print "pan: " + str(pan)
          self.pan_pub.publish(pan)
      def tilt_cb(self,tilt):
          print "tilt: "+ str(tilt)
          self.tilt_pub.publish(tilt)

      def cb(self,data):
          pass

if __name__ == "__main__":
   try:
      Demo()
   except:
      rospy.loginfo("shutdown_node")
