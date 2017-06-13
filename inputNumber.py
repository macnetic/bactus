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
    # INPUTNUMBER Prompts user to input a number
    #
    # Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
    # number. Repeats until user inputs a valid number.
    #
    # Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
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
