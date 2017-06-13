# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 12:14:56 2017

@author: Magnus Oksbøl Therkelsen
"""

def dataStatistics(data,statistic):
    """
    Statistical calculations on data imported with dataLoad function.
    
    Parameters
    ----------
    Input: 
        - Data as N x 3 array with
        - Statistic type as str.
       Types of statistic as str
           'Mean Temperature', 'Mean Growth Rate', 'Std Temperature', 
           'Std Growth rate', 'Rows', 'Mean Cold Growth rate' and 'Mean Hot Growth rate'
    Return
    ------
    Returns statistic result
    """
    #Mean Temperature
    result = None
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
    if statistic == 'Mean Cold Growth Rate':
        sort = np.array(data[:,0] < 20)
        mcgr = data[sort][:,1]
        if np.size(mcgr) == 0:
            print("No temperatures below 20 degrees in selected data.")
            result = "N/A"
        elif np.size(mcgr) > 0:
            result = np.mean(mcgr)
    #Mean growth rate above 50 degrees Celsius
    if statistic == 'Mean Hot Growth Rate':
        sort = np.array(data[:,0] > 50)
        mhgr = data[sort][:,1]
        if np.size(mhgr) == 0:
            print("No temperatures above 50 degrees in selected data.")
            result = "N/A"
        elif np.size(mhgr) > 0:
            result = np.mean(mhgr)
        
    
    if statistic == "Rows":
        print("There are {} rows in the selected data.".format(result))   
    elif result == "N/A":
        print("Cannot calculate {}. Please input valid data".format(statistic))
    else:
        print("The {} of the selcted data is {:f}".format(statistic,result))
    return result

# For test purposes
if __name__ == "__main__":
    datatest = dataLoad("test.txt")
    print("Statistics Test:")
    print(dataStatistics(datatest,"Rows"))
    print(dataStatistics(np.array([[20,0,0]),"Mean Cold Growth Rate"))


