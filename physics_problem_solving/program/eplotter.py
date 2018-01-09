import numpy as np
from scipy.integrate import quad

import matplotlib.pyplot as pyplot
from matplotlib import rc

pyplot.rc('text', usetex=True)
pyplot.rc('font', family='serif')
pyplot.rcParams['text.latex.preamble'] = [r'\boldmath']

""" Plots the data onto a Hubble diagram. """

def com_integral(x, O_L):
    """ The integral required to find the comoving distance, with: 
        x - our variable
        O_L - Value of Omega_Lambda being changed from two limits """
    z1 = (1 + x) ** 3 # Part of the integral
    B = O_L * (z1 - 1) # Another part of the integral
    return 1.0 / ( (z1 - B) ** 0.5 ) 

def m_function(hubble, c, z, l_peak, O_L):
    """ Function to calculate magnitude for a given redshift. """
    m_0 = -20.45 
    val_n = l_peak # Numerator of fraction
    cmv = quad(com_integral, 0, z, args=(O_L))
    cmv = (c / hubble) * cmv[0]
    val_d = 4 * np.pi * (cmv**2) * ((1+z)**2) # Denominator of fraction
    frac = val_n / val_d # Calculating the fraction
    return m_0 - (2.5 * np.log10(frac))

def model_ranged(hubble, c, data, step, l_peak, z, O_L):
    """ Using model with a generated linspace. """ 
    m = m_function(hubble, c, z, l_peak, O_L)
    return m

def plot_h(hubble, c, data, step, milestone, extension1):
    """ milestone a list containing l_peak and O_L"""
    odt = data[1] # Original data
    edt = data[0] # Extension data
    
    z = np.linspace(0, 1.5, num=150) # Generating redshift values to plot agianst
    model_one = np.zeros([len(z),1]) # Storing magnitudes for model_1, milestone
    model_two = np.zeros([len(z),1]) # Storing magnitudes for model_2, extension

    # Creating data to plot the model
    for i in range(len(z)):
        model_one[i] = model_ranged(hubble, c, data, step, milestone[0], z[i], 
                milestone[1])
        model_two[i] = model_ranged(hubble, c, data, step, extension1[0], z[i], 
                extension1[1])

    fig = pyplot.figure()
    pyplot.title(r"\textbf{Magnitude agaisnt Redshift}")
    pyplot.xlabel(r'$z$')
    pyplot.ylabel(r'\textbf{mag}')

    # Plotting the data
    pyplot.errorbar(edt[0][:,1],edt[0][:,2],yerr=edt[0][:,3],marker=".",color="0.1",
            elinewidth=0.5,linestyle="None", alpha=0.5)
    pyplot.errorbar(edt[1][:,1],edt[1][:,2],yerr=edt[1][:,3],marker=".",color="0.1",
            elinewidth=0.5,linestyle="None", alpha=0.5)

    pyplot.errorbar(odt[0][:,1],odt[0][:,2],yerr=odt[0][:,3],marker=".",color="grey",
            elinewidth=0.5,linestyle="None", alpha=0.5)
    pyplot.errorbar(odt[1][:,1],odt[1][:,2],yerr=odt[1][:,3],marker=".",color="grey",
            elinewidth=0.5,linestyle="None", alpha=0.5)

    pyplot.plot(z, model_one, color="blue")
    pyplot.plot(z, model_two, color="red")

    pyplot.savefig('program/graphs/hubble_diagram.pdf')
