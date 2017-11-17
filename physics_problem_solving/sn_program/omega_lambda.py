# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
from scipy.integrate import quad

def f(mag):
    """ Flux in units of erg cm^(-2)s^(-1)Angstrom^(-1). """
    m_0 = -20.45 # Comparative magnitude
    ex = (mag-m_0) / (2.5) # The exponent
    return (10 ** (-ex))

def flux(data):
    """ Using distance supernova data, calculating the flux from the given magnitudes. """
    dsn_data = data[0] # Selecting the data from the data module
    flux_store = np.zeros([dsn_data.shape[0],1]) # Storing the calculated values of flux

    for i in range(dsn_data.shape[0]):
        mag = dsn_data[i][2] # Mag from the current SN
        flux_store[i] = f(mag) # Calculating the flux of the current SN
    return flux_store

def flux_uncert(data):
    """ Calculating uncertainty in the flux by adding the mangitude error onto the 
    magnitude, and taking it away. """
    dsn_data = data[0] # Taking out the high redshift data
    flux_error_store = np.zeros([dsn_data.shape[0],2]) # Storing the values for error on flux

    for i in range(dsn_data.shape[0]):
        mag = dsn_data[i][2] # Mag from the current supernova
        mag_uncert = dsn_data[i][3] # Uncertainty on that magnitude

        mag_p = mag + mag_uncert # Magnitude with added uncertainty
        mag_n = mag - mag_uncert # Magnitude with uncertainty subtracted

        flux_p = f(mag_p) # Flux with uncertainty added
        flux_n = f(mag_n) # Flux with uncertainty subtracted

        flux = f(mag) # Flux of the object from magnitude

        flux_error_store[i][0] = flux - flux_p # Storing the greater uncert value
        flux_error_store[i][1] = flux_n - flux # Storing lesser uncert value

    uncert_av = np.average(flux_error_store, axis=1) # Averaging both the uncert values together
    return uncert_av

def com_integral(x, O_L):
    """ The integral required to find the comoving distance, with: 
        x - our variable
        O_L - Value of Omega_Lambda being changed from two limits """
    z1 = (1 + x) ** 3 # Part of the integral
    B = O_L * (z1 - 1) # Another part of the integral
    return 1.0 / ( (z1 - B) ** 0.5 ) 

def flux_model(l_peak, cmv, z):
    l_peak = l_peak# Converting l_peak into Watts
    return l_peak / (4 * np.pi * (cmv ** 2) * ((1+z)**2))

def mag_model(flux):
    return -20.45 - (2.5 * np.log10(flux))

def chi_sq_omg_lam(hubble, c, data, step, l_peak):
    """ Chi^2 function to find the best value for \Omega_Lambda. """
    dsn_data = data[0] # Pulling out distant supernovae data
    flx = flux(data) # Finding the flux for distance supernova data
    flx_unct = flux_uncert(data) # Finding the uncertainties 

    O_L_range = np.arange(0.0, 1.0, step) # Produces range of Omega_Lambda values to test from 0 to 1

    chi_sq_store = np.zeros([O_L_range.size,2]) # Stores chi^2 for each step

    for i in range(O_L_range.size):
        """ Outer loop to test for each value of Omega_Lambda. """
        O_L = O_L_range[i] # Selecting Omega_Lambda value to use
        chi_sq_store[i][0] = O_L # Stores current value of Omega_Lambda in first column
        current = [] # List to store chi^2 values
        for j in range(dsn_data.shape[0]):
            """ Inner loop to calculate chi^2 over supernova data. """
            z = dsn_data[j][1] # Selecting redshift for current supernova
            f_obs = flx[j] # Observed flux calculated using distance supernova data
            f_mdl_cmv = quad(com_integral, 0, z, args=(O_L)) # Using Scipy to calculate the comoving integral
            f_mdl_cmv = f_mdl_cmv[0] * (c / hubble) # Selecting the value from integral routine
            f_mdl = flux_model(l_peak, f_mdl_cmv, z) # Model flux using functions

            val_n = (f_obs - f_mdl) ** 2 # Numerator of chi^2 value
            val_d = flx_unct[j] ** 2 # Denominator of chi^2 value
            val = val_n / val_d # Calculating the chi^2 value
            current.append(val) # Adding all the chi^2s into a list
        chi_sq_store[i][1] = np.sum(current) # Storing the summed chi^2 into array
    return chi_sq_store

def chi_sq_min(hubble, c, data, step, l_peak):
    """ Finding the minimum chi^2 value from the calculate data. """
    chi_sq_data = chi_sq_omg_lam(hubble, c, data, step, l_peak) # Data from chi^2 function
    chi_sq_min = np.min(chi_sq_data[:,1]) # Minimum chi^2 from column

    min_index = np.where(chi_sq_data[:,1] == chi_sq_min) # Finding index of min value
    O_L_min = chi_sq_data[:,0][min_index] # Finding minimum value of Omega_lambda
    return chi_sq_min, O_L_min
