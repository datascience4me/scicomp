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
import numpy.linalg as lin
import scipy.io as sio
import matplotlib.pyplot as plt

   
# change working directory to that with the data files
oldFolder = os.getcwd()
dataFilesFolder = oldFolder + '\dataFiles'
os.chdir(dataFilesFolder)

filters = [2710, 3060, 3220, 4270, 4740, 5756] # filters used in measurement
controlData = []
sampleData = []

# read data files and save data to containers
for filter in filters :
    FileName = 'saatomittaus-' + str( filter ) + '.txt'
    data = fn.readFile(FileName)
    data = np.mean(fn.cutData( data, 180 ))
    controlData.append(data)
    
    FileName = 'nayteputki-' + str( filter ) + '.txt'
    data = fn.readFile(FileName)
    data = np.mean(fn.cutData( data, 180 ))
    
    # sample data should never be a higher value than control data, because
    # the filters will absorb some of the incident light
    if controlData[-1] < data:
        sampleData.append(controlData[-1])
    else:        
        sampleData.append(data)
    
os.chdir(oldFolder)

# load the absorption vectors of the gases and filters from .mat files,
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
dwavelen = np.append(dwavelen, dwavelen[-1])

# set the absorption vectors of the gases and filters
gasnames = ['H2O', 'CO', 'C2H2', 'CO2', 'CH4']
gases = [gases[gasname] for gasname in gasnames]
absorptions = [absorptions['NB'+str(filter)] for filter in filters]

# the concentrations are solved by multivariable calculus
# for this we define the matrix coefficients
A = np.zeros([len(absorptions), len(gases)])
for i in range(len(absorptions)):
    for j in range(len(gases)):
        alpha = np.sum( np.multiply( np.multiply(gases[j], absorptions[i]),
                                    dwavelen)*1e-2 )
        A[i,j] = alpha


A = A*p/(k*T)/1e4*L

I0 = controlData
I = sampleData

Y = np.zeros([len(absorptions),1])
for i in range(len(absorptions)):
    y = ( 1-I[i]/I0[i] )*np.sum( np.multiply(absorptions[i], dwavelen*1e-2))
    Y[i,0] = y
    
# solving the concentrations from the matrix equation    
C = lin.solve(A.T.dot(A), A.T.dot(Y))
C = np.squeeze(C)

# print results
print('Concentration of gases in sample tube:')
for i in range(len(C)):
    c = C[i]*1e6
    print(gasnames[i], ': ', '%.2f' % c, ' ppm', sep='')

# bar plot of results
x = np.arange(5)
plt.bar(x,C*1e6)
plt.xticks(x, gasnames)
plt.xlabel('Gas')
plt.ylabel('Concentration (ppm)')
