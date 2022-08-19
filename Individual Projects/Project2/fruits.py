#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:34:54 2020

@author: daniel
"""

from collections import defaultdict

# Reversing a dictionary 

fruit_to_color = {'banana':'yellow', \
                  'lemon':'yellow', \
                  'blueberry':'blue', \
                  'tomato': 'red',\
                  'strawberry':'red',\
                  'kiwi':'green'}
    
color_to_fruit = {
        'yellow': ['banana', 'lemon'],
        'blue': ['blueberry'],
        'red': ['tomato', 'strawberry'],
        'green': ['kiwi']}
                   
                   
def flip_dict(input_dict):  

    output_dict = {}    

    for key in input_dict: 
        
        val = input_dict[key]
        
        if not val in output_dict: 
            output_dict[val] = []
        
        output_dict[val].append(key)

    return output_dict


                   
def flip_dict2(input_dict):  

    output_dict = defaultdict(list) 

    for key in input_dict: 
        
        val = input_dict[key]
        
        output_dict[val].append(key)

    return output_dict



color_to_fruit = flip_dict2(fruit_to_color)
print(color_to_fruit)
                   