# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib import rc

pyplot.rc('text', usetex=True)
pyplot.rc('font', family='serif')
pyplot.rcParams['text.latex.preamble'] = [r'\boldmath']

def data(sne):
    # Reading in the SN data for B and V bands
    DataInModelB = 'data/' + sne + '/' + sne + '_lc_Bs_model.dat'
    DataInModelV = 'data/' + sne + '/' + sne + '_lc_Vs_model.dat'
    DataInB = 'data/' + sne + '/' + sne + '_lc_Bs_data.dat'
    DataInV = 'data/' + sne + '/' + sne + '_lc_Vs_data.dat'

    # For the SN B data
    with open(DataInB) as f:
        DataInLinesB = f.readlines()

    data_in_B = np.zeros([len(DataInLinesB),4]) # Storing the text file into array

    for i in range(len(data_in_B)):
        if i in {0,1,2,3}:
            pass
        else:
            split = DataInLinesB[i].split()
            for k in range(4):
                data_in_B[i][k] = split[k]

    data_in_B = np.delete(data_in_B, [0,1,2,3], axis=0)
    data_in_B = np.delete(data_in_B, (-1), axis=1) # Final data set to plot, w/out error row

    # For the SN V data
    with open(DataInV) as f:
        DataInLinesV = f.readlines()

    data_in_V = np.zeros([len(DataInLinesV),4]) # Storing the text file into array

    for i in range(len(data_in_V)):
        if i in {0,1,2,3}:
            pass
        else:
            split = DataInLinesV[i].split()
            for k in range(4):
                data_in_V[i][k] = split[k]

    data_in_V = np.delete(data_in_V, [0,1,2,3], axis=0)
    data_in_V = np.delete(data_in_V, (-1), axis=1) # Final data set to plot, w/out error row

    # -------------------- #

    # Template for B 
    with open(DataInModelB) as g:
        DataInModelLinesB = g.readlines()

    data_in_model_B = np.zeros([len(DataInModelLinesB),2]) # Create storage array

    for i in range(len(data_in_model_B)):
        if i in {0,1}:
            pass # Ignore first rows from files
        else:
            split = DataInModelLinesB[i].split()
            for k in range(2):
                if k == 0:
                    split[k] = split[k].replace(",", "") # Removing commas
                data_in_model_B[i][k] = split[k] # Storing into array
    
    data_in_model_B = np.delete(data_in_model_B, [0,1], axis=0) # Delete comment rows

    # Template for V 
    with open(DataInModelV) as g:
        DataInModelLinesV = g.readlines()

    data_in_model_V = np.zeros([len(DataInModelLinesV),2]) # Create storage array

    for i in range(len(data_in_model_V)):
        if i in {0,1}:
            pass # Ignore first rows from files
        else:
            split = DataInModelLinesV[i].split()
            for k in range(2):
                if k == 0:
                    split[k] = split[k].replace(",", "") # Removing commas
                data_in_model_V[i][k] = split[k] # Storing into array
    
    data_in_model_V = np.delete(data_in_model_V, [0,1], axis=0) # Delete comment rows
    return data_in_B, data_in_model_B, data_in_V, data_in_model_V

def plot(sne):
    dt = data(sne) # Calling data function

    # Pulling data and model for the supernova
    data_in_B = dt[0] # Data in B-band
    data_in_model_B = dt[1] # Model in B-band
    data_in_V = dt[2] # Data in V-band
    data_in_model_V = dt[3] # Model in V-band
 
    fig1 = pyplot.figure()
    fig1.gca().invert_yaxis()  
    
    pyplot.xlabel(r'\textbf{Time Elapsed Since Observing}')
    pyplot.ylabel(r'\textbf{Magnitude}')

    # Plotting B band data
    pyplot.errorbar(data_in_B[:,0], data_in_B[:,1], 
            yerr=data_in_B[:,2], color='0.1', linestyle='None', fmt='.', 
            markersize=5, capsize=5)
    pyplot.plot(data_in_model_B[:,0], data_in_model_B[:,1], color='0.1', label='B')
    pyplot.text(data_in_model_B[:,0][-1]+0.4, data_in_model_B[:,1][-1]+0.05, 
            r'\textbf{B}')

    # Plotting V band data
    pyplot.errorbar(data_in_V[:,0], data_in_V[:,1]-1, 
            yerr=data_in_V[:,2], color='0.1', linestyle='None', fmt='.', 
            markersize=5, capsize=5)
    pyplot.plot(data_in_model_V[:,0], data_in_model_V[:,1]-1, color='0.1', 
            linestyle='dashed', label='V')
    pyplot.text(data_in_model_V[:,0][-1]+0.4, data_in_model_V[:,1][-1]-0.9, 
            r'\textbf{V-1}')

    pyplot.savefig('graphs/' + sne + '.pdf')
