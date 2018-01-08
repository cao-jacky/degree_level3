# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

import omega_lambda

def find_nearest(array,value):
    """ Function to find the nearest value. """
    idx = (np.abs(array-value)).argmin()
    return array[idx]

def values(hubble, c, data, step, l_peak):
    """ Returns data when looking above and below our minimum chi^2 value"""
    chi_sq_min = omega_lambda.chi_sq_min(hubble, c, data, step, l_peak)[0] # Calling the value for chi_sq_min and the corresponding L_peak
    
    d = omega_lambda.chi_sq_omg_lam(hubble, c, data, step, l_peak) # Calling the data used to find the value of min chi^2

    min_index = np.where(d[:,1] == chi_sq_min)[0] # Finding index of min value
    omega_lambda_min = d[:,0][min_index]

    diff_storage = [] # List to store the differences calculated in the following loop

    for i in np.arange(1,10,1):
        above = min_index + i # Index, i values larger than min_index
        below = min_index - i # Index, i values smaller than min_index

        above_chi = d[:,1][above] # Calling the chi^2 values
        below_chi = d[:,1][below]

        above_subt = above_chi - chi_sq_min # Subtracting the chi^2's together
        below_subt = below_chi - chi_sq_min
        diff_average = np.average([above_subt, below_subt])# Above, below difference average

        diff_storage.append(diff_average) # Storing into our list 

    diff_storage = np.asarray(diff_storage) # Converting list into an array
    diff_nearest = find_nearest(diff_storage, 1.0) # Finding which difference is closest to one

    diff_index = np.where(diff_storage == diff_nearest)[0] + 1

    csqu_above = omega_lambda_min - d[:,0][min_index + diff_index] # Chi^2 uncertainty above
    csqu_below = omega_lambda_min - d[:,0][min_index - diff_index] # Chi^2 uncertainty below
    return csqu_below, csqu_above

