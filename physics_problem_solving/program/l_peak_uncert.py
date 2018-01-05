# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

import l_peak

rng = 20 # Value above and below min chi^2 to look for

def find_nearest(array,value):
    """ Function to find the nearest value. """
    idx = (np.abs(array-value)).argmin()
    return array[idx]

def chi_sqs(hubble, c, data, step):
    """ Returns data when looking above and below our minimum chi^2 value"""
    chi_sq_min = l_peak.chi_sq_min(hubble, c, data, step)[0] # Calling the value for chi_sq_min and the corresponding L_peak
    d = l_peak.chi_sq_l_peak(hubble, c, data, step) # Calling the data used to find the value of min chi^2

    min_index = np.where(d[:,1] == chi_sq_min)[0] # Finding index of min value

    chi_diff = np.zeros([(rng-1)**2,3]) # Storing the chi^2 differences
    chi_diff_list = []

    for i in range(rng):
        min_a = min_index + i # Finding above chi^2
        if min_a == min_index:
            pass # Skip if it is the same
        else:
            for j in range(rng):
                min_b = min_index - j # Finding below chi^2
                if min_b == min_index:
                    pass # Skip if it is the same 
                else: 
                    chi_a = d[:,1][min_a] # Finding the corresponding chi^2 value for above
                    chi_b = d[:,1][min_b] # Finding the corresponding chi^2 value for below
                    
                    chi_diff_list.append([chi_a,chi_b,chi_a-chi_b])

    # Converting list into an array and reshaping 
    chi_diff_list = np.asarray(chi_diff_list).reshape(((rng-1)**2, 3))
    return chi_diff_list, chi_sq_min

def one(hubble, c, data, step):
    """ Finding where the different is closest to one in the chi^2 values. """
    d = chi_sqs(hubble, c, data, step) # Calling our data and min chi_sq
    dt = d[0] # Calling the chi^2 data
    chi_sq_min = d[1] # Calling minimum chi^2 orginally found

    lv = find_nearest(dt[:,2], 1.0) # Lowest value
    lv_loc = np.where(dt[:,2] == lv) # Lowest value location
    
    lv_row = dt[lv_loc][0] # Calling the row that it is related to

    print(lv, lv_row)
    print(lv_row[0], chi_sq_min)
    print(lv_row[0]-chi_sq_min, lv_row[1]-chi_sq_min)

