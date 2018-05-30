# -*- coding: utf-8 -*-
"""
Ville Silvonen, ville.silvonen@student.tut.fi, 240086 

    RAK-19006, Various Topics in Civil Engineering, spring 2018 - 
    Python 3 for Scientific Computing, Final assignment
    
File: main.py

The purpose of this project is to remake a MATLAB code I used in a physics 
laboratory course work earlier this semester. The program will read a set of
data files and based on this data, will compute the concentrations of five
differrent gases in a sample gas mixture. Additionally, the program will 
draw some graphs based on the data. 
"""

# import modules deeded 
import os
import functions as fn
import numpy as np
import scipy.io as sio
   
# change working directory to that with the data files
oldFolder = os.getcwd()
dataFilesFolder = oldFolder + '\dataFiles'
os.chdir(dataFilesFolder)

filters = [2710, 3060, 3220, 4270, 4740, 5756] # filters used in measurement
controlData = []
controlDataStd = []
sampleData = []
sampleDataStd = []

# read data files and save data to containers
for filter in filters :
    FileName = 'saatomittaus-' + str( filter ) + '.txt'
    data = fn.readFile(FileName)
    data = fn.cutData( data, 180 )
    controlData.append(data)
    controlDataStd.append(np.std(data))
    
    FileName = 'nayteputki-' + str( filter ) + '.txt'
    data = fn.readFile(FileName)
    data = fn.cutData( data, 180 )
    sampleData.append(data)
    sampleDataStd.append(np.std(data))
    
os.chdir(oldFolder)

# load the absorption vectors of the gases and filters
# squeeze_me squeezes unit matrix dimensions 
gases = sio.loadmat('gases.mat', squeeze_me=True)
absorptions = sio.loadmat('filterAbsorbtion.mat', squeeze_me=True)
wavelen = sio.loadmat('lambda.mat', squeeze_me=True)

p=1.013e5       # Pa, pressure of gas
k=1.38e-23      # J/K, Boltzmann constant
T=298           # K, temperature of gas
L=0.2           # m, length of sample tube

# the wavelength vector at which the gas is scanned, and the changes in 
# wavelength
wavelen = wavelen['lambda']
dwavelen = np.abs(np.diff(wavelen)) 

gases = [gases['H2O'], gases['CO'], gases['C2H2'], gases['CO2'], gases['CH4']]



