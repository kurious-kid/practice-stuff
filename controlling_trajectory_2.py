#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

class initial_turtle:

	def __init__(self):
		# Starts a new node called my_initials
		rospy.init_node('my_initials', anonymous=True)
		self.the_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)


	def move(self):
		print("inside move")
		the_velocity = Twist()

		the_velocity.linear.x = 0
		the_velocity.linear.y = 1
		the_velocity.linear.z = 0
		the_velocity.angular.x = 0
		the_velocity.angular.y = 0
		the_velocity.angular.z = 0

		while not rospy.is_shutdown():
			self.the_publisher.publish(the_velocity)
			init_time = rospy.Time.now().to_sec()
			curr_time = rospy.Time.now().to_sec()

			while(curr_time - init_time < 5):
				self.the_publisher.publish(the_velocity)
				curr_time = rospy.Time.now().to_sec()

			# stopping the robot here
			the_velocity.linear.y = 0
			self.the_publisher.publish(the_velocity)

			# now going for angular velocity...that is now going for the curve in my name
			the_velocity.linear.x = 1.5
			the_velocity.linear.y = -1
			the_velocity.linear.z = 0
			the_velocity.angular.x = 0
			the_velocity.angular.y = 0
			the_velocity.angular.z = -0.97

			init_time = rospy.Time.now().to_sec()
			curr_time = rospy.Time.now().to_sec()
			while (curr_time - init_time < 2):
				self.the_publisher.publish(the_velocity)
				curr_time = rospy.Time.now().to_sec()

			# stopping the robot here
			the_velocity.linear.x = 0
			the_velocity.linear.y = 0
			the_velocity.linear.z = 0
			the_velocity.angular.x = 0
			the_velocity.angular.y = 0
			the_velocity.angular.z = 0
			self.the_publisher.publish(the_velocity)

			# now going for the last part of the initial
			the_velocity.linear.x = 0.6
			the_velocity.linear.y = 1
			the_velocity.linear.z = 0
			the_velocity.angular.x = 0
			the_velocity.angular.y = 0
			the_velocity.angular.z = 0

			init_time = rospy.Time.now().to_sec()
			curr_time = rospy.Time.now().to_sec()

			while (curr_time - init_time < 2):
				self.the_publisher.publish(the_velocity)
				curr_time = rospy.Time.now().to_sec()

			# stopping the bot
			the_velocity.linear.x = 0
			the_velocity.linear.y = 0
			self.the_publisher.publish(the_velocity)
			break


if __name__ == '__main__':
    try:
        #Testing our function
        ninja_turtle = initial_turtle()
        ninja_turtle.move()
    except rospy.ROSInterruptException: pass



