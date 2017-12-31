#!/usr/bin/env python

import rospy
from ROS_bots.msg import Positions

import math
import random

def runner():
    '''
    main function that updates bots positions
    '''

    # initialize the runner node
    rospy.init_node('runner', anonymous=True)

    # initialize the program's clock, to be used for position calculations
    init_time = rospy.Time.now()

    # gets the number of desired bots passed in as a terminal argument, if none, default to 1
    numbots = rospy.get_param('~numbots', 1)
    print 'creating', numbots, 'bots'
    # for desired num of bots, create a new bot instance
    all_bots = []
    for _ in range(0, numbots):
        all_bots.append(Bot())


    mypub = rospy.Publisher('pos_topic', Positions, queue_size=10)
    rate = rospy.Rate(2) # set to 2 Hz
    print 'Publishing locations'

    # as long as Ctrl-C not pressed
    while not rospy.is_shutdown():
        # calculate and print time elapsed
        time_elapsed = (rospy.Time.now() - init_time)
        time_elapsed = time_elapsed.to_sec()
        rospy.loginfo('time elapsed: ' + str(time_elapsed))

        # creates a x y and z position list, where the ith element of each list
        # corresponds to the respective list variable for the ith desired bot
        x_positions = []
        y_positions = []
        z_positions = []

        # update positions for every bot
        for bot in all_bots:
            x_positions.append(bot.return_cur_x(time_elapsed))
            y_positions.append(bot.return_cur_y(time_elapsed))
            z_positions.append(bot.return_cur_z(time_elapsed))

        # put positions into msg
        msg = Positions()
        msg.numbots = numbots
        msg.x_pos = x_positions
        msg.y_pos = y_positions
        msg.z_pos = z_positions

        mypub.publish(msg)

        rate.sleep()


class Bot():
    '''
    keeps track of the functions that dictate a singular bot's movement
    '''

    def __init__(self):

        # the different possible functions for bot location, as a function of time
        trajectories = [math.sin, math.cos, lambda t: t**2, lambda t: t]

        # select a random function to describe x, y, z positions 
        self.x_function = trajectories[random.randint(0,2)]
        self.y_function = trajectories[random.randint(0,2)]
        self.z_function = trajectories[random.randint(0,2)]

    def return_cur_x(self, global_clock):
        # returns float of x position as a funciton of time
        return float(self.x_function(global_clock))

    def return_cur_y(self, global_clock):    
        # returns float of y position as a funciton of time
        return float(self.y_function(global_clock))

    def return_cur_z(self, global_clock): 
        # returns float of z position as a funciton of time
        return float(self.z_function(global_clock))



if __name__ == '__main__':
    try:
        runner()

    except rospy.ROSInterruptException:
        pass