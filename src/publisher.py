#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Bool
from Tkinter import *
import time

global bl #variable boolean
def callback(data):
    	if(data==True):
	    pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
	    rate = rospy.Rate(15) # 15hz

	    message=PoseStamped()

	    print(message)

	    message.header.frame_id="map"


	    while not rospy.is_shutdown():
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

		print(message)
    	else:
		time.sleep(2)
	

def talker():
    
        #rospy.loginfo(hello_str)
        rospy.init_node('listener', anonymous=True)
 
	rospy.Subscriber("button_state", Bool, callback)
       
     # spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
    talker()
