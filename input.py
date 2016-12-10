# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 14:00:52 2016

@author: Collin
"""
import numpy as np

class Input:
    def __init__(self, list): 
        self.EL= list[0]
        self.SL = list[1]
        self.moving_time = list[2]
        self.AR = 45
        self.nparray=np.array([self.EL, self.SL, self.moving_time])
        self.const_max_rent=1600
        self.const_new_rent = 825