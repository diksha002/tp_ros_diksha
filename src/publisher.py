#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Bool
from Tkinter import *


global bl #variable boolean
def callback(data):
	#bl=data.data
	while(data.data==True):
		pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
		rate = rospy.Rate(15) # 15hz

		message=PoseStamped()

		message.header.frame_id="map"

		r=10
		theta=0
	
		while theta <= 2*(math.pi):
			message.pose.position.x=theta
			message.pose.position.y=math.sin(theta)
			pub.publish(message)
			rate.sleep()
			theta = theta + 0.1


		while theta >= 0:
			message.pose.position.x=theta
			message.pose.position.y=math.sin(-theta)
			pub.publish(message)
			rate.sleep()
			theta = theta - 0.1

	    #print(message)
	

def talker():
    
        rospy.init_node('listen', anonymous=True)
 
	rospy.Subscriber("button_state", Bool, callback)
       
	rospy.spin()

if __name__ == '__main__':
    talker()
