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

def getFilterParam(choice):
    """
    Prompts user for filter parameters.

    Parameters
    ----------
    choice : int
        Result from displayMenu()

    Return
    ------
    returns one of these values:

    temp_range : array
        Temperature range. returns None if user doesn't input range.
    growth_range : array
        Growth rate range. returns None if user doesn't input range.
    bac_type : array
        Bacteria types. returns None if no bacteria are selected.
    """

    if choice == 1:
        print("Write range comma-separated, e.g. '10.0,60.0'.")
        print('Leave the field empty to reset filter.')
        temp_range = inputRange('Temperature range: ')
        return temp_range
    elif choice == 2:
        print("Write range comma-separated, e.g. '10.0,60.0'.")
        print('Leave the field empty to reset filter.')
        growth_range = inputRange('Growth rate range: ')
        return growth_range
    elif choice == 3:
        # Display options for bacteria filter
        print("Write values comma-separated, e.g. '1,2,4'.")
        print('Leave the field empty to reset filter.')
        for i in range(len(bacteria)):
            print('{:d}. {:s}'.format(i+1, bacteria[i]))
        bac_type = inputIntSet('Bacteria species: ')
        return bac_type

def filterData(data, filter_params):
    """
    Filters data according user specified criteria
    
    Parameters
    ----------
    data : ndarray
        Input data array
    filter_params : array
        Filter parameters. First and second elements are temperature and
        growth rate ranges as tuples, third element is a tuple for 
        bacteria species.
    
    Return
    ------
    filtered_data : ndarray
        Array that only contains filtered data
    """
    
    # Unpack filter parameters
    tr, gr, bt = filter_params

    # Create a masked array
    m_data = np.ma.masked_array(data)

    # If user reset filter we set the mask for that column to False
    # For ranges, mask everything out of range
    # For bacteria type, check if it should be filtered
    if tr == None:
        m_data[:,0].mask = False
    else:
        m_data[:,0] = np.ma.masked_outside(m_data[:,0], *tr)

    if gr == None:
        m_data[:,1].mask = False
    else:
        m_data[:,1] = np.ma.masked_outside(m_data[:,1], *gr)

    if bt == None:
        m_data[:,2].mask = False
    else:
        m_data[:,2] = np.ma.masked_where(~np.in1d(m_data[:,2], bt), m_data[:,2])

    #Invert and combine
    filter = ~m_data[:,0].mask & ~m_data[:,1].mask & ~m_data[:,2].mask

    # Apply filter
    f_data = data[filter,:]

    return f_data