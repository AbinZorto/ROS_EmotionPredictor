#!/usr/bin/env python
# license removed for brevity

#importing dependencies and messages
import rospy
import random
from CR_week6_test.msg import object_info
from CR_week6_test.msg import human_info
from CR_week6_test.msg import perceived_info

#initialising publisher
pub_3 = rospy.Publisher('Topic3', perceived_info, queue_size=10)

rando = 0
msg3 = perceived_info()

# callback for first topic which generates a random number and 
# assigns value to object_size depending on random number
def callback(msg):
    rando = random.randint(1,8)
    if rando == 1:
        msg.object_size = 0
    if rando == 4:
        msg.object_size = 0
    if rando == 5:
        msg.object_size = 0
    if rando == 7:
        msg.object_size = 0
    msg3.id = msg.id
    msg3.object_size = msg.object_size

# callback for second topic which generates a random number and 
# assigns value to object_size depending on random number 
# and publishing the message on every callback
def callback1(msg1):
    rando = random.randint(1,8)
    if rando == 2:
        msg1.human_action = 0
    if rando == 3:
        msg1.human_expression = 0
    if rando == 4:
        msg1.human_action = 0
    if rando == 5:
        msg1.human_expression = 0
    if rando == 6:
        msg1.human_action = 0
        msg1.human_expression = 0
    if rando == 7:
        msg1.human_action = 0
        msg1.human_expression = 0

    msg3.human_action = msg1.human_action
    msg3.human_expression = msg1.human_expression
    pub_3.publish(msg3)


def listener():
#initialising node 
    rospy.init_node('perception_filter', anonymous=True)
#publishing perceived info message to topic 3
    pub_3 = rospy.Publisher('Topic3', perceived_info, queue_size=10)

#Subscribing to both topic 1 and topic 2
    rospy.Subscriber("Topic1", object_info, callback)
    rospy.Subscriber("Topic2", human_info, callback1)

    rospy.spin()

if __name__ == '__main__':
    listener()