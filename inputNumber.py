# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 21:53:42 2017

@author: megam
"""

def inputFloat(prompt):
    """
    Prompts the user to input a number and returns it as a float.
    Repeats until user inputs a valid number.
    
    Parameters
    ----------
    prompt : str
        User prompt
    
    Return
    ------
    num : float
        User input float
    """
    
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
        
    return num

def inputInt(prompt):
    """
    Prompts the user to input a number and returns it as an integer.
    Repeats until user inputs a valid number.
    
    Parameters
    ----------
    prompt : str
        User prompt
    
    Return
    ------
    num : int
        User input integer
    """
    return int(inputFloat(prompt))

def inputRange(prompt, sep=','):
    while True:
        try:
            str_in = input(prompt)
            if input == '':
                # TODO
                pass
            f_range = tuple(float(num) for num in input(prompt).split(sep=sep))
            break
        except ValueError:
            print('Invalid range')
        
    return f_range
