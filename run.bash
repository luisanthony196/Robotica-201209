#!/bin/bash

rostopic pub /my_turtle/turtle1/cmd_vel geometry_msgs/Twist -1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]'
rostopic pub /my_turtle/turtle1/cmd_vel geometry_msgs/Twist -1 -- '[0.0, 0.0, 0.0]' '[0.0, 0.0, 1.55]'
rostopic pub /my_turtle/turtle1/cmd_vel geometry_msgs/Twist -1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]'
rostopic pub /my_turtle/turtle1/cmd_vel geometry_msgs/Twist -1 -- '[0.0, 0.0, 0.0]' '[0.0, 0.0, 1.55]'
rostopic pub /my_turtle/turtle1/cmd_vel geometry_msgs/Twist -1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]'
rostopic pub /my_turtle/turtle1/cmd_vel geometry_msgs/Twist -1 -- '[0.0, 0.0, 0.0]' '[0.0, 0.0, 1.55]'
rostopic pub /my_turtle/turtle1/cmd_vel geometry_msgs/Twist -1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]'

