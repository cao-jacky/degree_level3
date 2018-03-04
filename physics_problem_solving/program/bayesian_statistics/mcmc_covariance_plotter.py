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
    f, axarr = pyplot.subplots(4, 4, figsize=(8,6))  

    # Setting axis limits for Omega_rad
    lims = [0.000,0.0001]
    axarr[3,3].set_xlim(lims[0], lims[1])
    axarr[2,0].set_ylim(lims[0], lims[1])
    axarr[2,1].set_ylim(lims[0], lims[1])
    axarr[2,2].set_ylim(lims[0], lims[1])
    axarr[2,3].set_xlim(lims[0], lims[1])
    axarr[2,3].set_ylim(lims[0], lims[1])

    #: Plotting all the data
    axarr[3,0].scatter(data[:,2], data[:,1], marker='.', s=10) # O_L and L_P
    axarr[3,1].scatter(data[:,3], data[:,1], marker='.', s=10) # O_k and L_P
    axarr[3,2].scatter(data[:,4], data[:,1], marker='.', s=10) # O_m and L_P
    axarr[3,3].scatter(data[:,5], data[:,1], marker='.', s=10) # O_r and L_P

    axarr[2,0].scatter(data[:,2], data[:,5], marker='.', s=10) # O_L and O_r
    axarr[2,1].scatter(data[:,3], data[:,5], marker='.', s=10) # O_k and O_r
    axarr[2,2].scatter(data[:,4], data[:,5], marker='.', s=10) # O_m and O_r

    axarr[1,0].scatter(data[:,2], data[:,4], marker='.', s=10) # O_L and O_m
    axarr[1,1].scatter(data[:,3], data[:,4], marker='.', s=10) # O_k and O_m

    axarr[0,0].scatter(data[:,2], data[:,3], marker='.', s=10) # O_l and O_k

    #: Plotting the averaged point
    axarr[3,0].scatter(np.average(data[:,2]), np.average(data[:,1]), marker=".", s=10, 
            color="red")
    axarr[3,1].scatter(np.average(data[:,3]), np.average(data[:,1]), marker=".", s=10, 
            color="red")
    axarr[3,2].scatter(np.average(data[:,4]), np.average(data[:,1]), marker=".", s=10, 
            color="red")
    axarr[3,3].scatter(np.average(data[:,5]), np.average(data[:,1]), marker=".", s=10, 
            color="red")

    axarr[2,0].scatter(np.average(data[:,2]), np.average(data[:,5]), marker=".", s=10, 
            color="red")
    axarr[2,1].scatter(np.average(data[:,3]), np.average(data[:,5]), marker=".", s=10, 
            color="red")
    axarr[2,2].scatter(np.average(data[:,4]), np.average(data[:,5]), marker=".", s=10, 
            color="red")

    axarr[1,0].scatter(np.average(data[:,2]), np.average(data[:,4]), marker=".", s=10, 
            color="red")
    axarr[1,1].scatter(np.average(data[:,3]), np.average(data[:,4]), marker=".", s=10, 
            color="red")

    axarr[0,0].scatter(np.average(data[:,2]), np.average(data[:,3]), marker=".", s=10, 
            color="red")

    #: Turning off tick labels for certain plots
    axarr[3,1].set_yticklabels([])
    axarr[3,2].set_yticklabels([])
    axarr[3,3].set_yticklabels([])

    axarr[2,0].set_xticklabels([])
    axarr[2,1].set_yticklabels([])
    axarr[2,1].set_xticklabels([])
    axarr[2,2].set_yticklabels([])
    axarr[2,2].set_xticklabels([])

    axarr[1,0].set_xticklabels([])
    axarr[1,1].set_yticklabels([])
    axarr[1,1].set_xticklabels([])

    axarr[0,0].set_xticklabels([])

    #: Custom tick labels
    axarr[2,0].set_yticklabels([r'$0.0$',r'$2.5$',r'$5.0$',r'$7.5$',r'$10.0$'])
    axarr[3,3].set_xticklabels([r'$0.0$',r'$2.5$',r'$5.0$',r'$7.5$',r'$10.0$'])

    #: Hiding subplots that I don't need
    axarr[0,1].axis('off')
    axarr[0,2].axis('off')
    axarr[0,3].axis('off')

    axarr[1,2].axis('off')
    axarr[1,3].axis('off')

    axarr[2,3].axis('off')

    #: Labels
    axarr[3,0].set_xlabel(r'$\Omega_{\Lambda}$')
    axarr[3,1].set_xlabel(r'$\Omega_{k}$')
    axarr[3,2].set_xlabel(r'$\Omega_{m}$')
    axarr[3,3].set_xlabel(r'$\Omega_{r}$')

    axarr[0,0].set_ylabel(r'$\Omega_{k}$')
    axarr[1,0].set_ylabel(r'$\Omega_{m}$')
    axarr[2,0].set_ylabel(r'$\Omega_{r}$') 
    axarr[3,0].set_ylabel(r'$L_{peak}$')

    # Rotation
    pyplot.setp(axarr[3,0].xaxis.get_majorticklabels(), rotation=45, fontsize=15)
    pyplot.setp(axarr[3,1].xaxis.get_majorticklabels(), rotation=45, fontsize=15)
    pyplot.setp(axarr[3,2].xaxis.get_majorticklabels(), rotation=45, fontsize=15)
    pyplot.setp(axarr[3,3].xaxis.get_majorticklabels(), rotation=45, fontsize=15)
   
    pyplot.setp(axarr[0,0].yaxis.get_majorticklabels(), rotation=45, fontsize=15)
    pyplot.setp(axarr[1,0].yaxis.get_majorticklabels(), rotation=45, fontsize=15)
    pyplot.setp(axarr[2,0].yaxis.get_majorticklabels(), rotation=45, fontsize=15)
    pyplot.setp(axarr[3,0].yaxis.get_majorticklabels(), rotation=45, fontsize=15)

    # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
    pyplot.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
    pyplot.setp([a.get_yticklabels() for a in axarr[:, 3]], visible=False)

    pyplot.tick_params(axis='y', which='major', labelsize=15)
    pyplot.tick_params(axis='x', labelsize=15)

    pyplot.savefig("graphs_extended/triangle.pdf")
    pyplot.savefig("graphs_extended/triangle_transparent.png", transparent=True)

if __name__ == '__main__':
    plotter()
