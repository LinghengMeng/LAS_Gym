#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 16:07:35 2018

@author: jack.lingheng.meng

"""

"""
This is an overall framework of non-distributed simultion environment.
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
    
"""
This is an overall design of agent
"""
class Agent():
    def __init__(self):
        """
        initialize
        """
        # Hyperparameters
        
        # Variables about single experience
        self._observationOld = []   # observation at time t
        self._observationNew = []   # observation at time t+1
        self._actionOld = []        # action at time t
        self._actionNew = []        # action at time t+1
        # Memory
        self._memory = []            # hard memory storing every experience
        # Components in an agent
        #   Component: actor-critic model i.e. policy and value function
        self._actorModel = self._create_actor_model()
        self._criticModel = self._create_critic_modle()
        #   Component: environment model
        self._environmentModel = self._create_environment_model()
        #   Component: intrinsic motivation model
        self._intrinsicMotivationModel = self._create_intrinsic_motivation_model()
        
    # ========================================================================= #
    #                       Components or Models Definitions                      #
    # ========================================================================= #    
    def _create_actor_model(self):
        """
        Create actor model:
            action = actorModel.predict(observation)
        """
        
    def _create_critic_model(self):
        """
        Create critic model:
            QValue = criticModel.predict(observation, action)
        """
        
    def _create_environment_model(self):
        """
        Create environment model:
            obervationNew, reward = environmentModel.predict(observatin, action)
        """
        
    def _create_intrinsic_motivation_model(self):
        """
        Create intrinsic motivation model:
            intrinsicMotivationModel.predict()
        """
        
    # ========================================================================= #
    #                      perceive and remember experiences                    #
    # ========================================================================= #        
    def perceive(self, observation, reward, done = False, info = []):
        """
        Perceive observation and reward from environment after an interaction
        Input: observation, reward, done, info
        """
        self._observationNew = observation
        self._reward = reward
        self._done = done
        self._remember(self._observationOld, self._actionOld, self._observation_new, self._reward)
        
    def _remember(self, observationOld, action_Old, observationNew, reward):
        """
        Store (observationOld, action_Old, observationNew, reward)
        """
        self._memory.append([observationOld, action_Old, observationNew, reward])
        #self._
    # ========================================================================= #
    #                               Train Agent                                 #
    # ========================================================================= #        
    def _train(self):
        """
        Train agent
        """
        samples = random.sample(self._memory, batch_size)   # prepare batch
        # train actor-critic
        self._train_critic(samples)
        self._train_actor(samples)
        # train environment model
        self._train_environment_model(samples)
        
    def _train_critic(self, samples):
        """
        Train critic
        """
        
    def _train_actor(self, samples):
        """
        Train actor
        """
        
    def _train_environment_model(self, samples):
        """
        Train environment model
        """
    def _train_intrinsic_motivation_model(self, samples):
        """
        Train intrinsic motivation model
        """
    # ========================================================================= #
    #                              Decide New Action                            #
    # ========================================================================= #        
    def act(self):
        