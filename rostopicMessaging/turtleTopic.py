

import roslib; roslib.load_manifest("teleop_twist_keyboard")

import rospy
from geometry_msgs.msg import Twist

import sys, tty, termios, select
msg = """
-------------------------
    Use Keyboard to Move:
        q   w   e
        a   s   d
        z   x   c

        g : quit
-------------------------
"""

# from https://github.com/ros-teleop/teleop_twist_keyboard/blob/master/teleop_twist_keyboard.py
def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key
# end of code section


keyMovements =  {
                    "q" : (1,0,0,1),
                    "w" : (1,0,0,0),
                    "e" : (1,0,0,-1),
                    "a" : (0,0,0,1),
                    "d" : (0,0,0,-1),
                    "z" : (-1,0,0,1),
                    "x" : (-1,0,0,0),
                    "c" : (-1,0,0,-1)
                }


# adapted from https://github.com/ros-teleop/teleop_twist_keyboard/blob/master/teleop_twist_keyboard.py


if __name__ == "__main__":

    settings = termios.tcgetattr(sys.stdin)
    pubMsg = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size = 1)
    rospy.init_node("turtle_teleop_key")

    x = 0 ; y = 0 ; z = 0 ; th = 0 ; speed = 0.5; turn = 1 ;


    try:
        print msg
        while True:
            keyInput = getKey()

            if keyInput in keyMovements.keys():
                x  = keyMovements[keyInput][0]
                y  = keyMovements[keyInput][1]
                z  = keyMovements[keyInput][2]
                th = keyMovements[keyInput][3]

            else:
                x = 0 ; y = 0 ; z = 0 ; th = 0 ;
                if keyInput == "g" or keyInput == "\x03":
                    break

            twistMsg = Twist()
            twistMsg.linear.x = x * speed
            twistMsg.linear.y = y * speed
            twistMsg.linear.z = z * speed
            twistMsg.angular.x = 0
            twistMsg.angular.y = 0
            twistMsg.angular.z = th * turn

            pubMsg.publish(twistMsg)


    except Exception as e:
        print e

    finally:
        twistMsg = Twist()
        twistMsg.linear.x = 0; twistMsg.linear.y = 0; twistMsg.linear.z = 0; twistMsg.angular.x = 0; twistMsg.angular.y = 0; twistMsg.angular.z = 0
        pubMsg.publish(twistMsg)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
