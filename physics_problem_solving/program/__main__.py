# -*- coding: utf-8 -*-
import timeit
start = timeit.default_timer() # Keeping track of program time

import data 
import edata

import l_peak
import omega_lambda
import l_peak_uncert
import omega_lambda_uncert

import plotter
import eplotter

import numpy as np
import datetime

""" Module to calculate the dark energy density, Omega_Lambda."""

now = datetime.datetime.now()

#---------- STANDARD VALUES ----------#
cm_data = [75, (3*(10**8))] # [H_0 (km s^-1 Mpc^-1), c (ms^-1)]
# Convert H_0 into SI
cm_data[0] = (cm_data[0] / 3.09) * (1.0 / (10**19)) # H_0 in units of s^-1
step = 0.01 # Step for L_peak to be sought for
rnge = [0,1] # Range to test Omega_Lambda values in

#---------- MILESTONE WORK ----------#
def milestone(file_name):
    sn_data = data.data_input(file_name) # Calling data to use

    # Finding the best fit L_peak value, and best fit Omega_Lambda value
    l_p = l_peak.fchi_sq_min(cm_data[0], cm_data[1], sn_data, step)
    o_l = omega_lambda.chi_sq_min(cm_data[0], cm_data[1], sn_data, step, float(l_p[1]))

    # Finding the uncertainties on L_peak and Omega_Lambda
    l_p_uncert = l_peak_uncert.values(cm_data[0], cm_data[1], sn_data, 0.01)
    o_l_uncert = omega_lambda_uncert.values(cm_data[0], cm_data[1], sn_data, step, float(l_p[1]))
    return l_p, l_p_uncert, o_l, o_l_uncert

#---------- EXTENSION WORK ----------#
def extension(file_name1, file_name2, data_type):
    """ file_name1 is the main file for the function.
        file_name2 is the secondary file for the function.
        data_type is what the function should do. """
    
    if data_type == "extension":
        sn_data = edata.redshift(file_name1) # Extension data set
        sn_data = [np.delete(sn_data[0], 4, axis=1), np.delete(sn_data[1], 4, axis=1)] 
    elif data_type == "total":
        # Both sets of data
        odat = data.data_input(file_name2) # Original data set
        edt = edata.redshift(file_name1) # Extension data set
        # : Removing the probability column
        edat = [np.delete(edt[0], 4, axis=1), np.delete(edt[1], 4, axis=1)] 
        sn_data = [np.append(odat[0], edat[0], axis=0), 
                np.append(odat[1], edat[1], axis=0)]
    elif data_type == "low_mass":
        sn_data = edata.galaxy_low(file_name1)
        sn_data = [np.delete(sn_data[0], 4, axis=1), np.delete(sn_data[1], 4, axis=1)] 
    elif data_type == "high_mass":
        sn_data = edata.galaxy_high(file_name1)
        sn_data = [np.delete(sn_data[0], 4, axis=1), np.delete(sn_data[1], 4, axis=1)]
    
    # Finding the best fit L_peak value, and best fit Omega_Lambda value
    fl_p = l_peak.fchi_sq_min(cm_data[0], cm_data[1], sn_data, 0.01)
    #ml_p = l_peak.mchi_sq_min(cm_data[0], cm_data[1], tot_data, 0.01)
    o_l = omega_lambda.chi_sq_min(cm_data[0], cm_data[1], sn_data, 0.01, float(fl_p[1]))

    # Finding the uncertainties on L_peak and Omega_Lambda
    l_p_uncert = l_peak_uncert.values(cm_data[0], cm_data[1], sn_data, 0.01)
    o_l_uncert = omega_lambda_uncert.values(cm_data[0], cm_data[1], sn_data, step, float(fl_p[1]))
    return fl_p, l_p_uncert, o_l, o_l_uncert

#---------- GRAPH PLOTTERS ----------#
def plotting(data):
    dt = data 
    l_p = dt[0]
    plotter.plot_l(cm_data[0], cm_data[1], sn_data, step)
    plotter.plot_o(cm_data[0], cm_data[1], sn_data, step, float(l_p[1]))
    plotter.plot_redmag(cm_data[0], cm_data[1], sn_data, step, float(l_p[1]))
    eplotter.plot_h(data)


#---------- CALLING STUFF ----------#

file_name = 'program/data/sn_data.txt'
efile_name = 'program/data/SCPUnion2.1_mu_vs_z.txt'

calling_milestone = True 
calling_extension = True
graphs = True

#---------- SAVING TO TEXT FILE ----------#
# This should be an automatic process which outputs a file confirming stuff has been done

txt_name = "supernova_cosmology.txt"
f = open(txt_name, 'w')
f.write("These values were generated at this date and time: " + str(now) + '\n')
f.write("\n")

f.write("The following values were also calculated in flux space! \n")
if calling_milestone == True:
    ml = milestone(file_name)
    f.write('\n')
    f.write("Using our milestone program we have calculated: " + '\n')
    f.write("L_peak: " + str(ml[0][1]) + ", + " + str(np.abs(ml[1][1][0])) + ", - " + str(np.abs(ml[1][0][0])) + "\n")
    f.write("Omega_Lambda: " + str(ml[2][1] ) + ", + " + str(np.abs(ml[3][1][0])) + ", - " + str(np.abs(ml[3][0][0]))  + "\n")

if calling_extension == True:
    f.write('\n')
    f.write("Using our extension program we have calculated the following: " + '\n')

    # Complete extension data set
    f.write("By using our complete extension data set: " + '\n')
    ex = extension(efile_name, file_name, "extension")
    f.write("L_peak: " + str(ex[0][1]) + ", + " + str(np.abs(ex[1][1][0])) + ", - " + str(np.abs(ex[1][0][0])) + "\n")
    f.write("Omega_Lambda: " + str(ex[2][1] ) + ", + " + str(np.abs(ex[3][1][0])) + ", - " + str(np.abs(ex[3][0][0]))  + "\n")
    f.write('\n')
 
    # Extension and original data set
    f.write("By using our complete extension and original data set: " + '\n')
    ex1 = extension(efile_name, file_name, "total")
    f.write("L_peak: " + str(ex1[0][1]) + ", + " + str(np.abs(ex1[1][1][0])) + ", - " + str(np.abs(ex1[1][0][0])) + "\n")
    f.write("Omega_Lambda: " + str(ex1[2][1] ) + ", + " + str(np.abs(ex1[3][1][0])) + ", - " + str(np.abs(ex1[3][0][0]))  + "\n")
    f.write('\n')

    # Extension data set: low mass
    f.write("By using our complete extension data set, for low mass galaxies: " + '\n')
    ex2 = extension(efile_name, file_name, "low_mass")
    f.write("L_peak: " + str(ex2[0][1]) + ", + " + str(np.abs(ex2[1][1][0])) + ", - " + str(np.abs(ex2[1][0][0])) + "\n")
    f.write("Omega_Lambda: " + str(ex2[2][1] ) + ", + " + str(np.abs(ex2[3][1][0])) + ", - " + str(np.abs(ex2[3][0][0]))  + "\n")
    f.write('\n')

    # Extension data set: low mass
    f.write("By using our complete extension data set, for high mass galaxies: " + '\n')
    ex3 = extension(efile_name, file_name, "high_mass")
    f.write("L_peak: " + str(ex3[0][1]) + ", + " + str(np.abs(ex3[1][1][0])) + ", - " + str(np.abs(ex3[1][0][0])) + "\n")
    f.write("Omega_Lambda: " + str(ex3[2][1] ) + ", + " + str(np.abs(ex3[3][1][0])) + ", - " + str(np.abs(ex3[3][0][0]))  + "\n")
    f.write('\n')

f.close()

#---------- GRAPHING ----------#
if graphs == True:
    odat = data.data_input(file_name) # Original data set
    edt = edata.redshift(efile_name) # Extension data set
    # : Removing the probability column
    edat = [np.delete(edt[0], 3, axis=1), np.delete(edt[1], 3, axis=1)] 

    eplotter.plot_h(cm_data[0], cm_data[1], [edat, odat], step, [ml[0][1],ml[2][1]], 
            [ex[0][1], ex[2][1]])

stop = timeit.default_timer()
print("Time this program took: ")
print(stop-start)
