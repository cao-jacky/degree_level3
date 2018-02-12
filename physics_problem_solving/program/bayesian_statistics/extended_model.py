import numpy as np
from scipy.integrate import quad

def com_integral(x, ol, ok, om, orad, w):
    """ The integral required to find the comoving distance, with: 
        x - our variable
        ol - Omega_Lambda
        ok - Omega_k
        om - Omega_m
        orad - Omega_r
        """
    c1 = (1 + x) # Component one
    qnt = 3 * (1 + w) # Quintessence exponent
    #: The denominator of the equation
    denom = (c1**(qnt) * ol) + (c1**2 * ok) + (c1**3 * om) + (c1**4 * orad) 
    return 1.0 / ( denom ** 0.5 ) 

def model(H0, c, z, lp, ol, ok, om, orad, w):
    """ Function to calculate magnitude for a given redshift. """
    m_0 = -20.45 
    val_n = lp # Numerator of fraction
    cmv = quad(com_integral, 0, z, args=(ol, ok, om, orad, w))
    cmv = (c / H0) * cmv[0]
    val_d = 4 * np.pi * (cmv**2) * ((1+z)**2) # Denominator of fraction
    frac = val_n / val_d # Calculating the fraction
    return m_0 - (2.5 * np.log10(frac))

