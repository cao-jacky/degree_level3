# -*- coding: utf-8 -*-
import numpy as np
from scipy.integrate import quad

import matplotlib.pyplot as pyplot
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

import l_peak
import omega_lambda

pyplot.rc('text', usetex=True)
pyplot.rc('font', family='serif')
pyplot.rcParams['text.latex.preamble'] = [r'\boldmath']

def plot_l(hubble, c, data, step):
    """ Plotting the chi^2 against L_peak. """
    dt = l_peak.chi_sq_l_peak(hubble, c, data, step)
    l_sol = 3.84 * (10**26) # Luminosity of the Sun in Watts, W
    
    fig = pyplot.figure()  
    pyplot.title(r"\textbf{$\chi$$^2$ against L$_{peak}$}")
    pyplot.xlabel(r'\textbf{L$_{peak}$}')
    pyplot.ylabel(r'$\chi$$^2$')
    pyplot.plot(dt[:,0],dt[:,1], color = '0.1')
    pyplot.savefig('graphs/luminosity_peak.pdf')

def plot_o(hubble, c, data, step, l_peak):
    """ Plotting chi^2 against Omega_Lambda. """
    dat = omega_lambda.chi_sq_omg_lam(hubble, c, data, step, l_peak)

    fig = pyplot.figure()
    pyplot.title(r"\textbf{$\chi$$^2$ against $\Omega$$_{\Lambda}$}")
    pyplot.xlabel(r'$\Omega_{\Lambda}$')
    pyplot.ylabel(r'$\chi$$^2$')
    pyplot.plot(dat[:,0],dat[:,1], color = '0.1')
    pyplot.savefig('graphs/omega_lambda.pdf')

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

def plot_redmag(hubble, c, data, step, l_peak):
    """ Plotting redshift vs magnitude, data and model. """

    O_L = omega_lambda.chi_sq_min(hubble, c, data, step, l_peak)[1]
    
    z = np.linspace(0, 1, num=100) # Generating redshift values to plot agianst
    fn_r = np.zeros([len(z),1]) # Storing calculated magnitudes

    # Creating data to plot the model
    for i in range(len(z)):
        fn_r[i] = model_ranged(hubble, c, data, step, l_peak, z[i], O_L)

    fig = pyplot.figure()
    pyplot.title(r"\textbf{Magnitude agaisnt Redshift}")
    pyplot.xlabel(r'$z$')
    pyplot.ylabel(r'\textbf{mag}')
    pyplot.errorbar(data[0][:,1],data[0][:,2],yerr=data[0][:,3],marker=".",color="0.1",elinewidth=0.5,linestyle="None")
    pyplot.errorbar(data[1][:,1],data[1][:,2],yerr=data[1][:,3],marker=".",color="0.1",elinewidth=0.5,linestyle="None")
    pyplot.plot(z, fn_r, color="0.1")
    pyplot.savefig('graphs/mag_redshift.pdf')
