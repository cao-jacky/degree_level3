import numpy as np
import glob

import matplotlib
import matplotlib.pyplot as pyplot
from matplotlib.patches import Ellipse
from matplotlib import rc

pyplot.rc('text', usetex=True)
pyplot.rc('font', family='serif')
pyplot.rcParams['text.latex.preamble'] = [r'\boldmath']

matplotlib.rcParams['lines.color'] = 'k'
matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler('color', ['k'])

def plotter():
    """ Plotting a triangle plot. """

    fnames = glob.glob("/Users/jackycao/Documents/Projects/degree_level3/physics_problem_solving/program/bayesian_statistics/runs_extended/*.txt") # Where the data files are
    arrays = [np.loadtxt(f) for f in fnames] # Loading the data
    data = np.concatenate(arrays)
 

    # Axes for the plots
    f, axarr = pyplot.subplots(5, 5)  

    #: Plotting all the data
    axarr[4,0].scatter(data[:,2], data[:,1], marker='.', s=4) # O_L and L_P
    axarr[4,1].scatter(data[:,3], data[:,1], marker='.', s=4) # O_k and L_P
    axarr[4,2].scatter(data[:,4], data[:,1], marker='.', s=4) # O_m and L_P
    axarr[4,3].scatter(data[:,5], data[:,1], marker='.', s=4) # O_r and L_P
    axarr[4,4].scatter(data[:,1], data[:,1], marker='.', s=4) # L_P and L_P

    axarr[3,0].scatter(data[:,2], data[:,5], marker='.', s=4) # O_L and O_r
    axarr[3,1].scatter(data[:,3], data[:,5], marker='.', s=4) # O_k and O_r
    axarr[3,2].scatter(data[:,4], data[:,5], marker='.', s=4) # O_m and O_r
    axarr[3,3].scatter(data[:,5], data[:,5], marker='.', s=4) # O_r and O_r

    axarr[2,0].scatter(data[:,2], data[:,4], marker='.', s=4) # O_L and O_m
    axarr[2,1].scatter(data[:,3], data[:,4], marker='.', s=4) # O_k and O_m
    axarr[2,2].scatter(data[:,4], data[:,4], marker='.', s=4) # O_m and O_m

    axarr[1,0].scatter(data[:,2], data[:,3], marker='.', s=4) # O_l and O_k
    axarr[1,1].scatter(data[:,3], data[:,3], marker='.', s=4) # O_k and O_k

    axarr[0,0].scatter(data[:,2], data[:,2], marker='.', s=4) # O_l and O_l

    #: Plotting the averaged point
    axarr[4,0].scatter(np.average(data[:,2]), np.average(data[:,1]), marker=".", s=4, 
            color="limegreen")
    axarr[4,1].scatter(np.average(data[:,3]), np.average(data[:,1]), marker=".", s=4, 
            color="limegreen")
    axarr[4,2].scatter(np.average(data[:,4]), np.average(data[:,1]), marker=".", s=4, 
            color="limegreen")
    axarr[4,3].scatter(np.average(data[:,5]), np.average(data[:,1]), marker=".", s=4, 
            color="limegreen")

    axarr[3,0].scatter(np.average(data[:,2]), np.average(data[:,5]), marker=".", s=4, 
            color="limegreen")
    axarr[3,1].scatter(np.average(data[:,3]), np.average(data[:,5]), marker=".", s=4, 
            color="limegreen")
    axarr[3,2].scatter(np.average(data[:,4]), np.average(data[:,5]), marker=".", s=4, 
            color="limegreen")

    axarr[2,0].scatter(np.average(data[:,2]), np.average(data[:,4]), marker=".", s=4, 
            color="limegreen")
    axarr[2,1].scatter(np.average(data[:,3]), np.average(data[:,4]), marker=".", s=4, 
            color="limegreen")

    axarr[1,0].scatter(np.average(data[:,2]), np.average(data[:,3]), marker=".", s=4, 
            color="limegreen")


    #: Turning off tick labels for certain plots
    axarr[4,1].set_yticklabels([])
    axarr[4,2].set_yticklabels([])
    axarr[4,3].set_yticklabels([])
    axarr[4,4].set_yticklabels([])

    axarr[3,0].set_xticklabels([])
    axarr[3,1].set_yticklabels([])
    axarr[3,1].set_xticklabels([])
    axarr[3,2].set_yticklabels([])
    axarr[3,2].set_xticklabels([])
    axarr[3,3].set_yticklabels([])
    axarr[3,3].set_xticklabels([])

    axarr[2,0].set_xticklabels([])
    axarr[2,1].set_yticklabels([])
    axarr[2,1].set_xticklabels([])
    axarr[2,2].set_yticklabels([])
    axarr[2,2].set_xticklabels([])

    axarr[1,0].set_xticklabels([])
    axarr[1,1].set_yticklabels([])
    axarr[1,1].set_xticklabels([])

    #: Hiding subplots that I don't need
    axarr[0,1].axis('off')
    axarr[0,2].axis('off')
    axarr[0,3].axis('off')
    axarr[0,4].axis('off')
    axarr[0,4].axis('off')

    axarr[1,2].axis('off')
    axarr[1,3].axis('off')
    axarr[1,4].axis('off')

    axarr[2,3].axis('off')
    axarr[2,4].axis('off')

    axarr[3,4].axis('off')

    #: Labels
    axarr[4,0].set_xlabel(r'$\Omega_{\Lambda}$')
    axarr[4,0].set_ylabel(r'$L_{peak}$')
    axarr[4,1].set_xlabel(r'$\Omega_{k}$')
    axarr[4,2].set_xlabel(r'$\Omega_{m}$')
    axarr[4,3].set_xlabel(r'$\Omega_{r}$')
    axarr[4,4].set_xlabel(r'$L_{peak}$')

    axarr[0,0].set_ylabel(r'$\Omega_{\Lambda}$')
    axarr[1,0].set_ylabel(r'$\Omega_{k}$')
    axarr[2,0].set_ylabel(r'$\Omega_{m}$')
    axarr[3,0].set_ylabel(r'$\Omega_{r}$')

    # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
    pyplot.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
    pyplot.setp([a.get_yticklabels() for a in axarr[:, 4]], visible=False)

    pyplot.savefig("graphs_extended/triangle.pdf")

if __name__ == '__main__':
    plotter()
