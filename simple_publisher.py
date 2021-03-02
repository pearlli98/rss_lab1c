#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Float32

def random_num_generator():
    pub = rospy.Publisher('my_random_float', Float32)
    rospy.init_node('simple_publisher', anonymous = True)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        random_num  = random.uniform(0, 10)
        rospy.loginfo(random_num)
        pub.publish(random_num)
        rate.sleep()

if __name__ == '__main__':
    try:
        random_num_generator()
    except rospy.ROSInterruptException:
        pass

