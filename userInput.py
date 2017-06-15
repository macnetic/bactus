# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 21:53:42 2017

@author: megam
"""
import os

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
            num_set = [float(num) for num in str_in.split(sep=sep)]
            break
        except ValueError:
            print('Invalid input')

    return num_set


def inputRange(prompt, sep=','):
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
        int_set = [int(e) for e in user_input]
        return int_set


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
        print()
        for i in range(len(options)):
            print("{:d}. {:s}".format(i + 1, options[i]))

        # Get a valid menu choice
        choice = inputInt(prompt)
        if choice in range(1, len(options) + 1):
            break

        print('Invalid menu selection')
    return choice


def getFilename():
    """
    Prompts the user for a file path, until user inputs valid file path.

    Return
    ------
    filename : str
        Path to file
    """

    while True:
        try:
            filename = os.path.abspath(input('Input file path: '))
            if os.path.isfile(filename): return filename
            raise IOError
        except IOError:
            print('Invalid filename')
