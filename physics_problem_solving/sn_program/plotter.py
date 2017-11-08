import l_peak
import omega_lambda
import matplotlib.pyplot as pyplot

def plot_l(hubble, c, data, step):
    """ Plotting the chi^2 against L_peak. """
    dt = l_peak.chi_sq_l_peak(hubble, c, data, step)
    l_sol = 3.84 * (10**26) # Luminosity of the Sun in Watts, W
    
    fig1 = pyplot.figure()
    pyplot.title('chi^2 against L_peak')
    pyplot.xlabel('L_peak')
    pyplot.ylabel('chi^2')
    pyplot.plot(dt[:,0]*l_sol,dt[:,1])
    pyplot.show()

def plot_o(hubble, c, data, step, l_peak):
    """ Plotting chi^2 against Omega_Lambda. """
    dat = omega_lambda.chi_sq_omg_lam(hubble, c, data, step, l_peak)

    fig2 = pyplot.figure()
    pyplot.title('chi^2 against Omega_Lambda')
    pyplot.xlabel('Omega_lambda')
    pyplot.ylabel('chi^2')
    pyplot.plot(dat[:,0],dat[:,1])
    pyplot.show()



