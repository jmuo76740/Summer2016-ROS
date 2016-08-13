# Summer2016-ROS
ROS Indigo Project


## Summary
This project served as an introduction to the ROS Indigo platform as part of a larger project that will involve building a miniature car that will be controlled via ROS Twist messaging.

### carModel
This folder contains the carModel.xacro file along with additional files used for displaying the car model in the RViz program.  The carModel has not yet been completed to the point that Twist messages from the command line will move it.

### rostopicMessaging
This folder contains carTwist.py, a program that publishes Twist messages to the "cmd_vel" channel in order to move a completed robot, and turtleTopic.py, a program for interacting with the ROS TurtleSim via the keyboard.


## Usage

* carModel
  1. Download and move into the carModel directory
  2. Open carModel.xacro in RViz using one of the two following commands
    * `roslaunch carModel display.launch`
        OR
    * `roslaunch carModel display.launch model:=urdf/carModel.xacro`
  3. View carModel in RViz
    * a secondary window will open that allows for the two front wheels to be spinned


* rostopicMessaging

  * Using TurtleSim 
    1. Download and move into rostopicMessaging directory
    2. Launch "roscore"
    3. Open new terminal
    4. Open TurtleSim
      * `rosrun turtlesim turtlesim_node`
    5. Open new terminal
    6. Run "turtleTopic.py"
      * `python turtleTopic.py`
    7. Use the keyboard to move the turtle
  
  * Using Arbotix Robot Model
    1. Install Arbotix Simulator
      * `sudo apt-get install ros-indigo-arbotix`
      * `rospack profile`
    2. Launch "roscore"
    3. Launch the Arbotix simulator
      * `roslaunch rbx1_bringup fake_turtlebot.launch`
    4. Launch the robot model
      * ``rosrun rviz rviz -d `rospack find rbx1_nav`/sim.rviz``
    5. Download and move into rostopicMessaging directory
    6. Run "carTwist.py"
      * `python carTwist.py`
    7. Use the keyboard to move the robot model

