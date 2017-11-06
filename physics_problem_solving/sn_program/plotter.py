import l_peak
import matplotlib.pyplot as pyplot

def plot(hubble, c, data, step):
    """ Plotting the chi^2 against L_peak. """
    dt = l_peak.chi_sq_l_peak(hubble, c, data, step)
    l_sol = 3.84 * (10**26) # Luminosity of the Sun in Watts, W
    
    fig1 = pyplot.figure()
    pyplot.title('test')
    pyplot.xlabel('L_Peak')
    pyplot.ylabel('chi^2')
    pyplot.plot(dt[:,0]*l_sol,dt[:,1])
    pyplot.show()
