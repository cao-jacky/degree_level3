import numpy as np
import matplotlib.pyplot as pyplot
import matplotlib.colors
from matplotlib import rc
import re

pyplot.rc('text', usetex=True)
pyplot.rc('font', family='serif')
pyplot.rcParams['text.latex.preamble'] = [r'\boldmath']

path = '/Users/jackycao/Documents/Projects/degree_level3/laboratory_project/programs/covariance/'
sn = ['2017hhz']

def data(loc_sn):
    """ Reads the file. """
    
    with open(loc_sn) as f:
        lines = f.readlines()

    data = []

    for i in range(len(lines)):
        split = lines[i].split()
        if i in {0,4,8,12}:
            data.append(split[2])
        else:
            data.append(split[1])
    return data

def data_array(loc_sn):
    """ Storing data into an array. """
    
    dt = data(loc_sn)
    dt_n = np.zeros([4, 4])

    count = 0 # Storing current location of the data
    for i in range(4):
        for j in range(4):
            count = count + 1
            dt_n[i][j] = re.findall(r"[-+]?\d*\.\d+|\d+", dt[count-1])[0]
    return dt_n

def plotter(loc_sn):
    """ Plots data into a heat map. """
    dt = data_array(loc_sn)

    fig1 = pyplot.figure()
    pyplot.imshow(dt, norm=matplotlib.colors.LogNorm(vmin=0.001, vmax=1.5))
    pyplot.colorbar()
    pyplot.savefig("heatmap_" + sn[0] +".pdf")

if  __name__ == '__main__':
    plotter(path + sn[0] + '_covariance.txt')
