# -*- coding: utf-8 -*-
"""
Ville Silvonen, ville.silvonen@student.tut.fi, 240086 

    RAK-19006, Various Topics in Civil Engineering, spring 2018 - 
    Python 3 for Scientific Computing, Final assignment

File: functions.py

Functions used in the main program.
"""


import numpy as np


# Cuts the input data to a specified length. 
# input:   
#   data: list of data 
#   outSize: number of data points in output
# output:   
#   data: cut list of data
def cutData( data, outSize ):
    dataSize = data.size
    diff = dataSize - outSize
    
    # remove data points from beginnnig and end of data
    if np.mod( diff, 2) == 0:
        data = data[ int(diff/2) : int(dataSize - diff/2) ]
    else:
        data = data[ int((diff-1)/2) : int(dataSize - (diff-1)/2) - 1 ]

    return data


# Reads the data file (second column has the data we're interested in)
# input: 
#   FileName: name of file to be read
# output: 
#   data: ndarray type array with data
def readFile(FileName):
    data = np.loadtxt( FileName, usecols=1 )
    
    return data
    