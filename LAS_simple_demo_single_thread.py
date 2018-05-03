#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 14:34:37 2018

@author: jack.lingheng.meng
"""
import time
from math import *
from vreppy import VRep
import numpy as np
import random
import gym
from gym import spaces
import pdb

class LivingArchitectureEnv(gym.Env):
    def __init__(self):
        # connect vrep server
        print("Connecting vrep server...")
        
        self.vrep = VRep.connect("127.0.0.1", 19997)
        # initialize vrep objects
        print("Initialize vrep objects...")
        # actuators: sma 
        self.sma1_node0 = self.vrep.joint.with_position_control("sma1_node#0")
        self.sma2_node0 = self.vrep.joint.with_position_control("sma2_node#0")
        self.sma3_node0 = self.vrep.joint.with_position_control("sma3_node#0")

        self.sma1_node1 = self.vrep.joint.with_position_control("sma1_node#1")
        self.sma2_node1 = self.vrep.joint.with_position_control("sma2_node#1")
        self.sma3_node1 = self.vrep.joint.with_position_control("sma3_node#1")

        self.sma1_node2 = self.vrep.joint.with_position_control("sma1_node#2")
        self.sma2_node2 = self.vrep.joint.with_position_control("sma2_node#2")
        self.sma3_node2 = self.vrep.joint.with_position_control("sma3_node#2")

        self.sma1_node3 = self.vrep.joint.with_position_control("sma1_node#3")
        self.sma2_node3 = self.vrep.joint.with_position_control("sma2_node#3")
        self.sma3_node3 = self.vrep.joint.with_position_control("sma3_node#3")

        self.sma1_node4 = self.vrep.joint.with_position_control("sma1_node#4")
        self.sma2_node4 = self.vrep.joint.with_position_control("sma2_node#4")
        self.sma3_node4 = self.vrep.joint.with_position_control("sma3_node#4")

        self.sma1_node5 = self.vrep.joint.with_position_control("sma1_node#5")
        self.sma2_node5 = self.vrep.joint.with_position_control("sma2_node#5")
        self.sma3_node5 = self.vrep.joint.with_position_control("sma3_node#5")

        self.sma1_node6 = self.vrep.joint.with_position_control("sma1_node#6")
        self.sma2_node6 = self.vrep.joint.with_position_control("sma2_node#6")
        self.sma3_node6 = self.vrep.joint.with_position_control("sma3_node#6")

        self.sma1_node7 = self.vrep.joint.with_position_control("sma1_node#7")
        self.sma2_node7 = self.vrep.joint.with_position_control("sma2_node#7")
        self.sma3_node7 = self.vrep.joint.with_position_control("sma3_node#7")

        self.sma1_node8 = self.vrep.joint.with_position_control("sma1_node#8")
        self.sma2_node8 = self.vrep.joint.with_position_control("sma2_node#8")
        self.sma3_node8 = self.vrep.joint.with_position_control("sma3_node#8")

        self.sma1_node9 = self.vrep.joint.with_position_control("sma1_node#9")
        self.sma2_node9 = self.vrep.joint.with_position_control("sma2_node#9")
        self.sma3_node9 = self.vrep.joint.with_position_control("sma3_node#9")

        self.sma1_node10 = self.vrep.joint.with_position_control("sma1_node#10")
        self.sma2_node10 = self.vrep.joint.with_position_control("sma2_node#10")
        self.sma3_node10 = self.vrep.joint.with_position_control("sma3_node#10")

        self.sma1_node11 = self.vrep.joint.with_position_control("sma1_node#11")
        self.sma2_node11 = self.vrep.joint.with_position_control("sma2_node#11")
        self.sma3_node11 = self.vrep.joint.with_position_control("sma3_node#11")

        self.sma1_node12 = self.vrep.joint.with_position_control("sma1_node#12")
        self.sma2_node12 = self.vrep.joint.with_position_control("sma2_node#12")
        self.sma3_node12 = self.vrep.joint.with_position_control("sma3_node#12")
                                                                
        # actuators & sensors: lights
        self.omnidirect_light1_node0 = self.vrep.light.omnidirectional("omnidirect_light1_node#0")
        self.omnidirect_light2_node0 = self.vrep.light.omnidirectional("omnidirect_light2_node#0")
        self.omnidirect_light3_node0 = self.vrep.light.omnidirectional("omnidirect_light3_node#0")

        self.omnidirect_light1_node1 = self.vrep.light.omnidirectional("omnidirect_light1_node#1")
        self.omnidirect_light2_node1 = self.vrep.light.omnidirectional("omnidirect_light2_node#1")
        self.omnidirect_light3_node1 = self.vrep.light.omnidirectional("omnidirect_light3_node#1")

        self.omnidirect_light1_node2 = self.vrep.light.omnidirectional("omnidirect_light1_node#2")
        self.omnidirect_light2_node2 = self.vrep.light.omnidirectional("omnidirect_light2_node#2")
        self.omnidirect_light3_node2 = self.vrep.light.omnidirectional("omnidirect_light3_node#2")

        self.omnidirect_light1_node3 = self.vrep.light.omnidirectional("omnidirect_light1_node#3")
        self.omnidirect_light2_node3 = self.vrep.light.omnidirectional("omnidirect_light2_node#3")
        self.omnidirect_light3_node3 = self.vrep.light.omnidirectional("omnidirect_light3_node#3")

        self.omnidirect_light1_node4 = self.vrep.light.omnidirectional("omnidirect_light1_node#4")
        self.omnidirect_light2_node4 = self.vrep.light.omnidirectional("omnidirect_light2_node#4")
        self.omnidirect_light3_node4 = self.vrep.light.omnidirectional("omnidirect_light3_node#4")

        self.omnidirect_light1_node5 = self.vrep.light.omnidirectional("omnidirect_light1_node#5")
        self.omnidirect_light2_node5 = self.vrep.light.omnidirectional("omnidirect_light2_node#5")
        self.omnidirect_light3_node5 = self.vrep.light.omnidirectional("omnidirect_light3_node#5")

        self.omnidirect_light1_node6 = self.vrep.light.omnidirectional("omnidirect_light1_node#6")
        self.omnidirect_light2_node6 = self.vrep.light.omnidirectional("omnidirect_light2_node#6")
        self.omnidirect_light3_node6 = self.vrep.light.omnidirectional("omnidirect_light3_node#6")

        self.omnidirect_light1_node7 = self.vrep.light.omnidirectional("omnidirect_light1_node#7")
        self.omnidirect_light2_node7 = self.vrep.light.omnidirectional("omnidirect_light2_node#7")
        self.omnidirect_light3_node7 = self.vrep.light.omnidirectional("omnidirect_light3_node#7")

        self.omnidirect_light1_node8 = self.vrep.light.omnidirectional("omnidirect_light1_node#8")
        self.omnidirect_light2_node8 = self.vrep.light.omnidirectional("omnidirect_light2_node#8")
        self.omnidirect_light3_node8 = self.vrep.light.omnidirectional("omnidirect_light3_node#8")

        self.omnidirect_light1_node9 = self.vrep.light.omnidirectional("omnidirect_light1_node#9")
        self.omnidirect_light2_node9 = self.vrep.light.omnidirectional("omnidirect_light2_node#9")
        self.omnidirect_light3_node9 = self.vrep.light.omnidirectional("omnidirect_light3_node#9")

        self.omnidirect_light1_node10 = self.vrep.light.omnidirectional("omnidirect_light1_node#10")
        self.omnidirect_light2_node10 = self.vrep.light.omnidirectional("omnidirect_light2_node#10")
        self.omnidirect_light3_node10 = self.vrep.light.omnidirectional("omnidirect_light3_node#10")

        self.omnidirect_light1_node11 = self.vrep.light.omnidirectional("omnidirect_light1_node#11")
        self.omnidirect_light2_node11 = self.vrep.light.omnidirectional("omnidirect_light2_node#11")
        self.omnidirect_light3_node11 = self.vrep.light.omnidirectional("omnidirect_light3_node#11")
                                                                        
        self.omnidirect_light1_node12 = self.vrep.light.omnidirectional("omnidirect_light1_node#12")
        self.omnidirect_light2_node12 = self.vrep.light.omnidirectional("omnidirect_light2_node#12")
        self.omnidirect_light3_node12 = self.vrep.light.omnidirectional("omnidirect_light3_node#12")
        
        # sensors: proximity sensors
        self.ir_1_node0 = self.vrep.sensor.proximity("ir_1_node#0")
        self.ir_2_node0 = self.vrep.sensor.proximity("ir_2_node#0")
        self.ir_3_node0 = self.vrep.sensor.proximity("ir_3_node#0")
                                                     
        self.ir_1_node1 = self.vrep.sensor.proximity("ir_1_node#1")
        self.ir_2_node1 = self.vrep.sensor.proximity("ir_2_node#1")
        self.ir_3_node1 = self.vrep.sensor.proximity("ir_3_node#1")

        self.ir_1_node2 = self.vrep.sensor.proximity("ir_1_node#2")
        self.ir_2_node2 = self.vrep.sensor.proximity("ir_2_node#2")
        self.ir_3_node2 = self.vrep.sensor.proximity("ir_3_node#2")

        self.ir_1_node3 = self.vrep.sensor.proximity("ir_1_node#3")
        self.ir_2_node3 = self.vrep.sensor.proximity("ir_2_node#3")
        self.ir_3_node3 = self.vrep.sensor.proximity("ir_3_node#3")
                                                     
        self.ir_1_node4 = self.vrep.sensor.proximity("ir_1_node#4")
        self.ir_2_node4 = self.vrep.sensor.proximity("ir_2_node#4")
        self.ir_3_node4 = self.vrep.sensor.proximity("ir_3_node#4")
                                                     
        self.ir_1_node5 = self.vrep.sensor.proximity("ir_1_node#5")
        self.ir_2_node5 = self.vrep.sensor.proximity("ir_2_node#5")
        self.ir_3_node5 = self.vrep.sensor.proximity("ir_3_node#5")

        self.ir_1_node6 = self.vrep.sensor.proximity("ir_1_node#6")
        self.ir_2_node6 = self.vrep.sensor.proximity("ir_2_node#6")
        self.ir_3_node6 = self.vrep.sensor.proximity("ir_3_node#6")

        self.ir_1_node7 = self.vrep.sensor.proximity("ir_1_node#7")
        self.ir_2_node7 = self.vrep.sensor.proximity("ir_2_node#7")
        self.ir_3_node7 = self.vrep.sensor.proximity("ir_3_node#7")

        self.ir_1_node8 = self.vrep.sensor.proximity("ir_1_node#8")
        self.ir_2_node8 = self.vrep.sensor.proximity("ir_2_node#8")
        self.ir_3_node8 = self.vrep.sensor.proximity("ir_3_node#8")
                                                     
        self.ir_1_node9 = self.vrep.sensor.proximity("ir_1_node#9")
        self.ir_2_node9 = self.vrep.sensor.proximity("ir_2_node#9")
        self.ir_3_node9 = self.vrep.sensor.proximity("ir_3_node#9")

        self.ir_1_node10 = self.vrep.sensor.proximity("ir_1_node#10")
        self.ir_2_node10 = self.vrep.sensor.proximity("ir_2_node#10")
        self.ir_3_node10 = self.vrep.sensor.proximity("ir_3_node#10")

        self.ir_1_node11 = self.vrep.sensor.proximity("ir_1_node#11")
        self.ir_2_node11 = self.vrep.sensor.proximity("ir_2_node#11")
        self.ir_3_node11 = self.vrep.sensor.proximity("ir_3_node#11")
                                                      
        self.ir_1_node12 = self.vrep.sensor.proximity("ir_1_node#12")
        self.ir_2_node12 = self.vrep.sensor.proximity("ir_2_node#12")
        self.ir_3_node12 = self.vrep.sensor.proximity("ir_3_node#12")
        
        # initialize action and observation space
        print("Initialize action and observation space...")
        self.prox_sensor_num = 3 * 13# (3 prox ) * 13 nodes
        self.smas_num = 3 * 13       # (3 smas ) * 13 nodes
        self.lights_num = 3 * 13     # (3 lights ) * 13 nodes
        self.sensors_dim = 6 * 13    # (3 prox + 3 lights) * 13 nodes
        self.actuators_dim = 6 * 13  # (3 smas + 3 lights) * 13 nodes
        
        self.obs_max = np.array([np.inf]*self.actuators_dim)
        self.obs_min = - np.array([np.inf]*self.actuators_dim)
        self.act_max = np.array([1.]*self.sensors_dim)
        self.act_min = - np.array([1.]*self.sensors_dim)
        
        self.observation_space = spaces.Box(self.obs_min, self.obs_max)
        self.action_space = spaces.Box(self.act_min, self.act_max)
        print("Initialization done!")
        
        self.reward = 0
        
    def _self_observe(self):
        # read prox sensor
        ir_1_node0_state, ir_1_node0_position = self.ir_1_node0.read()
        ir_2_node0_state, ir_2_node0_position = self.ir_2_node0.read()
        ir_3_node0_state, ir_3_node0_position = self.ir_3_node0.read()
        
        ir_1_node1_state, ir_1_node1_position = self.ir_1_node1.read()
        ir_2_node1_state, ir_2_node1_position = self.ir_2_node1.read()
        ir_3_node1_state, ir_3_node1_position = self.ir_3_node1.read()
        
        ir_1_node2_state, ir_1_node2_position = self.ir_1_node2.read()
        ir_2_node2_state, ir_2_node2_position = self.ir_2_node2.read()
        ir_3_node2_state, ir_3_node2_position = self.ir_3_node2.read()
        
        ir_1_node3_state, ir_1_node3_position = self.ir_1_node3.read()
        ir_2_node3_state, ir_2_node3_position = self.ir_2_node3.read()
        ir_3_node3_state, ir_3_node3_position = self.ir_3_node3.read()
        
        ir_1_node4_state, ir_1_node4_position = self.ir_1_node4.read()
        ir_2_node4_state, ir_2_node4_position = self.ir_2_node4.read()
        ir_3_node4_state, ir_3_node4_position = self.ir_3_node4.read()
        
        ir_1_node5_state, ir_1_node5_position = self.ir_1_node5.read()
        ir_2_node5_state, ir_2_node5_position = self.ir_2_node5.read()
        ir_3_node5_state, ir_3_node5_position = self.ir_3_node5.read()
        
        ir_1_node6_state, ir_1_node6_position = self.ir_1_node6.read()
        ir_2_node6_state, ir_2_node6_position = self.ir_2_node6.read()
        ir_3_node6_state, ir_3_node6_position = self.ir_3_node6.read()
        
        ir_1_node7_state, ir_1_node7_position = self.ir_1_node7.read()
        ir_2_node7_state, ir_2_node7_position = self.ir_2_node7.read()
        ir_3_node7_state, ir_3_node7_position = self.ir_3_node7.read()
        
        ir_1_node8_state, ir_1_node8_position = self.ir_1_node8.read()
        ir_2_node8_state, ir_2_node8_position = self.ir_2_node8.read()
        ir_3_node8_state, ir_3_node8_position = self.ir_3_node8.read()
        
        ir_1_node9_state, ir_1_node9_position = self.ir_1_node9.read()
        ir_2_node9_state, ir_2_node9_position = self.ir_2_node9.read()
        ir_3_node9_state, ir_3_node9_position = self.ir_3_node9.read()
        
        ir_1_node10_state, ir_1_node10_position = self.ir_1_node10.read()
        ir_2_node10_state, ir_2_node10_position = self.ir_2_node10.read()
        ir_3_node10_state, ir_3_node10_position = self.ir_3_node10.read()
        
        ir_1_node11_state, ir_1_node11_position = self.ir_1_node11.read()
        ir_2_node11_state, ir_2_node11_position = self.ir_2_node11.read()
        ir_3_node11_state, ir_3_node11_position = self.ir_3_node11.read()
        
        ir_1_node12_state, ir_1_node12_position = self.ir_1_node12.read()
        ir_2_node12_state, ir_2_node12_position = self.ir_2_node12.read()
        ir_3_node12_state, ir_3_node12_position = self.ir_3_node12.read()
        
        # read lights state
        omnidirect_light1_node0_state, diffsePart, specularPart = self.omnidirect_light1_node0.get_light_state_and_color()
        omnidirect_light2_node0_state, diffsePart, specularPart = self.omnidirect_light2_node0.get_light_state_and_color()
        omnidirect_light3_node0_state, diffsePart, specularPart = self.omnidirect_light3_node0.get_light_state_and_color()
        
        omnidirect_light1_node1_state, diffsePart, specularPart = self.omnidirect_light1_node1.get_light_state_and_color()
        omnidirect_light2_node1_state, diffsePart, specularPart = self.omnidirect_light2_node1.get_light_state_and_color()
        omnidirect_light3_node1_state, diffsePart, specularPart = self.omnidirect_light3_node1.get_light_state_and_color()
        
        omnidirect_light1_node2_state, diffsePart, specularPart = self.omnidirect_light1_node2.get_light_state_and_color()
        omnidirect_light2_node2_state, diffsePart, specularPart = self.omnidirect_light2_node2.get_light_state_and_color()
        omnidirect_light3_node2_state, diffsePart, specularPart = self.omnidirect_light3_node2.get_light_state_and_color()
        
        omnidirect_light1_node3_state, diffsePart, specularPart = self.omnidirect_light1_node3.get_light_state_and_color()
        omnidirect_light2_node3_state, diffsePart, specularPart = self.omnidirect_light2_node3.get_light_state_and_color()
        omnidirect_light3_node3_state, diffsePart, specularPart = self.omnidirect_light3_node3.get_light_state_and_color()
        
        omnidirect_light1_node4_state, diffsePart, specularPart = self.omnidirect_light1_node4.get_light_state_and_color()
        omnidirect_light2_node4_state, diffsePart, specularPart = self.omnidirect_light2_node4.get_light_state_and_color()
        omnidirect_light3_node4_state, diffsePart, specularPart = self.omnidirect_light3_node4.get_light_state_and_color()
        
        omnidirect_light1_node5_state, diffsePart, specularPart = self.omnidirect_light1_node5.get_light_state_and_color()
        omnidirect_light2_node5_state, diffsePart, specularPart = self.omnidirect_light2_node5.get_light_state_and_color()
        omnidirect_light3_node5_state, diffsePart, specularPart = self.omnidirect_light3_node5.get_light_state_and_color()
        
        omnidirect_light1_node6_state, diffsePart, specularPart = self.omnidirect_light1_node6.get_light_state_and_color()
        omnidirect_light2_node6_state, diffsePart, specularPart = self.omnidirect_light2_node6.get_light_state_and_color()
        omnidirect_light3_node6_state, diffsePart, specularPart = self.omnidirect_light3_node6.get_light_state_and_color()
        
        omnidirect_light1_node7_state, diffsePart, specularPart = self.omnidirect_light1_node7.get_light_state_and_color()
        omnidirect_light2_node7_state, diffsePart, specularPart = self.omnidirect_light2_node7.get_light_state_and_color()
        omnidirect_light3_node7_state, diffsePart, specularPart = self.omnidirect_light3_node7.get_light_state_and_color()
        
        omnidirect_light1_node8_state, diffsePart, specularPart = self.omnidirect_light1_node8.get_light_state_and_color()
        omnidirect_light2_node8_state, diffsePart, specularPart = self.omnidirect_light2_node8.get_light_state_and_color()
        omnidirect_light3_node8_state, diffsePart, specularPart = self.omnidirect_light3_node8.get_light_state_and_color()
        
        omnidirect_light1_node9_state, diffsePart, specularPart = self.omnidirect_light1_node9.get_light_state_and_color()
        omnidirect_light2_node9_state, diffsePart, specularPart = self.omnidirect_light2_node9.get_light_state_and_color()
        omnidirect_light3_node9_state, diffsePart, specularPart = self.omnidirect_light3_node9.get_light_state_and_color()
        
        omnidirect_light1_node10_state, diffsePart, specularPart = self.omnidirect_light1_node10.get_light_state_and_color()
        omnidirect_light2_node10_state, diffsePart, specularPart = self.omnidirect_light2_node10.get_light_state_and_color()
        omnidirect_light3_node10_state, diffsePart, specularPart = self.omnidirect_light3_node10.get_light_state_and_color()
        
        omnidirect_light1_node11_state, diffsePart, specularPart = self.omnidirect_light1_node11.get_light_state_and_color()
        omnidirect_light2_node11_state, diffsePart, specularPart = self.omnidirect_light2_node11.get_light_state_and_color()
        omnidirect_light3_node11_state, diffsePart, specularPart = self.omnidirect_light3_node11.get_light_state_and_color()
        
        omnidirect_light1_node12_state, diffsePart, specularPart = self.omnidirect_light1_node12.get_light_state_and_color()
        omnidirect_light2_node12_state, diffsePart, specularPart = self.omnidirect_light2_node12.get_light_state_and_color()
        omnidirect_light3_node12_state, diffsePart, specularPart = self.omnidirect_light3_node12.get_light_state_and_color()
        
        self.observation = np.array([ir_1_node0_state, ir_2_node0_state, ir_3_node0_state,
                                     ir_1_node1_state, ir_2_node1_state, ir_3_node1_state,
                                     ir_1_node2_state, ir_2_node2_state, ir_3_node2_state,
                                     ir_1_node3_state, ir_2_node3_state, ir_3_node3_state,
                                     ir_1_node4_state, ir_2_node4_state, ir_3_node4_state,
                                     ir_1_node5_state, ir_2_node5_state, ir_3_node5_state,
                                     ir_1_node6_state, ir_2_node6_state, ir_3_node6_state,
                                     ir_1_node7_state, ir_2_node7_state, ir_3_node7_state,
                                     ir_1_node8_state, ir_2_node8_state, ir_3_node8_state,
                                     ir_1_node9_state, ir_2_node9_state, ir_3_node9_state,
                                     ir_1_node10_state, ir_2_node10_state, ir_3_node10_state,
                                     ir_1_node11_state, ir_2_node11_state, ir_3_node11_state,
                                     ir_1_node12_state, ir_2_node12_state, ir_3_node12_state,
                                     omnidirect_light1_node0_state, omnidirect_light2_node0_state, omnidirect_light3_node0_state,
                                     omnidirect_light1_node1_state, omnidirect_light2_node1_state, omnidirect_light3_node1_state,
                                     omnidirect_light1_node2_state, omnidirect_light2_node2_state, omnidirect_light3_node2_state,
                                     omnidirect_light1_node3_state, omnidirect_light2_node3_state, omnidirect_light3_node3_state,
                                     omnidirect_light1_node4_state, omnidirect_light2_node4_state, omnidirect_light3_node4_state,
                                     omnidirect_light1_node5_state, omnidirect_light2_node5_state, omnidirect_light3_node5_state,
                                     omnidirect_light1_node6_state, omnidirect_light2_node6_state, omnidirect_light3_node6_state,
                                     omnidirect_light1_node7_state, omnidirect_light2_node7_state, omnidirect_light3_node7_state,
                                     omnidirect_light1_node8_state, omnidirect_light2_node8_state, omnidirect_light3_node8_state,
                                     omnidirect_light1_node9_state, omnidirect_light2_node9_state, omnidirect_light3_node9_state,
                                     omnidirect_light1_node10_state, omnidirect_light2_node10_state, omnidirect_light3_node10_state,
                                     omnidirect_light1_node11_state, omnidirect_light2_node11_state, omnidirect_light3_node11_state,
                                     omnidirect_light1_node12_state, omnidirect_light2_node12_state, omnidirect_light3_node12_state])
        return self.observation    
    
    def step(self, actions):
        # actions: 
        #   sma: 0-2
        #   lights: 3-5
        
        actions = np.clip(actions, self.act_min, self.act_max)
        
        action_smas = actions[:self.smas_num]
        action_lights = actions[self.smas_num:]
        action_lights = action_lights.astype(int)
        # move sma
        self.sma1_node0.set_target_position(action_smas[0])
        self.sma2_node0.set_target_position(action_smas[1])
        self.sma3_node0.set_target_position(action_smas[2])
        
        self.sma1_node1.set_target_position(action_smas[3])
        self.sma2_node1.set_target_position(action_smas[4])
        self.sma3_node1.set_target_position(action_smas[5])
        
        self.sma1_node2.set_target_position(action_smas[6])
        self.sma2_node2.set_target_position(action_smas[7])
        self.sma3_node2.set_target_position(action_smas[8])
        
        self.sma1_node3.set_target_position(action_smas[9])
        self.sma2_node3.set_target_position(action_smas[10])
        self.sma3_node3.set_target_position(action_smas[11])
        
        self.sma1_node4.set_target_position(action_smas[12])
        self.sma2_node4.set_target_position(action_smas[13])
        self.sma3_node4.set_target_position(action_smas[14])
        
        self.sma1_node5.set_target_position(action_smas[15])
        self.sma2_node5.set_target_position(action_smas[16])
        self.sma3_node5.set_target_position(action_smas[17])
        
        self.sma1_node6.set_target_position(action_smas[18])
        self.sma2_node6.set_target_position(action_smas[19])
        self.sma3_node6.set_target_position(action_smas[20])
        
        self.sma1_node7.set_target_position(action_smas[21])
        self.sma2_node7.set_target_position(action_smas[22])
        self.sma3_node7.set_target_position(action_smas[23])

        self.sma1_node8.set_target_position(action_smas[24])
        self.sma2_node8.set_target_position(action_smas[25])
        self.sma3_node8.set_target_position(action_smas[26])
        
        self.sma1_node9.set_target_position(action_smas[27])
        self.sma2_node9.set_target_position(action_smas[28])
        self.sma3_node9.set_target_position(action_smas[29])
        
        self.sma1_node10.set_target_position(action_smas[30])
        self.sma2_node10.set_target_position(action_smas[31])
        self.sma3_node10.set_target_position(action_smas[32])
        
        self.sma1_node11.set_target_position(action_smas[33])
        self.sma2_node11.set_target_position(action_smas[34])
        self.sma3_node11.set_target_position(action_smas[35])
        
        self.sma1_node12.set_target_position(action_smas[36])
        self.sma2_node12.set_target_position(action_smas[37])
        self.sma3_node12.set_target_position(action_smas[38])
        
        # change light state
        
        self.omnidirect_light1_node0.set_light_state(action_lights[0])
        self.omnidirect_light2_node0.set_light_state(action_lights[1])
        self.omnidirect_light3_node0.set_light_state(action_lights[2])
        
        self.omnidirect_light1_node1.set_light_state(action_lights[3])
        self.omnidirect_light2_node1.set_light_state(action_lights[4])
        self.omnidirect_light3_node1.set_light_state(action_lights[5])
        
        self.omnidirect_light1_node2.set_light_state(action_lights[6])
        self.omnidirect_light2_node2.set_light_state(action_lights[7])
        self.omnidirect_light3_node2.set_light_state(action_lights[8])
        
        self.omnidirect_light1_node3.set_light_state(action_lights[9])
        self.omnidirect_light2_node3.set_light_state(action_lights[10])
        self.omnidirect_light3_node3.set_light_state(action_lights[11])
        
        self.omnidirect_light1_node4.set_light_state(action_lights[12])
        self.omnidirect_light2_node4.set_light_state(action_lights[13])
        self.omnidirect_light3_node4.set_light_state(action_lights[14])
        
        self.omnidirect_light1_node5.set_light_state(action_lights[15])
        self.omnidirect_light2_node5.set_light_state(action_lights[16])
        self.omnidirect_light3_node5.set_light_state(action_lights[17])
        
        self.omnidirect_light1_node6.set_light_state(action_lights[18])
        self.omnidirect_light2_node6.set_light_state(action_lights[19])
        self.omnidirect_light3_node6.set_light_state(action_lights[20])
        
        self.omnidirect_light1_node7.set_light_state(action_lights[21])
        self.omnidirect_light2_node7.set_light_state(action_lights[22])
        self.omnidirect_light3_node7.set_light_state(action_lights[23])
        
        self.omnidirect_light1_node8.set_light_state(action_lights[24])
        self.omnidirect_light2_node8.set_light_state(action_lights[25])
        self.omnidirect_light3_node8.set_light_state(action_lights[26])
        
        self.omnidirect_light1_node9.set_light_state(action_lights[27])
        self.omnidirect_light2_node9.set_light_state(action_lights[28])
        self.omnidirect_light3_node9.set_light_state(action_lights[29])
        
        self.omnidirect_light1_node10.set_light_state(action_lights[30])
        self.omnidirect_light2_node10.set_light_state(action_lights[31])
        self.omnidirect_light3_node10.set_light_state(action_lights[32])
        
        self.omnidirect_light1_node11.set_light_state(action_lights[33])
        self.omnidirect_light2_node11.set_light_state(action_lights[34])
        self.omnidirect_light3_node11.set_light_state(action_lights[35])
        
        self.omnidirect_light1_node12.set_light_state(action_lights[36])
        self.omnidirect_light2_node12.set_light_state(action_lights[37])
        self.omnidirect_light3_node12.set_light_state(action_lights[38])
        
        # observe new state
        self._self_observe()
        # reward
        self._reward()
        
        return self.observation, self.reward, False, {}
    
    def _reward(self):

        self.reward = np.mean(self.observation[:self.prox_sensor_num])
        return self.reward
    
    def reset(self):
        self.vrep.simulation.stop()
        self.vrep.simulation.start()
        self._self_observe()
        return self.observation
    
    def destroy(self):
        self.vrep.close_connection()
    
if __name__ == '__main__':
    env = LivingArchitectureEnv()
    env.reset()
    # trival agent   
    i = 1 
    while True:
        # random actions
        smas = np.random.randn(39)
        lights = np.random.randint(2,size = 39)
        action = np.array([smas, lights])
        action = action.flatten()
        
        observation, reward, done, info = env.step(action)
        print("Step: {}, reward: {}".format(i, reward))
        i = i+1
        #time.sleep(0.1)
    
    env.destroy()
