    # -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:12:10 2017

@author: Magnus Oksbøl Therkelsen & Carl Emil Elling
"""

import numpy as np

from inputNumber import inputRange, inputIntSet
from displayMenu import displayMenu

bacteria = (
        'Salmonella enterica', 'Bacillus cereus', 'Listeria', 
        'Brochothrix thermosphacta'
        )

def getFilterParams():
    """
    Prompts user for filter parameters.
    
    Return
    ------
    temp_range : tuple
        Temperature range. returns None if user doesn't input range.
    growth_range : tuple
        Growth rate range. returns None if user doesn't input range.
    bac_type : tuple
        Bacteria types. returns None if no bacteria are selected.
    """
    
    print("Write values comma-separated, e.g. '10.0,60.0' or '1,2,3'.")
    print('Leave the field empty to reset filter.')
    temp_range = inputRange('Temperature range: ')
    growth_range = inputRange('Growth rate range: ')
    
    # Display options for bacteria filter
    for i in range(len(bacteria)):
        print('{:d}. {:s}'.format(i+1, bacteria[i]))
    bac_type = inputIntSet('Bacteria species: ')
    
    return temp_range, growth_range, bac_type

def filterData(data):
    """
    Filters data according user specified criteria
    
    Parameters
    ----------
    data : ndarray
        Input data array
    
    Return
    ------
    filtered_data : ndarray
        Array that only contains filtered data
    """
    
    
    
    return filtered_data