# Summer2016-ROS
ROS Indigo Project


## Summary
This project served as an introduction to the ROS Indigo platform as part of a larger project that will involve building a miniature car that will be controlled via ROS Twist messaging.

## carModel
This folder contains the carModel.xacro file along with additional files used for displaying the car model in the RViz program.  The carModel has not yet been completed to the point that Twist messages from the command line will move it.

## rostopicMessaging
This folder contains carTwist.py, a program that publishes Twist messages to the "cmd_vel" channel in order to move a completed robot, and turtleTopic.py, a program for interacting with the ROS TurtleSim via the keyboard.
