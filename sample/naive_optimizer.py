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
    def objective(input_list, obj='tr'):
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
             'fun': lambda x: np.array([-x[0]+183])},
            {'type': 'ineq',
             'fun': lambda x: np.array([x[2] - x[1]])},
            {'type': 'ineq',
             'fun': lambda x: np.array([x[0] - x[2]])}
            )
        self.optimize_result = optimize.minimize(Optimizer.objective, list, args=(obj,), constraints=self.cons,
                                                 method='slsqp', options={'disp': False})
        self.final_point = MoveStrategy(self.optimize_result.x)

    def print_results(self):
        print("Days until lease end: {:.0f}".format(self.optimize_result.x[0])),
        print("Days until new lease: {:.0f}".format(self.optimize_result.x[1]))
        print("Days until move: {:.0f}".format(self.optimize_result.x[2]))
        print("Time Spent: {:.2f}".format(self.final_point.time))
        print("Money Spent: {:.2f}".format(self.final_point.money))
        print("Time/Money: {:.2f}".format(self.optimize_result.fun))


if __name__ == "__main__":
    input_initial = [183, 180, 180]
    a = Optimizer(input_initial, 'time')
    a.print_results()
