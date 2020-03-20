#!/usr/bin/env python
# license removed for brevity

#importing dependencies messages and services
import sys
import rospy
from CR_week6_test.msg import perceived_info
from CR_week6_test.msg import robot_info
from CR_week6_test.srv import*

#initialising publisher
pub_4 = rospy.Publisher('Topic4', robot_info, queue_size=10)

msg4 = robot_info()
message = (0,0,0,0)

# callback which gets message values from topic 3, 
# to be sent to the service 
# gets the response from service 
# it then returns the request values and response from 
# the service and publishes the response to topic 4
def callback(msg):
    global message
    result = prediction_client()
    message = [msg.id,msg.object_size,msg.human_action,msg.human_expression]

    msg4.id = msg.id
    msg4.p_happy = result.p_happy
    msg4.p_neutral = result.p_neutral
    msg4.p_sad = result.p_sad

    pub_4.publish(msg4)

    return result, message

#this section does the following
#initialising publisher
#initialising the node
#subscribes to topic 3

def main():
    rospy.init_node('robot_controller', anonymous=True)
    pub_4 = rospy.Publisher('Topic4', robot_info, queue_size=10)
    rospy.Subscriber("Topic3", perceived_info, callback)
    rospy.spin()

#this section is for the client  
def prediction_client():
#blocks until the service is available
    rospy.wait_for_service('predictrobotexpression')
    try:
#creating a handle for the service and calling the handle
        predictrobotexpression = rospy.ServiceProxy('predictrobotexpression', predict_robot_expression)
        response = predictrobotexpression(message[0],message[1],message[2],message[3])
        return response

    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


if __name__ == "__main__":
    main()
    