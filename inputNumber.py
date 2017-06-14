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
        Input from user
    """
    num = int(inputFloat(prompt))
    return num

def inputSet(prompt, sep=','):
    """
    Prompts the user for a set of numbers and returns them, 
    or None if user doesn't input a range.
    
    Parameters
    ----------
    prompt : str
        User prompt
    sep : str, optional
        Separator between numbers
    """
    while True:
        try:
            str_in = input(prompt)
            if str_in == '':
                # Indicates that no set has been selected.
                num_set = None
                break
            
            # Attempt to convert to tuple containing values
            num_set = tuple(float(num) for num in str_in.split(sep=sep))
            break
        except ValueError:
            print('Invalid input')
        
    return num_set

def inputRange(prompt,  sep=','):
    """
    Prompts the user for a numerical range and returns range, 
    or None if user doesn't input a range.
    
    Parameters
    ----------
    prompt : str
        User prompt
    sep : str, optional
        Separator between numbers
    """
    while True:
        f_range = inputSet(prompt, sep)
        # A range is two numbers, so raise an error if it's not
        if f_range == None:
            break
        elif len(f_range) != 2:
            print('Invalid range')
            continue
        
        break
        
    return f_range

def inputIntSet(prompt, sep=','):
    """
    Prompts the user for a set of integers and returns them, 
    or None if user doesn't input a range.
    
    Parameters
    ----------
    prompt : str
        User prompt
    sep : str, optional
        Separator between numbers
    """
    user_input = inputSet(prompt, sep)
    if user_input == None:
        return user_input
    else:
        int_set = tuple(int(e) for e in user_input)
        return int_set