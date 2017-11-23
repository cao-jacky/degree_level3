# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib import rc
#from numpy import *

def data(sne):
    DataInModelB = 'data/' + sne + '/' + sne + '_lc_Bs_model.dat'
    DataInModelV = 'data/' + sne + '/' + sne + '_lc_Vs_model.dat'
    DataInB = 'data/'+ sne '/' + sne + '_lc_Bs_data.dat'
    DataInV = 'data/'+ sne '/' + sne + '_lc_Bs_data.dat'

    # For the actual SN data
    with open(DataIn) as f:
        DataInLines = f.readlines()

    data_in = np.zeros([len(DataInLines),4])

    for i in range(len(data_in)):
        if i in {0,1,2,3}:
            pass
        else:
            split = DataInLines[i].split()
            for k in range(4):
                data_in[i][k] = split[k]

    data_in = np.delete(data_in, [0,1,2,3], axis=0)
    data_in = np.delete(data_in, (-1), axis=1) # Final data set to plot, w/out error row

    # For the model/template for the SN
    with open(DataInModel) as g:
        DataInModelLines = g.readlines()

    data_in_model = np.zeros([len(DataInModelLines),2])

    for i in range(len(data_in_model)):
        if i in {0,1}:
            pass
        else:
            split = DataInModelLines[i].split()
            for k in range(2):
                if k == 0:
                    split[k] = split[k].replace(",", "")
                data_in_model[i][k] = split[k]
    
    data_in_model = np.delete(data_in_model, [0,1], axis=0)

    return data_in, data_in_model

def plot():
    dt = data()
    data_in = dt[0]
    data_in_model = dt[1]
    
    fig1 = pyplot.figure()
    fig1.gca().invert_yaxis()
    pyplot.scatter(data_in[:,0], data_in[:,1])
    pyplot.plot(data_in_model[:,0], data_in_model[:,1])
    pyplot.savefig('test.pdf')


if __name__ == '__main__':
    plot()
