import numpy as np
import matplotlib.pyplot as pyplot
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

def new_data(loc_sn):
    """ Outputting into a new format. """

    dt = data(loc_sn)
    dt_n = np.zeros([len(dt), 3])

    for i in range(len(dt)):
        if i in {0,4,8,12}:
            dt_n[i][1] = 1
        else:
            dt_n[i][1] = dt_n[i-1][1] + 1
        if i < 4:
            dt_n[i][0] = 1
        if 4 < i < 8:
            dt_n[i][0] = 2
        if 8 < i < 12:
            dt_n[i][0] = 3
        if i > 12:
            dt_n[i][0] = 4

    for i in range(len(dt)):
        no = re.findall(r"[-+]?\d*\.\d+|\d+", dt[i]) # Pulling out number from the string
        dt_n[i][2] = no[0]
    return dt_n

def plotter(loc_sn):
    dt = new_data(loc_sn)

    fig1 = pyplot.figure()
    im = fig1.pcolormesh(dt[:,0], dt[:,1], dt[:,2])
    fig1.colorbar(im)
    pyplot.savefig("heatmap.pdf")



if  __name__ == '__main__':
    plotter(path + sn[0] + '_covariance.txt')
