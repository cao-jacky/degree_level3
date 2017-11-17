# -*- coding: utf-8 -*-
import data 
import l_peak
import omega_lambda
import l_peak_uncert
import omega_lambda_uncert
import plotter

""" Module to calculate the dark energy density, Omega_Lambda."""

file_name = 'sn_data.txt'
cm_data = [75, (3*(10**8))] # In the order [hubbles_constant (km s^-1 Mpc^-1), speed_of_light (ms^-1)]
# Convert H_0 into SI
cm_data[0] = (cm_data[0] / 3.09) * (1.0 / (10**19)) # Hubble's costant in units of s^-1

rnge = [0,1] # Range to test Omega_Lambda values in

data = data.data_input(file_name)

# Finding the best fit L_peak value, and best fit Omega_Lambda value
l_peak = l_peak.chi_sq_min(cm_data[0], cm_data[1], data, 0.01)
omega_lambda.chi_sq_min(cm_data[0], cm_data[1], data, 0.01, float(l_peak[1]))

# Finding the uncertainties on L_peak and Omega_Lambda
l_peak_uncert.data(cm_data[0], cm_data[1], data, 0.01)

# Plotting the graphs that we need
plotter.plot_l(cm_data[0], cm_data[1], data, 0.01)
plotter.plot_o(cm_data[0], cm_data[1], data, 0.01, float(l_peak[1]))
plotter.plot_redmag(cm_data[0], cm_data[1], data, 0.01, float(l_peak[1]))
