import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib import rc

def data(data):
    """ Reads data and stores into an array. """

    with open(data) as f:
        lines = f.readlines()

    data_file = np.zeros([len(lines),5])

    for i in range(len(data_file)):
        if lines[i][0].isdigit() == True:
            split = lines[i].split()
            for k in range(5):
                data_file[i][k] = split[k]

    data_file = np.delete(data_file,[0,1],0) # Removes two initial empty arrays
    
    return data_file

def plot(data_file):
    d = data(data_file)

    zeros = np.zeros([d.shape[0],1])

    # Plot B band
    fig1 = pyplot.figure()
    fig1.gca().invert_yaxis()
    pyplot.rc('text', usetex=True)
    pyplot.rc('font', family='serif')
    pyplot.title(r'\textbf{B band}')
    pyplot.xlabel(r'\textbf{Time Elapsed Since Observing}')
    pyplot.ylabel(r'\textbf{Magnitude}')
    pyplot.errorbar(d[:,0], d[:,1], yerr=d[:,2], fmt='o', markersize=8, capsize=5)

    # Plot V band
    fig2 = pyplot.figure()
    fig2.gca().invert_yaxis()
    pyplot.rc('text', usetex=True)
    pyplot.rc('font', family='serif')
    pyplot.title(r'\textbf{V band}')
    pyplot.xlabel(r'\textbf{Time Elapsed Since Observing}')
    pyplot.ylabel(r'\textbf{Magnitude}')
    pyplot.errorbar(d[:,0], d[:,3], yerr=d[:,4], fmt='o', markersize=8, capsize=5)
    pyplot.show()

if __name__ == '__main__':
    plot("data/2017hhz.txt")
