# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 14:00:52 2016

@author: Collin
"""
import numpy as np


class MoveStrategy:
    def __init__(self, list): 
        self.EL= list[0]
        self.SL = list[1]
        self.moving_time = list[2]
        self.AR = 45
        self.nparray=np.array([self.EL, self.SL, self.moving_time])
        self.const_max_rent=1600
        self.const_new_rent = 825
        self.objective_function = self.time_ratio
        self.find_time_spent()
        self.find_money_lost()
        self.calculate_objective_value()

    def find_money_lost(self):
        self.money = (self.EL*self.const_max_rent +
        self.AR*self.const_max_rent*.85 +
        self.const_new_rent * self.SL)
        return self.money

    @staticmethod
    def calculate_commute(move_date):
        days = 183 - move_date
        time_per_day = (20 * 7 + 25 + 25) / 7
        time = days * time_per_day
        return time
        # TODO make this reflect actual weekdays

        # TODO make commute times a probability distribution

    def find_time_spent(self):
        self.time = self.moving_time - self.calculate_commute(self.moving_time)
        return self.time

    def calculate_objective_value(self):
        self.objective_value = self.objective_function(self.time, self.money)
        return self.objective_value

    @staticmethod
    def time_ratio(time, money):
        # Minimize time spent/money saved
        objective = time / money
        return objective