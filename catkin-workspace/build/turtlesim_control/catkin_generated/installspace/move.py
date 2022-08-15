#!/usr/bin/env python2

from __future__ import print_function

import sys
import rospy
from geometry_msgs.msg import Twist

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def publisher(x, y):
    rospy.init_node('goal', anonymous=True)
    pub = rospy.Subscriber('/turtle1/cmd_vel', Twist, callback)
    rospy.spin()
    #rate = rospy.Rate(10)
    #while not rospy.is_shutdown():
        #print("hi %s %s"%(x, y))
        #rate.sleep()

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = sys.argv[1]
        y = sys.argv[2]
    else:
        print("parametros incorrectos")
        sys.exit(1)
    publisher(x, y)
