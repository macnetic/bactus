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
    # Text file is loaded as a CSV file with spaces as separators
    data = np.array(pd.read_csv(filename,sep=" "))
    dataErrorFree = np.zeros(3)
    dataErrorTemperature = np.zeros(3)
    dataErrorTemperatureNo = np.array([])
    dataErrorGrowth = np.zeros(3)
    dataErrorGrowthNo = np.array([])
    dataErrorBacteria = np.zeros(3)
    dataErrorBacteriaNo = []
    for i in range(len(data[:,0])):
        # Does temperature match delimiters? 
        temperatureInRange = 10 <= data[i,0] <= 60
        # Does growth rate match delimiters?
        growthInRange = 0 <= data[i,1]
        # Does bacteria type match delimiters?   
        bacteriaInRange = 1 <= data[i,2] <= 4
        if (temperatureInRange and growthInRange and bacteriaInRange): 
            dataErrorFree = np.vstack((dataErrorFree, data[i,:]))
        if temperatureInRange == False:
            dataErrorTemperature = np.vstack((dataErrorTemperature,data[i,:]))
            # Row index of error values are found. 2 is added, since row numbers start at 0, and 
            # because of the initial 1x3 array with zeros
            dataErrorTemperatureNo = np.append(dataErrorTemperatureNo,str(i+2))
        if growthInRange == False:
            dataErrorGrowth = np.vstack((dataErrorGrowth,data[i,:]))
            dataErrorGrowthNo = np.append(dataErrorGrowthNo,str(i+2))
        if bacteriaInRange == False:
            dataErrorBacteria = np.vstack((dataErrorBacteria,data[i,:]))
            dataErrorBacteriaNo = np.append(dataErrorBacteriaNo,str(i+2))
    # initial [0,0,0] array removed
    data = dataErrorFree[1:]
    if np.size(dataErrorTemperatureNo) > 0:
        dataErrorTemperatureNo = ", ".join(dataErrorTemperatureNo)
        print("Temperature error in line(s): {}. Temperature needs to be between 10 and 60 degrees celsius. Line(s) have been removed from dataset.".format(dataErrorTemperatureNo))
    if np.size(dataErrorGrowthNo) > 0:
        dataErrorGrowthNo = ", ".join(dataErrorGrowthNo)
        print("Growth rate error in line(s): {}. Growth rate needs to be a positive number. Line(s) have been removed from dataset.".format(dataErrorGrowthNo))
    if np.size(dataErrorBacteriaNo) > 0:
        dataErrorBacteriaNo = ", ".join(dataErrorBacteriaNo)
        print("Error in bacteria type in line(s): {}. Line(s) have been removed from dataset. Type needs to be a positive integer from 1 to 4 where:".format(dataErrorBacteriaNo))
        print("1 = Salmonella enterica. 2 = Bacillus cereus. 3 = Listeria. 4 = Brochothrix thermosphacta.")
    return data
    
    
#For test purposes
if __name__ == '__main__':    
    print(dataLoad("test.txt"))
    datatest = dataLoad("test.txt")
    print("Data Test")
    print(datatest)
    