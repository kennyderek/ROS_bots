#!/usr/bin/env python

import rospy
from jetbrains_task.msg import Positions

def callback(data):
    '''
    function for handling messages read from topic,
    prints x, y, and z coordinates of each Bot to console
    '''
    print '********'

    # message data is read one bot at a time, for every bot created
    for i in range(0, data.numbots):

        # prints to console and logs x, y, z coordinates for a bot to the node
        rospy.loginfo("Bot " + str(i + 1) + " at (x, y, z) coordinates: " + str((data.x_pos[i], data.y_pos[i], data.z_pos[i])))

def observer():

    # initialize the observer node
    rospy.init_node('observer', anonymous=True)

    # Subscribes to the pos_topic topic and feeds Positions.msg to callback function
    rospy.Subscriber('pos_topic', Positions, callback)

    # keeps python from exiting until node is stopped
    rospy.spin()

if __name__ == '__main__':
    observer()

