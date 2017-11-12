import l_peak
import omega_lambda
import matplotlib.pyplot as pyplot

def plot_l(hubble, c, data, step):
    """ Plotting the chi^2 against L_peak. """
    dt = l_peak.chi_sq_l_peak(hubble, c, data, step)
    l_sol = 3.84 * (10**26) # Luminosity of the Sun in Watts, W
    
    fig = pyplot.figure()
    pyplot.title('chi^2 against L_peak')
    pyplot.xlabel('L_peak')
    pyplot.ylabel('chi^2')
    pyplot.plot(dt[:,0]*l_sol,dt[:,1])
    pyplot.savefig('luminosity_peak.pdf')
    #pyplot.show()

def plot_o(hubble, c, data, step, l_peak):
    """ Plotting chi^2 against Omega_Lambda. """
    dat = omega_lambda.chi_sq_omg_lam(hubble, c, data, step, l_peak)

    fig = pyplot.figure()
    pyplot.title('chi^2 against Omega_Lambda')
    pyplot.xlabel('Omega_lambda')
    pyplot.ylabel('chi^2')
    pyplot.plot(dat[:,0],dat[:,1])
    pyplot.savefig('omega_lambda.pdf')
    #pyplot.show()

def com_integral(x, O_L):
    """ The integral required to find the comoving distance, with: 
        x - our variable
        O_L - Value of Omega_Lambda being changed from two limits """
    z1 = (1 + x) ** 3 # Part of the integral
    B = O_L * (z1 - 1) # Another part of the integral
    return 1.0 / ( (z1 - B) ** 0.5 ) 

def z_function(hubble, c, z, l_peak, O_L):
    val_n = l_peak # Numerator of fraction
    com_int = quad(com_integral, 0, z, args=(0_L))
    val_d = 4 * np.pi * 
    return 

def model(hubble, c, data, step, l_peak):
    """Producing 'model' data from our found L_peak and Omega_Lambda"""
    dt_min = omega_lambda.chi_sq_min(hubble, c, data, step, l_peak)
    
    dsn_data = data[0] # Distant supernovae data
    data_store = np.zeros([dsn_data.shape[0],2])

    for i in range(dsn_data.shape[0]):
        mag = dsn_data[i][2]
    


def plot_redmag(hubble, c, data, step, l_peak):
    """ Plotting redshift vs magnitude, data and model. """

    fig = pyplot.figure()
    pyplot.title('redshift against magnitude')
    pyplot.xlabel('magnitude')
    pyplot.ylabel('redshift')
    pyplot.scatter(data[0][:,2],data[0][:,1])
    pyplot.savefig('redmag.pdf')


