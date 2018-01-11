import numpy as np
from scipy.integrate import quad

import matplotlib.pyplot as pyplot
from matplotlib import patches
from matplotlib import rc

import edata
import model

pyplot.rc('text', usetex=True)
pyplot.rc('font', family='serif')
pyplot.rcParams['text.latex.preamble'] = [r'\boldmath']

# Our parameters 
H0 = (75 /3.09) * (1.0 / (10**19)) # Hubble's constant
c = (3*(10**8)) # Speed of light in a vacuum

step = 0.01

def data(file_name):
    sn_data = edata.redshift(file_name)
    sn_data = [np.delete(sn_data[0], 4, axis=1), np.delete(sn_data[1], 4, axis=1)]
    return sn_data[0]

def error_function(file_name, lp, ol):
    dt = data(file_name)
    m_mdl = np.zeros([len(dt[:,1]),1]) # Storing the model magnitudes
    #: Producing model data with the redshifts from file
    for i in range(len(dt[:,1])):
        m_mdl[i] = model.model_running(H0, c, dt[:,1][i], lp, ol)

    # Joining data and model values array
    total_data = np.concatenate((dt,m_mdl), axis=1)

    # Chi^2: (data-model)**2/(error**2)
    chi_sq = ((total_data[:,2] - total_data[:,4])**2) / (total_data[:,3]**2)
    total_chi_sq = np.sum(chi_sq) # Sums all the values together
    return total_chi_sq

def likelihood_ratio(chi_sq_crrnt, chi_sq_prpsed):
    return np.exp(- chi_sq_prpsed + chi_sq_crrnt)

def current_values(file_name, lp, ol):
    chi_sq_crrnt = error_function(file_name, lp, ol) / 2 # Current chi^2

    #: Proposed values for new Omega_Lambda and L_peak
    ol_prpsed = np.random.normal(ol, 0.15, 1)
    lp_prpsed = np.random.normal(lp, 0.2*(10**35),1)
    print(ol_prpsed, lp_prpsed)
    if ol_prpsed > 1.0:
        ol_prpsed = np.random.normal(ol, 0.15, 1)

    chi_sq_prpsed = error_function(file_name, lp_prpsed, ol_prpsed) / 2 # Proposed chi^2

    ratio = likelihood_ratio(chi_sq_crrnt, chi_sq_prpsed) # Calcualting the ratio
    return ratio, lp_prpsed, ol_prpsed

def mcmc(file_name, lp, ol, rng):
    lp_ol = np.zeros([rng, 3]) # Storing all our values

    for i in range(len(lp_ol)):
        lp_n = lp
        ol_n = ol
        if i == 0:
            lp_ol[i][1] = lp
            lp_ol[i][2] = ol
        else:
            ratio_value = current_values(file_name,lp_n,ol_n)
            lp_ol[i][0] = ratio_value[0]
            lp_ol[i][1] = ratio_value[1]
            lp_ol[i][2] = ratio_value[2]
            if ratio_value[0] > np.random.rand(1):
                lp = ratio_value[1]
                ol = ratio_value[2]
            else:
                lp = lp
                ol = ol
    return lp_ol

def maximum_likelihood(file_name, lp, ol, rng):
    data = mcmc(file_name, lp, ol, rng)
    #: Saving data to a textfile to then plot
    np.savetxt("bayesian_statistics/data.txt", data)

    data_sorted = data[data[:,0].argsort()] # Sorting by the likelihood probability
    data_likelihood = np.where(data_sorted[:,0] < 1)[0]
    lto = data_likelihood[-1] # Last entry which is less than one, use as an index
    max_lh_row = data_sorted[lto] # Row with the maximum likelihood data
    lp_max = max_lh_row[1] # For L_peak
    ol_max = max_lh_row[2] # For Omega_Lambda
    return lp_max, ol_max

def plotter(max_point):
    """ Plots into a covariance plot"""
    data = np.loadtxt("bayesian_statistics/data.txt")

    fig1 = pyplot.figure()
    #: Labels
    #pyplot.title(r"\textbf{Covariance plot of L_{peak} and Omega_{Lambda}}")
    pyplot.xlabel(r'$L_{peak}$')
    pyplot.ylabel(r'$\Omega_{\Lambda}$')

    #: Plotting main data
    pyplot.scatter(data[:,1], data[:,2],marker=".",color="0.1")
    pyplot.scatter(3.60936635 * (10**35),0.78, marker=".", color="red")
    pyplot.scatter(max_point[0],max_point[1], marker=".", color="green")

    #: Plotting confidence interval ellipses
    ##: Calculating largest L_peak variance
    lp_max_var = np.amax(data[:,1]) - max_point[0]
    lp_min_var = max_point[0] - np.amin(data[:,1]) 
    if lp_max_var > lp_min_var:
        lp_var = lp_max_var
    else:
        lp_var = lp_min_var

    print(np.var(data[:,1]))
    print(np.var(data[:,2]))

    ##: Calculating largest Omega_Lambda variance
    ol_max_var = np.amax(data[:,2]) - max_point[1]
    ol_min_var = max_point[1] - np.amin(data[:,2]) 

    if ol_max_var > ol_min_var:
        ol_var = ol_max_var
    else:
        ol_var = ol_min_var

    pyplot.contour(x, y,(x**2/lp_var**2 + y**2/ol_var**2), [5.991], colors='k')

    # Compute ellipse parameters
    a = lp_var                               # Semimajor axis
    x0 = max_point[0]                        # Center x-value
    y0 = max_point[1]                        # Center y-value
    b = ol_var                               # Semiminor axis
    phi = 0                                  # Angle betw major axis and x-axis

    # Parametric plot in t
    resolution = 1000
    t = np.linspace(0, 2*np.pi, resolution)
    x = x0 + a * np.cos(t) * np.cos(phi) - b * np.sin(t) * np.sin(phi)
    y = y0 + a * np.cos(t) * np.sin(phi) + b * np.sin(t) * np.cos(phi)
    
    pyplot.plot(x, y)

    pyplot.savefig("bayesian_statistics/ol_lp.pdf")
