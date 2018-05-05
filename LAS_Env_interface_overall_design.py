#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 16:07:35 2018

@author: jack.lingheng.meng

This is a overall framework of non-distributed simultion environment.

"""

class LivingArchitectureEnv():
    def __init__(self):
        """
        initialize
        """
        self._actionMode = []
        self._observation = []
        self._reward = []
        
    def step(self, action):
        """
        Take one step of interaction
        Input: action
        Output: observation, reward, done, info
        """
        # Take action
        if self.actionMode == raw:
            self._action_raw(action)
        elif self.actionMode == primitive:
            self._action_primitive(action)
        elif self.actionMode == prescribed:
            self._action_priscribed()
        else:
            ValueError("Wrong action mode.")
        
        # Get new observation and reward
        self._observation = self._self_observe()
        self._reward = self._reward(self._observation)
        
        return observation, rewward, done, info
         
    def _action_priscribed(self):
        """
        Take prescribed actions based on current observation. This action mode
        does not need to receive action from an agent.
        Input: current observation
        """
        if self.observationOld == case1:
            prescribed_action1
        elif self.observation == case2:
            prescribed_action2
        elif self.observation == case3:
            prescribed_action3  
        elif self.observation == case4:
            prescribed_action4
        else:
            prescribed_action_others
        
    def _action_primitive(self, action):
        """
        Take primitive action
        Input: primitive action
        """
        
    def _action_raw(self, action):
        """
        Take action by directly control each actuator 
        Input: action values
        """
        
    def _self_observe(self):
        """
        Get sensory data
        """
        
    def _reward(self, observation):
        """
        Calculate reward based on current observation
        Input: current observation
        Output: reward
        """
        
        return self.reward
    
    def reset(self):
        """
        Reset to the start of simulation
        """
        start_simulation()
        self._observation = self._self_observe()
        return self._observation