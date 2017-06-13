# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 22:01:50 2017

@author: megam
"""

import numpy as np
from inputNumber import inputNumber

def displayMenu(options):
    """
    DISPLAYMENU Displays a menu of options, ask the user to choose an item
    and returns the number of the menu item chosen.
    
    Usage
    -----
    choice = displayMenu(options)
    
    Parameters
    ----------
    options : string array
        Menu options (array of strings)
    
    Return
    ------
    choice : int
        Chosen option (integer)
    
    Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    """
    
    while True:
        # Display menu options
        for i in range(len(options)):
            print("{:d}. {:s}".format(i+1, options[i]))
            
        # Get a valid menu choice
        try:
            choice = inputNumber("Please choose a menu item: ")
            if choice in range(1, len(options)+1): break
            raise ValueError
        except ValueError:
            print('Invalid menu selection')
            
            
    return choice

if __name__ == '__main__':
    displayMenu(['Hej','Med','Dig'])