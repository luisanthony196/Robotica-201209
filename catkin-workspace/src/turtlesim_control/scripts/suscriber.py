#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def suscriber():
    print('hello;)

if __name__ == '__main__':
    try:
        suscriber()
    except rospy.ROSInterruptException:
        pass
