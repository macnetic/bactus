# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 12:24:33 2017

@author: Magnus Oksbøl Therkelsen & Carl Emil Elling
"""

from displayMenu import displayMenu
from getFilename import getFilename
from dataLoad import dataLoad


# Menus options
options = (
        'Load data.','Filter data.','Display statistics.','Generate plots.',
        'Quit.'
        )

data = None

while True:
    sel = displayMenu(options)
    
    if sel == 1:
        # Load data
        fileIn = getFilename()
        data = dataLoad(fileIn)
    elif sel == 2:
        # Filter data
        pass
    elif sel == 3:
        # Compute statistic
        pass
    elif sel == 4:
        # Generate plots
        pass
    elif sel == 5:
        # Quit the program
        break