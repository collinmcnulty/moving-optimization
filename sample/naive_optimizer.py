# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 10:54:30 2016

@author: Collin
"""

import numpy as np
import scipy.optimize as optimize
from sample.input_def import MoveStrategy


class Optimizer:
    @staticmethod
    def objective(input_list):
        point = MoveStrategy(input_list)
        return point.objective_value

    def __init__(self, list, obj='tr'):
        self.initial_point = MoveStrategy(list, obj)
        self.cons = (
            {'type': 'ineq',
             'fun': lambda x: np.array([x[0] - x[1]]),
             },
            {'type': 'ineq',
             'fun': lambda x: np.array([x[0] - 60])},
            {'type': 'ineq',
             'fun': lambda x: np.array([x[1]])},
            {'type': 'ineq',
             'fun': lambda x: np.array([x[2]])},

            {'type': 'ineq',
             'fun': lambda x: np.array([x[1] - x[2]])}
            )
        self.optimize_result = optimize.minimize(Optimizer.objective, list, constraints=self.cons,
                                                 method='cobyla', options={'disp': False})
        self.final_point = MoveStrategy(self.optimize_result.x)

    def print_results(self):
        print("Days until lease end: {}".format(self.optimize_result.x[0])),
        print("Days until new lease: {}".format(self.optimize_result.x[1]))
        print("Days until new lease: {}".format(self.optimize_result.x[2]))
        print("Time Spent: {}".format(self.final_point.time))
        print("Money Spent: {}".format(self.final_point.money))
        print("Time/Money: {}".format(self.optimize_result.fun))


if __name__ == "__main__":
    input_initial = [80, 60, 70]
    a = Optimizer(input_initial)
    a.print_results()
