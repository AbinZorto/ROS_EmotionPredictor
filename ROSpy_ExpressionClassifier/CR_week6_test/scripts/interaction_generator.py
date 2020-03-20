#!/usr/bin/env python
# license removed for brevity

#importing dependencies and messages
import rospy
import random
from CR_week6_test.msg import object_info
from CR_week6_test.msg import human_info

#assigning variable to message
msg1 = object_info()
msg2 = human_info()
msg1.id = 0
msg2.id = 0

#function to generate data for every interaction
def generator(msg1_, msg2_):
#id for every interaction
    msg1_.id = msg1_.id + 1
    msg2_.id = msg2_.id + 1
#random value for every interaction
    msg1_.object_size = random.randint(1,2)
    msg2_.human_expression = random.randint(1,3)
    msg2_.human_action = random.randint(1,3)


#this section does the following
#initialising publisher for both messages to two different topics
#initialising the node
# setting the interactions to occur once every 10 seconds    
# while continuing to generate interactions and publish 
# the messages until node is shutdown

def main():
    pub_1 = rospy.Publisher('Topic1', object_info, queue_size=10)
    pub_2 = rospy.Publisher('Topic2', human_info, queue_size=10)
    rospy.init_node('interaction_generator', anonymous=True)
    rate = rospy.Rate(0.1)
    while not rospy.is_shutdown():
        generator(msg1,msg2)
        pub_1.publish(msg1)
        pub_2.publish(msg2)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass