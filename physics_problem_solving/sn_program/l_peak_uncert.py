# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

import l_peak

def data(hubble, c, data, step):
    chi_sq_min = l_peak.chi_sq_min(hubble, c, data, step)[0] # Calling the value for chi_sq_min and the corresponding L_peak
    d = l_peak.chi_sq_l_peak(hubble, c, data, step) # Calling the data used to find the value of min chi^2

    min_index = np.where(d[:,1] == chi_sq_min) # Finding index of min value

    print min_index
