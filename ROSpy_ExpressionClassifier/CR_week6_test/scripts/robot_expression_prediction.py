#!/usr/bin/env python
# license removed for brevity

#importing dependencies messages and services
import rospy
from bayesian.bbn import build_bbn
from bayesian.utils import make_key
from CR_week6_test.srv import predict_robot_expression, predict_robot_expressionResponse

a = 0
b = 0
c = 0
#Filling out propabiblities and for bayesian belief network 
def f_human_expression(human_expression):
    if human_expression == '1':
        return 1.0 / 3.0
    elif human_expression == '2':
        return 1.0 / 3.0
    elif human_expression == '3':
        return 1.0 / 3.0

def f_human_action(human_action):
    if human_action == '1':
        return 1.0 / 3.0
    elif human_action == '2':
        return 1.0 / 3.0
    elif human_action == '3':
        return 1.0 / 3.0

def f_object_size(object_size):
    if object_size == '1':
        return 0.5
    elif object_size == '2':
        return 0.5

def f_robot_expression(human_expression, human_action, object_size, robot_expression):
    
    table = dict()
    table['111h'] = 0.8
    table['112h'] = 1.0
    table['121h'] = 0.8
    table['122h'] = 1.0
    table['131h'] = 0.6
    table['132h'] = 0.8
    table['211h'] = 0.0
    table['212h'] = 0.0
    table['221h'] = 0.0
    table['222h'] = 0.1
    table['231h'] = 0.0
    table['232h'] = 0.2
    table['311h'] = 0.7
    table['312h'] = 0.8
    table['321h'] = 0.8
    table['322h'] = 0.9
    table['331h'] = 0.6
    table['332h'] = 0.7
    table['111s'] = 0.2
    table['112s'] = 0.0
    table['121s'] = 0.2
    table['122s'] = 0.0
    table['131s'] = 0.2
    table['132s'] = 0.2
    table['211s'] = 0.0
    table['212s'] = 0.0
    table['221s'] = 0.1
    table['222s'] = 0.1
    table['231s'] = 0.2
    table['232s'] = 0.2
    table['311s'] = 0.3
    table['312s'] = 0.2
    table['321s'] = 0.2
    table['322s'] = 0.1
    table['331s'] = 0.2
    table['332s'] = 0.2
    table['111n'] = 0.0
    table['112n'] = 0.0
    table['121n'] = 0.0
    table['122n'] = 0.0
    table['131n'] = 0.2
    table['132n'] = 0.0
    table['211n'] = 1.0
    table['212n'] = 1.0
    table['221n'] = 0.9
    table['222n'] = 0.8
    table['231n'] = 0.8
    table['232n'] = 0.6
    table['311n'] = 0.0
    table['312n'] = 0.0
    table['321n'] = 0.0
    table['322n'] = 0.0
    table['331n'] = 0.2
    table['332n'] = 0.1  

    return table[make_key(human_expression, human_action, object_size, robot_expression)] 

# function to get the probability of each robot expression from network calculation
# with if statements to prevent function from calling query with wrong arguments
# if statements allow the prediction to be made even if value of argument is 0
def handle_server(req):

    if req.human_expression == 0 and req.human_action == 0 and req.object_size == 0:
        a = g.query().get(('robot_expression', 'h'))
        b = g.query().get(('robot_expression', 'n'))
        c = g.query().get(('robot_expression', 's'))

    elif req.human_expression == 0 and req.human_action == 0:
        a = g.query(object_size=str(req.object_size)).get(('robot_expression', 'h'))
        b = g.query(object_size=str(req.object_size)).get(('robot_expression', 'n'))
        c = g.query(object_size=str(req.object_size)).get(('robot_expression', 's'))

    elif req.human_expression == 0 and req.object_size == 0:
        a = g.query(human_action=str(req.human_action)).get(('robot_expression', 'h'))
        b = g.query(human_action=str(req.human_action)).get(('robot_expression', 'n'))
        c = g.query(human_action=str(req.human_action)).get(('robot_expression', 's'))

    elif req.human_action == 0 and req.object_size == 0:
        a = g.query(human_expression=str(req.human_expression)).get(('robot_expression', 'h'))
        b = g.query(human_expression=str(req.human_expression)).get(('robot_expression', 'n'))
        c = g.query(human_expression=str(req.human_expression)).get(('robot_expression', 's'))

    elif req.human_expression == 0:
        a = g.query(human_action=str(req.human_action), object_size=str(req.object_size)).get(('robot_expression', 'h'))
        b = g.query(human_action=str(req.human_action), object_size=str(req.object_size)).get(('robot_expression', 'n'))
        c = g.query(human_action=str(req.human_action), object_size=str(req.object_size)).get(('robot_expression', 's'))

    elif req.human_action == 0:
        a = g.query(human_expression=str(req.human_expression), object_size=str(req.object_size)).get(('robot_expression', 'h'))
        b = g.query(human_expression=str(req.human_expression), object_size=str(req.object_size)).get(('robot_expression', 'n'))
        c = g.query(human_expression=str(req.human_expression), object_size=str(req.object_size)).get(('robot_expression', 's'))

    elif req.object_size == 0:
        a = g.query(human_action=str(req.human_action), human_expression=str(req.human_expression)).get(('robot_expression', 'h'))
        b = g.query(human_action=str(req.human_action), human_expression=str(req.human_expression)).get(('robot_expression', 'n'))
        c = g.query(human_action=str(req.human_action), human_expression=str(req.human_expression)).get(('robot_expression', 's'))

    else:
        a = g.query(object_size=str(req.object_size), human_action=str(req.human_action), human_expression=str(req.human_expression)).get(('robot_expression', 'h'))
        b = g.query(object_size=str(req.object_size), human_action=str(req.human_action), human_expression=str(req.human_expression)).get(('robot_expression', 'n'))
        c = g.query(object_size=str(req.object_size), human_action=str(req.human_action), human_expression=str(req.human_expression)).get(('robot_expression', 's'))
    return predict_robot_expressionResponse(a,b,c)
#section for service
# node is initialised
# service is declared    
def main_server():
    rospy.init_node('robot_expression_prediction')
    s = rospy.Service('predictrobotexpression', predict_robot_expression, handle_server)
    rospy.spin()

if __name__ == '__main__':
    g = build_bbn(
        f_human_expression, f_human_action,  f_object_size, f_robot_expression, 
        domains=dict(
            human_expression=['1', '2', '3'],
            human_action=['1', '2', '3'],
            object_size=['1', '2'],
            robot_expression=['h', 's', 'n']))
    main_server()
