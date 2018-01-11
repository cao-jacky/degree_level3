import numpy as np
from scipy.integrate import quad

import matplotlib.pyplot as pyplot
from matplotlib import rc

import edata
import model

pyplot.rc('text', usetex=True)
pyplot.rc('font', family='serif')
pyplot.rcParams['text.latex.preamble'] = [r'\boldmath']

# Our parameters 
H0 = (75 /3.09) * (1.0 / (10**19)) # Hubble's constant
c = (3*(10**8)) # Speed of light in a vacuum

lp_true = 2.92936635 * (10**35) # L_peak 
ol_true = 0.82 #Omega_Lambda

step = 0.01


efile_name = 'data/SCPUnion2.1_mu_vs_z.txt'

def data():
    sn_data = edata.redshift(efile_name)
    sn_data = [np.delete(sn_data[0], 4, axis=1), np.delete(sn_data[1], 4, axis=1)]
    return sn_data



