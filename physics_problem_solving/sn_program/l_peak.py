import numpy as np

def f(mag):
    """ Units of flux initially in erg cm^(-2)s^(-1)Angstrom^(-1). """
    m_0 = -20.45 # Comparative magnitude
    ex = (mag-m_0) / (2.5) # The exponent
    # CONVERT FLUX TO SI
    return (10 ** (-ex))

def flux(data):
    """ Used with low redshift data, calculating the flux from the given magnitudes. """
    lzsn_data = data[1] # Selecting the data from the data module
    flux_store = np.zeros([lzsn_data.shape[0],1]) # Storing the calculated values of flux

    for i in range(lzsn_data.shape[0]):
        mag = lzsn_data[i][2] # Mag from the current SN
        flux_store[i] = f(mag) # Calculating the flux of the current SN
    return flux_store

def flux_uncert(data):
    """ Calculating uncertainty in the flux by adding the mangitude error onto the 
    magnitude, and taking it away. """
    lzsn_data = data[1] # Taking out the low redshift data
    flux_error_store = np.zeros([lzsn_data.shape[0],2]) # Storing the values for error on flux

    for i in range(lzsn_data.shape[0]):
        mag = lzsn_data[i][2] # Mag from the current supernova
        mag_uncert = lzsn_data[i][3] # Uncertainty on that magnitude

        mag_p = mag + mag_uncert # Magnitude with added uncertainty
        mag_n = mag - mag_uncert # Magnitude with uncertainty subtracted

        flux_p = f(mag_p) # Flux with uncertainty added
        flux_n = f(mag_n) # Flux with uncertainty subtracted

        flux = f(mag) # Flux of the object from magnitude

        flux_error_store[i][0] = flux - flux_p # Storing the greater uncert value
        flux_error_store[i][1] = flux_n - flux # Storing lesser uncert value

    uncert_av = np.average(flux_error_store, axis=1) # Averaging both the uncert values together
    return uncert_av

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
    """ Calculates the L_mean and L_max from low SN data. """
    l_vals = luminosity_peak(hubble, c, data) # Calls previous function
    l_mean = np.min(l_vals) # Min value in our L_peak range
    l_max = np.max(l_vals) # Max value in our L_peak range
    return l_mean, l_max

def flux_model(hubble, c, data, i, l_peak):
    """ Calculating the flux for the L_peak model values. """
    lzsn_data = data[1]
    cmv = comoving_distances(hubble, c, data) # Calling comoving distances function
    
    flux = l_peak / ( 4 * np.pi * (cmv[i])**2 * (1 + lzsn_data[i][1])**2) # Calculates flux
    return flux

def chi_sq_l_peak(hubble, c, data, step):
    """ Chi^2 function to find the suitable value for L_peak. """
    lzsn_data = data[1] # Calling the low redshift data
    flx = flux(data) # Using flux data for the low redshift data
    flx_unct = flux_uncert(data) # Calling the uncertainties

    l_lims = luminosity_range(hubble, c, data) # Calls previous function for L range
    
    #l_sol = 3.84 * (10**26) # Luminosity of the Sun in Watts, W
    l_sol = 1.0
    l_mean = l_lims[0] / l_sol # Mean luminosity in terms of Solar Luminosity
    l_max = l_lims[1] / l_sol # Max luminosity in terms of Solar Luminosity
    l_range = np.arange(l_mean, l_max, step) # Produces a range of L_peak values to test

    chi_sq_store = np.zeros([l_range.size,2]) # Stores the value for chi^2 for each step

    for i in range(l_range.size):
        """ Outer loop to test for each value for L_peak for our models. """
        l_peak = l_range[i] # Selecting L_peak value to use
        chi_sq_store[i][0] = l_peak # Stores current using L_peak value in first column
        current = [] # List to sum up all the chi^2 values
        for j in range(lzsn_data.shape[0]):
            """ Inner loop to calculate chi^2 over supernova. """
            f_obs = flx[j] # Observed flux from low redshift data
            f_mdl = flux_model(hubble, c, data, j, l_peak * l_sol) # Model flux

            val_n = (f_obs - f_mdl) ** 2 # Numerator of chi^2 value
            val_d = flx_unct[j] ** 2 # Denominator of chi^2 value
            val = val_n / val_d # Calculating the chi^2 value
            current.append(val) # Adding all the current chi^2s value to the list
        chi_sq_store[i][1] = np.sum(current) # Store total chi^2 values into an array
    return chi_sq_store

def chi_sq_min(hubble, c, data, step):
    """ Finding the minimum chi^2 value from our calculated data. """
    chi_sq_data = chi_sq_l_peak(hubble, c, data, step) # Data from chi^2 function
    chi_sq_min = np.min(chi_sq_data[:,1]) # Finding minimum chi^2 value from column

    min_index = np.where(chi_sq_data[:,1] == chi_sq_min) # Finding index of min value
    l_peak_min = chi_sq_data[:,0][min_index] # Finding value corresponding to min chi^2
   
    l_sol = 3.84 * (10**26) # Luminosity of the Sun in Watts, W

    return chi_sq_min, (l_peak_min)
