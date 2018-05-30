# -*- coding: utf-8 -*-
"""
Created on Wed May 30 17:41:53 2018

@author: Ville
"""

"""
This function cuts the input data to a specified length. 

input: list of data, number of data points in output
output: cut list of data
"""
import numpy as np

def cutData( data, outSize ):
    dataSize = len(data)
    diff = dataSize - outSize
    indices = []

    # number of removed elements from beginning and end of list
    if np.mod( diff, 2) == 0:
        n = int(diff/2)
    else:
        n = int( (diff-1)/2 )
        
    # indices of data points to be removed  
    for i in range(n):
        indices.append(i)
        indices.append( len(data)-1-i )
    
    print(indices)
    # remove data points from data
    for i in sorted( indices, reverse=True ):
        del data[i]
    
    return data