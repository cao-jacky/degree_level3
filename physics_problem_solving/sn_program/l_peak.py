import numpy as np

def f(mag):
    """ Units of flux initially in erg cm^(-2)s^(-1)Angstrom^(-1). """
    m_0 = -20.45 # Comparative magnitude
    ex = (mag-m_0) / (2.5) # The exponent
    # CONVERT FLUX TO SI
    return (10 ** (-ex)) * (10**7)

def flux(data):
    """ Used with low redshift data, calculating the flux from the given magnitudes. """
    lzsn_data = data[1] # Selecting the data from the data module
    flux_store = np.zeros([lzsn_data.shape[0],1]) # Storing the calculated values of flux

    for i in range(lzsn_data.shape[0]):
        mag = lzsn_data[i][2] # Mag from the current SN
        flux_store[i] = f(mag) # Calculating the flux of the current SN
    return flux_store

def flux_uncertainty(data):
    lzsn_data = data[1] # Selection out low redshift data
    flux_data = flux(data) # Finding flux information
    uncert = np.zeros([lzsn_data.shape[0],1]) # Storing values for uncertainty 
    
    for i in range(lzsn_data.shape[0]):
        A = flux_data[i]
        print A
        #flux_uncert = A * np.log(10) * alpha_A

    return 

def comoving_distances(hubble, c, data):
    """ Comoving distance is defined by $R_0 \eta=cz/ H_0$. """
    lzsn_data = data[1] # Selecting the data from the data module
    cmv_store = np.zeros([lzsn_data.shape[0],1]) # Storing the calculated comoving values

    for i in range(lzsn_data.shape[0]):
        redshift = lzsn_data[i][1]
        cmv_store[i] = (c * redshift) / hubble
    return cmv_store

def luminosity_peak(hubble, c, data):
    """ Calculating L_peak for each SN in low supernova data. """
    lzsn_data = data[1] # Pulling lzsn data
    l_peak_store = np.zeros([lzsn_data.shape[0],1]) # Storing our L_peak values

    cmv = comoving_distances(hubble, c, data) # Calling comoving distance function
    flx = flux(data) # Calling flux function

    for i in range(lzsn_data.shape[0]):
        l_peak = 4 * np.pi * (cmv[i])**2 * flx[i] * (1 + lzsn_data[i][1])**2
        l_peak_store[i] = l_peak
    return l_peak_store

def luminosity_range(hubble, c, data):
    l_vals = luminosity_peak(hubble, c, data) 
    l_mean = np.mean(l_vals) # Min value in our L_peak range
    l_max = np.max(l_vals) # Max value in our L_peak range
    return l_mean, l_max
