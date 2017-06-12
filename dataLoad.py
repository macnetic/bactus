# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 13:55:25 2017

@author: Magnus Oksbøl Therkelsen & Carl Emil Elling
"""
import pandas as pd
import numpy as np
def dataLoad(filename):
    """
    Imports a data file with entries separated with spaces as an array
    
    Parameters
    ----------
    Input: filename as str
    
    Return
    ------
    Returns data as N x 3 matrix
    """
    data = np.array(pd.read_csv(filename,sep=" "))
    dataErrorFree = np.zeros(3)
    dataErrors = np.array([])
    for i in range(len(data[:,0])):
        # Does temperature match delimiters? 
        temperatureInRange = 10 <= data[i,0] <= 60
        # Does growth rate match delimiters?
        growthInRange = 0 <= data[i,1]
        # Does bacteria type match delimiters?   
        bacteriaInRange = 1 <= data[i,2] <=4
        if (temperatureInRange and growthInRange and bacteriaInRange): 
            np.append(dataErrorFree,data[i,:],axis=0)
        print()
        
dataLoad("test.txt")