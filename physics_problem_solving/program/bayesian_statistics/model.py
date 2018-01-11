import numpy as np
from scipy.integrate import quad

def com_integral(x, ol):
    """ The integral required to find the comoving distance, with: 
        x - our variable
        ol - Value of Omega_Lambda being changed from two limits """
    z1 = (1 + x) ** 3 # Part of the integral
    B = ol * (z1 - 1) # Another part of the integral
    return 1.0 / ( (z1 - B) ** 0.5 ) 

def m_function(H0, c, z, lp, ol):
    """ Function to calculate magnitude for a given redshift. """
    m_0 = -20.45 
    val_n = lp # Numerator of fraction
    cmv = quad(com_integral, 0, z, args=(ol))
    cmv = (c / H0) * cmv[0]
    val_d = 4 * np.pi * (cmv**2) * ((1+z)**2) # Denominator of fraction
    frac = val_n / val_d # Calculating the fraction
    return m_0 - (2.5 * np.log10(frac))

def model_running(H0, c, z, lp, ol):
    """ Our model"""  
    m = m_function(H0, c, z, lp, ol)
    return m

