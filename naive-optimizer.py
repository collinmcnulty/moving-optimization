# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 10:54:30 2016

@author: Collin
"""

import scipy.optimize as optimize
import numpy as np
import pandas as pd
from input_def import Input 

def calculate_commute(move_date):
    days = 183 - move_date
    time_per_day = (20 * 7 + 25 + 25)/7
    time = days * time_per_day
    return time
    #TODO make this reflect actual weekdays
    
    #TODO make commute times a probability distribution
    
def check_input_obj_type(input):
    if not isinstance(input, Input):
        input = convert_input_to_obj(input) 
    return input

def find_money_lost(input):
    input = check_input_obj_type(input)
    money = (input.EL*input.const_max_rent + 
    input.AR*input.const_max_rent*.85 +  
    input.const_new_rent * input.SL)
    
    return money
            
def find_time_spent(input):
    input = check_input_obj_type(input)
    time = input.moving_time - calculate_commute(input.moving_time)
    return time
    
def calculate_objective(input):
    # Minimize time spent/money saved    
    input = convert_input_to_obj(input)
    time_spent = find_time_spent(input)
    money_lost = find_money_lost(input)
    objective = time_spent/money_lost
    return objective
    
def convert_input_to_obj(input_array):
    return Input(input_array)



def print_results(res):
    print(res.x)
    print(find_money_lost(res.x))
    print(find_time_spent(res.x))


if __name__=="__main__":
    input_initial = Input([80, 60, 70])
    cons = ({'type':'ineq',
             'fun' : lambda x: np.array([x[0]-x[1]]),
             },
             {'type' : 'ineq',
              'fun' : lambda x: np.array([x[0]-60])},
               {'type' : 'ineq',
              'fun' : lambda x: np.array([x[1]])},
            {'type' : 'ineq',
              'fun' : lambda x: np.array([x[2]])},
            
            {'type' : 'ineq',
              'fun' : lambda x: np.array([x[1]-x[2]])}
            )
    res = optimize.minimize(calculate_objective, input_initial.nparray, constraints=cons,
               method = 'cobyla', options = {'disp':True})       
    print_results(res)
    
    def test_point(list):
        print(find_money_lost(list))