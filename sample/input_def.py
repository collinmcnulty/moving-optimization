# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 14:00:52 2016

@author: Collin
"""
import numpy as np


class MoveStrategy:
    def __init__(self, list, obj='tr'):
        self.EL = list[0]
        self.SL = list[1]
        self.moving_time = list[2]
        self.AR = 45
        self.nparray = np.array([self.EL, self.SL, self.moving_time])
        self.const_max_rent = 1600 / 30
        self.const_new_rent = 825 / 30
        self.const_normal_rent = 1325 / 30
        if obj == 'tr':
            self.objective_function = self.time_ratio
        elif obj == 'time':
            self.objective_function = self.time_ratio
        self.find_time_spent()
        self.find_money_lost()
        self.calculate_objective_value()

    def find_money_lost(self):
        days_abandoned = 183. - self.EL
        whole_days_abandoned = int(days_abandoned - (days_abandoned % 1))
        dec1penalty = (1600 - 1325) * 182 / 365 + 1325
        money = 0
        for i in range(whole_days_abandoned + 1):
            if i == whole_days_abandoned:
                last_day = (days_abandoned % 1)**2 * (
                i / 183 * dec1penalty + ((1 - i) / 183) * 1325) / 30  # Makes function continuous
                money += last_day
            else:
                money += (i / 183 * dec1penalty + ((1 - i) / 183) * 1325) / 30
        new_rent = self.const_new_rent * (183 - self.SL)
        self.money = new_rent + money
        return self.money

    @staticmethod
    def calculate_commute(move_date):
        days_in_new_crib = 183 - move_date
        whole_days_in_new_crib = int(days_in_new_crib - days_in_new_crib % 1)
        time = 0
        for i in range(whole_days_in_new_crib + 1):
            if i == whole_days_in_new_crib:
                mod = days_in_new_crib - whole_days_in_new_crib
            else:
                mod = 1
            weekday = i % 7
            if weekday in [0, 1, 5, 6]:  # Thursday, Fri, Tues, Wed
                time -= 20 * mod
            elif weekday in [2, 3]:
                time -= 25 * mod
            else:
                time += 25 * mod
        return time

        # TODO make commute times a probability distribution

    def find_time_spent(self):
        self.time = self.calculate_commute(self.moving_time)
        return self.time

    def calculate_objective_value(self):
        self.objective_value = self.objective_function()
        return self.objective_value

    def time_ratio(self):
        # Minimize time spent/money saved
        if self.money > 1:
            self.time_ratio_val = self.time / self.money
        else:
            self.time_ratio_val = -100
        return self.time_ratio_val

    def print_results(self):
        print("Days until lease end: {:.0f}".format(self.EL)),
        print("Days until new lease: {:.0f}".format(self.SL))
        print("Days until move: {:.0f}".format(self.moving_time))
        print("Time Spent: {:.2f}".format(self.time))
        print("Money Spent: {:.2f}".format(self.money))
        print("Time/Money: {:.2f}".format(self.time_ratio_val))


if __name__ == "__main__":
    input_initial = [183, 182, 182]
    a = MoveStrategy(input_initial)
    a.print_results()
