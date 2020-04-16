#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time


def move():
    # Starts a new node
    rospy.init_node('robotont_velocity_publisher', anonymous=True)
    velocity_publisher = rospy.Publisher(
        '/robotont/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    side_length = 20            # 1/10th of a second
    turn_length = 10            # 1/10th of a second
    turn_speed = math.pi / 4    # turn 45 degrees per second
    while not rospy.is_shutdown():

        # Loop to move the turtle in an specified distance
        try:
            # Drive straight
            for i in range(0, side_length):
                vel_msg.linear.x = 1
                vel_msg.linear.y = 0
                vel_msg.angular.z = 0
                velocity_publisher.publish(vel_msg)
                rospy.sleep(0.1)

            # Rotate
            for i in range(0, turn_length):
                vel_msg.linear.x = 0
                vel_msg.linear.y = 0
                vel_msg.angular.z = turn_speed
                velocity_publisher.publish(vel_msg)
                rospy.sleep(0.1)

            # After the loop, stops the robot
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            # Send the stop message to the robot
            velocity_publisher.publish(vel_msg)
            rospy.sleep(1)

        except KeyboardInterrupt:
            # Stop the robot before exiting
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            # Send the stop message to the robot
            velocity_publisher.publish(vel_msg)
            rospy.sleep(1)


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
