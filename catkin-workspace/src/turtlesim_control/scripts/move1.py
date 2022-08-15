#!/usr/bin/env python
import sys
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose2D
from turtlesim.msg import Pose
from math import atan2, pow, sqrt

def callback(data):
    # Guardamos en parametros la posicion de la tortuga
    rospy.set_param('poseX', data.x)
    rospy.set_param('poseY', data.y)
    rospy.set_param('poseT', data.theta)

def calc(pos, obj):
    d = sqrt(pow(float(obj.x) - float(pos.x), 2) + pow(float(obj.x) + float(pos.y), 2))
    a = atan2(float(obj.y) - float(pos.y), float(obj.x) - float(pos.x))
    tupla = {
        "distancia" : d,
        "angulo" : a
    }
    return tupla

def move(x, y):
    # Inicamos el nodo goal
    rospy.init_node('goal', anonymous=True)
    # Iniciamos el publicador de la tortuga
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    # Obtenemos la posicion de la tortuga
    pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, callback)
    vel_msg = Twist()
    tupla = calc(Pose2D(rospy.get_param('poseX'),rospy.get_param('poseY'),0), Pose2D(x,y,0))
    # Definimos las velocidades que no usaremos en 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    while(3 <= tupla["distancia"]):
        # Realizamos el calculo
        tupla = calc(Pose2D(rospy.get_param('poseX'),rospy.get_param('poseY'),0), Pose2D(x,y,0))
        print(tupla["distancia"])
        vel_msg.linear.x = tupla["distancia"]
        vel_msg.angular.z = tupla["angulo"] - rospy.get_param('poseT')
        velocity_publisher.publish(vel_msg)
        rate.sleep()

    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.spin()


if __name__ == '__main__':
    try:
        if len(sys.argv) == 3:
            x = sys.argv[1]
            y = sys.argv[2]
            move(x, y)
        else:
            print("parametros incorrectos")
            sys.exit(1)
    except rospy.ROSInterruptException: pass
