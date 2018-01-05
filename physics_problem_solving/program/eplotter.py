import numpy as np

import matplotlib.pyplot as pyplot
from matplotlib import rc

pyplot.rc('text', usetex=True)
pyplot.rc('font', family='serif')
pyplot.rcParams['text.latex.preamble'] = [r'\boldmath']

""" Plots the extra data onto a Hubble diagram. """

def plot_h(data):
    odt = data[1] # Original data
    edt = data[0] # Extension data

    fig = pyplot.figure()
    pyplot.title(r"\textbf{Distance agaisnt Redshift}")
    pyplot.xlabel(r'$z$')
    pyplot.ylabel(r'\textbf{Distance}')
    pyplot.errorbar(edt[0][:,1],edt[0][:,2],yerr=edt[0][:,3],marker=".",color="0.1",elinewidth=0.5,linestyle="None")
    pyplot.errorbar(edt[1][:,1],edt[1][:,2],yerr=edt[1][:,3],marker=".",color="0.1",elinewidth=0.5,linestyle="None")

    pyplot.errorbar(odt[0][:,1],odt[0][:,2],yerr=odt[0][:,3],marker=".",color="grey",elinewidth=0.5,linestyle="None")
    pyplot.errorbar(odt[1][:,1],odt[1][:,2],yerr=odt[1][:,3],marker=".",color="grey",elinewidth=0.5,linestyle="None")

    pyplot.savefig('program/graphs/hubble_diagram.pdf')
