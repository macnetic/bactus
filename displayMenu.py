# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 22:01:50 2017

@author: megam
"""

from inputNumber import inputInt


def displayMenu(options, prompt=None):
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
    
    # Default prompt
    if prompt == None: 
        prompt = 'Please choose a menu item: '
    
    while True:
        # Display menu options
        for i in range(len(options)):
            print("\n{:d}. {:s}".format(i+1, options[i]))
            
        # Get a valid menu choice
        choice = inputInt(prompt)
        if choice in range(1, len(options)+1): break
        print('Invalid menu selection')
            
            
    return choice

# Test om det virker
if __name__ == '__main__':
    displayMenu(['Hej','Med','Dig'])