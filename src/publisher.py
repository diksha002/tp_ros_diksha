#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from geometry_msgs.msg import PoseStamped
 
def talker():
    pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
    rospy.init_node('talker', anonymous=False)
    rate = rospy.Rate(15) # 15hz

    message=PoseStamped()

    print(message)
    #message.pose.position.x=42
    #print(message)

    message.header.frame_id="map"
    while not rospy.is_shutdown():
	#theta=rospy.get_time()   #theta est maintenant dependant de temps
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
		message.pose.position.y=math.asin(-theta)
		pub.publish(message)
        	rate.sleep()
		theta = theta - 0.1

	print(message)
        #rospy.loginfo(hello_str)
        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

