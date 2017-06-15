# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 12:24:33 2017

@author: Magnus Oksbøl Therkelsen & Carl Emil Elling
"""

import userInput
from dataLoad import dataLoad
import filterData
from dataStatistic import *
from dataPlot import *


# Menus options
optionsMain = (
        'Load data.','Filter data.','Display statistics.','Generate plots.',
        'Quit.'
        )
optionsStat = (
        'Mean Temperature', 'Mean Growth Rate', 'Std Temperature', 
        'Std Growth rate', 'Rows', 'Mean Cold Growth rate', 'Mean Hot Growth rate', 'Back to Main Menu'
        )
optionsFilter = ('Temperature range', 'Growth rate range', 'Bacteria species', 'Reset all filters','Back to Main Menu')
data = np.array([])
f_params = [None, None, None]
f_data = np.array([])

while True:
    sel = userInput.displayMenu(optionsMain)
    
    if sel == 1:
        # Load data
        fileIn = userInput.getFilename()
        data = dataLoad(fileIn)
        # Reset filter and filter data
        f_params = [None, None, None]
        f_data = filterData.filterData(data, f_params)
    elif sel == 2:
        # Filter data
        choice = userInput.displayMenu(optionsFilter, prompt='Please choose a filter: ')
        if choice == 4:
                f_params = [None, None, None]
        elif choice == 5:
            continue
        else:
            f_params[choice-1] = filterData.getFilterParam(choice)

        f_data = filterData.filterData(data, f_params)
    elif sel == 3:
        # Compute statistics
        print("Filter(s) applied: {}")
        selStat = userInput.displayMenu(optionsStat)
        dataStatistics(data,optionsStat[selStat-1])
    elif sel == 4:
        # Generate plots
        dataPlot(data)
        pass
    elif sel == 5:
        # Quit the program
        break

