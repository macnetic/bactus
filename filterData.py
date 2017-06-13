# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:12:10 2017

@author: Magnus Oksbøl Therkelsen & Carl Emil Elling
"""

import numpy as np


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
    
    temp_range = float(input('Temperature: <lower upper>: ').split(sep = ' '))
    growth_range = float(input('Growth: <lower upper>: ').split(sep = ' '))
    bac_dict = {
            'Salmonella enterica':1, 'Bacillus cereus':2, 'Listeria':3, 
            'Brochothrix thermosphacta':4 
            }
    
    
    return filtered_data