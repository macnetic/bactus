# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 12:14:56 2017

@author: Magnus Oksbøl Therkelsen
"""

def dataStatistics(data,statistic):
    #Mean Temperature
    if statistic == 'Mean Temperature':
        result = np.mean(data[:,0])
    #Mean Growth rate
    if statistic == 'Mean Growth Rate':
        result = np.mean(data[:,1])
    #Standard deviation of temperature
    if statistic == 'Std Temperature':
        result = np.std(data[:,0])
    #Standard deviation of growth rate
    if statistic == 'Std Growth rate':
        result = np.std(data[:,1])
    #Total number of rows in data
    if statistic == 'Rows':
        result = np.size(data[:,0])
    #Mean growth rate below 20 degrees Celsius
    if statistic == 'Mean Cold Growth rate':
        mcgr = np.array([])
        for i in range(len(data[:,0])):
            if data[i,0] < 20:
                mcgr = np.append(data[i],mcgr)
        result = np.mean(mcgr)
    #Mean growth rate above 50 degrees Celsius
    if statistic == 'Mean Hot Growth rate':
        mhgr = np.array([])
        for i in range(len(data[:,1])):
            if data[i,1] < 20:
                mhgr = np.append(data[i,1],mhgr)
        result = np.mean(mhgr)    
        
    return(result)