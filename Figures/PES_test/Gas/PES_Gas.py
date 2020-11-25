# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:36:21 2020

@author: chr218
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from scipy import constants
from scipy.integrate import odeint


'''
Functions & Subroutines
'''


#...

'''
Program Begins Here
'''
#Import Barriers [kJ/mol]
data = pd.read_csv("G_Barriers.csv")

#Collect Gibbs free energy barriers.-These will ultimately be used for the rate constants.
Gf = (data.values[:,1])
Gr = (data.values[:,2])

print(Gf)

'''
Plotting
'''
#Plot params

#Generate Platforms
x_increments = range(len(Gf)) #increments for x-axis of our plot
x_increments_offset = [x+0.5 for x in x_increments] #Offset x-increments to create 'platforms'
    

fig, ax = plt.subplots() 
#ax.plot(x_increments, Gf,linestyle='None', marker='o', color= 'k')
#ax.plot(x_increments_offset, Gf,linestyle='None', marker='o', color= 'k')

#Generate Dashed line & Bold lines connecting platforms
for i,x in enumerate(x_increments):
    y_bold = []
    x_bold = []
    y_bold.append(Gf[i])
    y_bold.append(Gf[i])
    x_bold.append(x)
    x_bold.append(x_increments_offset[i])
    
    if i != len(x_increments)-1:
        y_dashed = []
        x_dashed= []
        y_dashed.append(Gf[i])
        y_dashed.append(Gf[i+1])
        x_dashed.append(x_increments_offset[i])
        x_dashed.append(x_increments[i+1])
    
    #plot
    ax.plot(x_bold, y_bold ,linestyle='-', linewidth = 5, marker='None', color= 'k')
    ax.plot(x_dashed, y_dashed, linestyle='dashed', marker='None', color= 'k')