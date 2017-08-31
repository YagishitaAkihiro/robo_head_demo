#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Pose
import tf

b_pan = 0.785
b_til = 0.785

class Demo():
      def __init__(self):
          rospy.init_node("demo")
          rospy.loginfo("start_node")
          self.pan_pub  = rospy.Publisher("/pan_controller/command", Float64, queue_size=1)
          self.tilt_pub = rospy.Publisher("/tilt_controller/command", Float64, queue_size=1)
          self.pan_pub.publish(0)
          #rospy.Subscriber("/pan",  Float64, self.pan_cb,  queue_size=1)
          #rospy.Subscriber("/tilt", Float64, self.tilt_cb, queue_size=1)
          rospy.Subscriber("oculus_ori", Pose , self.cb, queue_size=1)
          rospy.spin()

      def cb(self,data):
#          print data
          angle = tf.transformations.euler_from_quaternion((data.orientation.x,data.orientation.y,data.orientation.z,data.orientation.w))
 #         print "x: " + str(angle[0]) + ", y: " + str(angle[1]) + ", z: " + str(angle[2])
          #x:updawn z:rightleft
          """
          if data.orientation.y < 0:
             pan = -angle[1]
          else:
             pan = angle[1]
          if data.orientation.x < 0:
             til = -angle[1]
          else:
             pan = angle[1]
          """
          global b_pan, b_til
          if not -0.05 < (b_pan - (angle[1]+0.785)) < 0.05:
             self.pan_pub.publish(round((b_pan + (angle[1]+0.785))/2,3))
          if not -0.05 < (b_til - (angle[0]+0.785)) < 0.05:
             self.tilt_pub.publish(round((b_til + (angle[0]+0.785))/2,3))
          b_pan = angle[1]+0.785
          b_til = angle[0]+0.785
if __name__ == "__main__":
   try:
      Demo()
   except:
      rospy.loginfo("shutdown_node")
