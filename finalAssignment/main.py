"""
Ville Silvonen, ville.silvonen@student.tut.fi, 240086 

    RAK-19006, Various Topics in Civil Engineering, spring 2018 - 
    Python 3 for Scientific Computing, Final assignment
    
The purpose of this project is to remake a MATLAB code I used in a physics 
laboratory course work earlier this semester. The program will read a set of
data files and based on this data, will compute the concentrations of five
differrent gases in a sample gas mixture. Additionally, the program will 
draw some graphs based on the data. 
"""

# import modules deeded 
import os
import numpy as np

# change working directory to that with the data files
oldFolder = os.getcwd()
dataFilesFolder = oldFolder + '\dataFiles'
os.chdir(dataFilesFolder) 

# read data files
filters = [2710, 3060, 3320, 4270, 4740, 5756] # filters used in measurement
controlData = []
controlDataStd = []

for filter in filters :
    FileName = 'saatomittaus-' + str(filter)
    




os.chdir(oldFolder)

