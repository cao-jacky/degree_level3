import numpy as np

def f(mag):
    """ Units of flux initially in erg cm^(-2)s^(-1)Angstrom^(-1). """
    m_0 = -20.45 # Comparative magnitude
    ex = (mag-m_0) / (2.5) # The exponent
    return (10 ** (-ex)) 

def flux(data):
    """ Used with low redshift data, calculating the flux from the given magnitudes. """
    lzsn_data = data[1] # Selecting the data from the data module
    flux_store = np.zeros([lzsn_data.shape[0],1]) # Storing the calculated values of flux

    for i in range(lzsn_data.shape[0]):
        mag = lzsn_data[i][2] # Mag from the current SN
        flux_store[i] = f(mag) # Calculating the flux of the current SN
    # HOW WOULD UNCERTAINTIES WORK FOR THIS MAGNITUDE??? 
    return flux_store

def comoving_distances(hubble, c, data):
    """ Comoving distance is defined by $R_0 \eta=cz/ H_0$. """
    lzsn_data = data[1] # Selecting the data from the data module
    cmv_store = np.zeros([lzsn_data.shape[0],1]) # Storing the calculated comoving values

    for i in range(lzsn_data.shape[0]):
        redshift = lzsn_data[i][1]
        cmv_store[i] = (c * redshift) / hubble
    return cmv_store

def luminosity_peak(hubble, c, data):
    """ Calculating L_peak for low supernova data. """
    lzsn_data = data[1] # Pulling lzsn data
    l_peak_store = np.zeros([lzsn_data.shape[0],1]) # Storing our L_peak values

    cmv = comoving_distances(hubble, c, data) # Calling comoving distance function
    flx = flux(data) # Calling flux function

    for i in range(lzsn_data.shape[0]):
        l_peak = 4 * np.pi * (cmv[i])**2 * flx[i] * (1 + lzsn_data[i][1])**2
        l_peak_store[i] = l_peak
    return l_peak_store

