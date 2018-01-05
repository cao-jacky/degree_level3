# -*- coding: utf-8 -*-
import data 
import edata

import l_peak
import omega_lambda
import l_peak_uncert
import omega_lambda_uncert

import plotter

""" Module to calculate the dark energy density, Omega_Lambda."""

#---------- STANDARD VALUES ----------#
cm_data = [75, (3*(10**8))] # [H_0 (km s^-1 Mpc^-1), c (ms^-1)]
# Convert H_0 into SI
cm_data[0] = (cm_data[0] / 3.09) * (1.0 / (10**19)) # H_0 in units of s^-1
rnge = [0,1] # Range to test Omega_Lambda values in

#---------- MILESTONE WORK ----------#
def milestone():
    # Initial calling
    file_name = 'program/data/sn_data.txt'
    sn_data = data.data_input(file_name) # Calling data to use

    # Finding the best fit L_peak value, and best fit Omega_Lambda value
    l_p = l_peak.chi_sq_min(cm_data[0], cm_data[1], sn_data, 0.01)
    omega_lambda.chi_sq_min(cm_data[0], cm_data[1], sn_data, 0.01, float(l_p[1]))

    # Finding the uncertainties on L_peak and Omega_Lambda
    l_p_uncert = l_peak_uncert.one(cm_data[0], cm_data[1], sn_data, 0.01)
    #omega_lamba_uncert.data
    omega_lambda_uncert = 1.0

    # Plotting the graphs that we need
    #plotter.plot_l(cm_data[0], cm_data[1], sn_data, 0.01)
    #plotter.plot_o(cm_data[0], cm_data[1], sn_data, 0.01, float(l_p[1]))
    #plotter.plot_redmag(cm_data[0], cm_data[1], sn_data, 0.01, float(l_p[1]))

    return l_p, l_p_uncert, omega_lambda, omega_lambda_uncert

#---------- EXTENSION WORK ----------#
def extension():
    efile_name = 'program/data/SCPUnion2.1_mu_vs_z.txt'
    edat = edata.data_splitter(efile_name)

#---------- CALLING STUFF ----------#

milestone()

