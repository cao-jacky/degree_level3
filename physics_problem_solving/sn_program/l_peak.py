import numpy as np

def f(mag):
    """ Units of flux initially in erg cm^(-2)s^(-1)Angstrom^(-1). """
    m_0 = -20.45 # Comparative magnitude

    ex = (mag-m_0) / (2.5) # The exponent
    print 10 ** (-ex)
    return (10 ** (-ex)) 

def calculate_flux(data):
    """ Used with low redshift data, calculating the flux from the given magnitudes. """
    
    lzsn_data = data[1] # Selecting the data from the data module

    for i in range(lzsn_data.shape[0]):
        mag = lzsn_data[i][2] # Mag from the current SN
        fl = f(mag) # Calculating the flux of the current SN
        print fl

    # HOW WOULD UNCERTAINTIES WORK FOR THIS MAGNITUDE???
    
    
    return 

def comoving_distances():
    return b

def luminosity_peak():
    return c

