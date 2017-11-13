# -*- coding: utf-8 -*-
import numpy as np
from scipy.integrate import quad

import l_peak
import omega_lambda
import matplotlib.pyplot as pyplot

def plot_l(hubble, c, data, step):
    """ Plotting the chi^2 against L_peak. """
    dt = l_peak.chi_sq_l_peak(hubble, c, data, step)
    l_sol = 3.84 * (10**26) # Luminosity of the Sun in Watts, W
    
    fig = pyplot.figure()
    pyplot.title('chi^2 against L_peak')
    pyplot.xlabel('L_peak')
    pyplot.ylabel('chi^2')
    pyplot.plot(dt[:,0]*l_sol,dt[:,1])
    pyplot.savefig('luminosity_peak.pdf')
    #pyplot.show()

def plot_o(hubble, c, data, step, l_peak):
    """ Plotting chi^2 against Omega_Lambda. """
    dat = omega_lambda.chi_sq_omg_lam(hubble, c, data, step, l_peak)

    fig = pyplot.figure()
    pyplot.title('chi^2 against Omega_Lambda')
    pyplot.xlabel('Omega_lambda')
    pyplot.ylabel('chi^2')
    pyplot.plot(dat[:,0],dat[:,1])
    pyplot.savefig('omega_lambda.pdf')
    #pyplot.show()

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
    frac = val_n / val_d # Calculating the fraction
    return m_0 - (2.5 * np.log10(frac * (10**7)))

def model_ranged(hubble, c, data, step, l_peak, z):
    """ Using model with a generated linspace. """ 
    l_sol = 3.84 * (10**26) # Luminosity of the Sun in Watts, W
    O_L = omega_lambda.chi_sq_min(hubble, c, data, step, l_peak)[1]
    hubble = hubble / (10**6)
    l_peak = l_peak * l_sol
    O_L = 0.84
    print O_L, l_peak, c, z, hubble
    m = m_function(hubble, c, z, l_peak, O_L)
    #print m
    return m

def plot_redmag(hubble, c, data, step, l_peak):
    """ Plotting redshift vs magnitude, data and model. """

    z = np.linspace(0, 1, num=100) # Generating redshift values to plot agianst
    fn_r = np.zeros([len(z),1]) # Storing calculated magnitudes

    for i in range(len(z)):
        fn_r[i] = model_ranged(hubble, c, data, step, l_peak, z[i])

    fig = pyplot.figure()
    pyplot.title('magnitude against redshift')
    pyplot.ylabel('magnitude')
    pyplot.xlabel('redshift')
    pyplot.scatter(data[0][:,1],data[0][:,2])
    pyplot.scatter(data[1][:,1],data[1][:,2])
    pyplot.plot(z, fn_r)
    pyplot.savefig('redmag.pdf')
