# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

import l_peak

def data(hubble, c, data, step):
    chi_sq_min = l_peak.chi_sq_min(hubble, c, data, step)[0] # Calling the value for chi_sq_min and the corresponding L_peak
    d = l_peak.chi_sq_l_peak(hubble, c, data, step) # Calling the data used to find the value of min chi^2

    min_index = np.where(d[:,1] == chi_sq_min)[0] # Finding index of min value

    for i in range(20):
        min_a = min_index + i # Finding above chi^2
        for j in range(20):
            min_b = min_index - j # Finding below chi^2
            
            chi_a = d[:,1][min_a] # Finding the corresponding chi^2 value for above
            chi_b = d[:,1][min_b] # Finding the corresponding chi^2 value for below

            #print chi_a - chi_b

            if np.abs(chi_a - chi_b) >= 1:
                print chi_a - chi_b
                print chi_sq_min
                print min_index
                print min_a, min_b
                break
        break 


