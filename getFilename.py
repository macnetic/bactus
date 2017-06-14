# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:13:32 2017

@author: Carl Emil Elling, Magnus Oksbøl Therkelsen
"""

import os

def getFilename():
    """
    Prompts the user for a file path, until user inputs valid file path.
    
    Return
    ------
    filename : str
        Path to file
    """
    
    while True:
        try:
            filename = os.path.abspath(input('Input file path: '))
            if os.path.isfile(filename): return filename
            raise IOError
        except IOError:
            print('Invalid filename')
