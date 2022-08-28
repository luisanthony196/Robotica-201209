#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class TurtleBot:
    def __init__(self):
        rospy.init_node('burger', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.prox_subscriber = rospy.Subscriber('/scan', LaserScan, self.update_prox)
        self.prox = LaserScan()
        self.rate = rospy.Rate(10)

    def update_prox(self, data):
        self.prox = data

    def move(self):
        vel_msg = Twist()
        t0 = rospy.Time.now().to_sec()
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        while(True):
            range_ahead = 0
            if (len(self.prox.ranges) > 0):
                mini = self.prox.range_min
                ahead = self.prox.ranges[0]
                left = self.prox.ranges[15]
                right = self.prox.ranges[345]
                print(ahead, right, left)
                if (ahead - mini <= 0.25 or left - mini <= 0.15 or right - mini <= 0.15):
                    if (left > right):
                        vel_msg.linear.x = 0.1
                        vel_msg.angular.z = 0.6
                    else:
                        vel_msg.linear.x = 0.1
                        vel_msg.angular.z = -0.6
                else:
                    vel_msg.linear.x = 0.2
                    vel_msg.angular.z = 0
                self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        burger = TurtleBot()
        burger.move()
    except rospy.ROSInterruptException:
        pass
