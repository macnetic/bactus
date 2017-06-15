# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:49:45 2017

@author: Carl Emil Elling & Magnus Oksbøl Therkelsen
"""
import numpy as np
import matplotlib.pyplot as plt
def dataPlot(data):
    """
    DATAPLOT 
    
    
    Parameters
    ----------
    Data: 
        N x 3 array.
        
        Data input from dataLoad. Either filtered or unfiltered
    
    Prints
    ------
    Bar chart of number of different bacteria 
    Plot of growth rate by temperature
    
    Authors: Carl Emil Elling & Magnus Oksbøl Therkelsen
    """
#    Number of bacteria - bar chart
# Number of different bacteria is counted
    bacId = [1,2,3,4]
    bacNo = [0,0,0,0]
    for i in range(len(data[:,2])):
        for j in range(len(bacId)):
            if data[i,2] == bacId[j]:
                bacNo[j] = bacNo[j]+1
                     
    width = 0.35
    colors = ["green","red","blue","orange"]
    plot = plt.bar(bacId,bacNo,width,color=colors,alpha=0.7)
    plt.title("Number of bacteria in selected dataset")
    plt.xlabel("Bacteria type")
    plt.ylabel("Number of bacteria")
    plt.xticks(bacId, ('1', '2', '3', '4'))
    #Legend for the dataset
    plt.legend((plot[0],plot[1],plot[2],plot[3]), ('1. Salmonella enterica', '2. Bacillus cereus','3. Listeria','4. Brochothrix thermosphacta'),bbox_to_anchor=(1,1))
    # Filter criteria added as text
    test = [0,1,2]
    plt.figtext(0.2,-0.05,str(test))

    plt.show()
    
#    Growth rate by temperature
    #Data is sorted by temperature 
    sortedData = data[data[:,0].argsort()]
    #and by bacteria type
    bac1 = sortedData[sortedData[:,2] == 1]
    bac2 = sortedData[sortedData[:,2] == 2]
    bac3 = sortedData[sortedData[:,2] == 3]
    bac4 = sortedData[sortedData[:,2] == 4]
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    plt.title("Growth rate by temperature")
    plt.xlabel("Temperature in °C")
    plt.ylabel("Growth rate of bacteria")
    pl1 = ax1.plot(bac1[:,0],bac1[:,1],'-o',color="green",alpha=0.7,label='1. Salmonella enterica')
    pl2 = ax1.plot(bac2[:,0],bac2[:,1],'-o',color="red",alpha=0.7,label='2. Bacillus cereus')
    pl3 = ax1.plot(bac3[:,0],bac3[:,1],'-o',color="blue",alpha=0.7,label='3. Listeria')
    pl4 = ax1.plot(bac4[:,0],bac4[:,1],'-o',color="orange",alpha=0.7,label='4. Brochothrix thermosphacta')
    ax1.legend(bbox_to_anchor=(1,1))
    # Filter criteria added as text
    test = [0,1,2]
    plt.figtext(0.2,-0.05,str(test))
    plt.plot()

# For testing purposes
if __name__ == '__main__':
    dataPlot(dataLoad("test.txt"))