# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 12:24:33 2017

@author: Magnus Oksbøl Therkelsen & Carl Emil Elling
"""

from displayMenu import displayMenu
from getFilename import getFilename
from dataLoad import dataLoad


# Menus options
optionsMain = (
        'Load data.','Filter data.','Display statistics.','Generate plots.',
        'Quit.'
        )
optionsStat = (
        'Mean Temperature', 'Mean Growth Rate', 'Std Temperature', 
        'Std Growth rate', 'Rows', 'Mean Cold Growth rate', 'Mean Hot Growth rate'
        )
optionsFilter = (
        
        )
data = None
while True:
    sel = displayMenu(optionsMain)
    
    if sel == 1:
        # Load data
        fileIn = getFilename()
        data = dataLoad(fileIn)
    elif sel == 2:
        # Filter data
        pass
    elif sel == 3:
        # Compute statistic
        selStat = displayMenu(optionsStat)
        print(dataStatistics(selStat))
    elif sel == 4:
        # Generate plots
        pass
    elif sel == 5:
        # Quit the program
        break