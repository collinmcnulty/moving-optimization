# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 14:00:52 2016

@author: Collin
"""
import numpy as np


class MoveStrategy:
    def __init__(self, list, obj='tr'):
        self.EL= list[0]
        self.SL = list[1]
        self.moving_time = list[2]
        self.AR = 45
        self.nparray=np.array([self.EL, self.SL, self.moving_time])
        self.const_max_rent=1600/30
        self.const_new_rent = 825/30
        if obj == 'tr':
            self.objective_function = self.time_ratio
        elif obj == 'time':
            self.objective_function = self.find_time_spent
        self.find_time_spent()
        self.find_money_lost()
        self.calculate_objective_value()

    def find_money_lost(self):
        self.money = (self.EL*self.const_max_rent +
        self.AR*self.const_max_rent*.85 +
        self.const_new_rent * (183-self.SL)) -8082.5
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
        self.time =  -self.calculate_commute(self.moving_time)
        return self.time

    def calculate_objective_value(self):
        self.objective_value = self.objective_function()
        return self.objective_value


    def time_ratio(self):
        # Minimize time spent/money saved
         objective = self.time / self.money
         return objective

    def print_results(self):
        print("Days until lease end: {:.0f}".format(self.EL)),
        print("Days until new lease: {:.0f}".format(self.SL))
        print("Days until move: {:.0f}".format(self.moving_time))
        print("Time Spent: {:.2f}".format(self.time))
        print("Money Spent: {:.2f}".format(self.money))
        print("Time/Money: {:.2f}".format(self.time/self.money))

if __name__ == "__main__":
    input_initial = [60, 60, 60]
    a = MoveStrategy(input_initial)
    a.print_results()