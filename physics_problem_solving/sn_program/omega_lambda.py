import numpy as np

# using L_peak from lzsn data we could then reuse 10.14 to calculate the flux for each 
# distant SN? But then we have to deal with the comoving distances for high redshift.

def flux_obs(hubble, c, data, l_peak):
    """ Calculating the observed value for flux using: 
        f_obs =  \frac{L_peak}{4\pi [R_0 S(\eta)]^2 (1+z)^2 . """
    num = l_peak # Numerator of f_obs eqn
    dsn_data = data[0]
    f_o = np.zeros([dsn_data.shape[0],1]) # Storing all the calculated values for f_observed
    
    for i in range(dsn_data.shape[0]):
        z = dsn_data[i][1]
        cmv = (c * z) / hubble # Comoving distance R_0 \eta
        den = 4 * np.pi * (cmv**2) * (1 + z) **2 # Denominator of the equation
        f_o[i] = num/den # Calculated value of f_observed

    print f_o
    return f_o

def chi_squared():
    return chi_sq

def omega_lambda():

    # outside, L_peak testing
    # inner loop chi_squared over supernova

    # L_peak limits
    l_step = 100
    l_peak = 0.0

    for i in range():
        for i in range():
            ???
