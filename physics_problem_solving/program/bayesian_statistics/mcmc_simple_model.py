import numpy as np
import glob

import matplotlib
import matplotlib.pyplot as pyplot
from matplotlib.patches import Ellipse
from matplotlib import rc

import edata
import simple_model

pyplot.rc('text', usetex=True)
pyplot.rc('font', family='serif')
pyplot.rcParams['text.latex.preamble'] = [r'\boldmath']

matplotlib.rcParams['lines.color'] = 'k'
matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler('color', ['k'])

# Our parameters 
H0 = (75 /3.09) * (1.0 / (10**19)) # Hubble's constant
c = (3*(10**8)) # Speed of light in a vacuum

step = 0.01

def data(file_name):
    sn_data = edata.redshift(file_name)
    return sn_data

def error_function(file_name, lp, ol):
    dt = data(file_name)
    dt = np.concatenate((dt[0],dt[1]))
    m_mdl = np.zeros([len(dt[:,1]),1]) # Storing the model magnitudes
    #: Producing model data with the redshifts from file
    for i in range(len(dt[:,1])):
        m_mdl[i] = simple_model.model_running(H0, c, dt[:,1][i], lp, ol)

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
    ol_prpsed = np.random.normal(ol, 0.1, 1)
    lp_prpsed = np.random.normal(lp, 0.2*(10**35),1)  

    print(ol_prpsed, lp_prpsed)
    
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

def maximum_likelihood(file_name, lp, ol, rng, name):
    data = mcmc(file_name, lp, ol, rng)
    #: Saving data to a textfile to then plot
    np.savetxt("bayesian_statistics/runs_simple/data_run" + str(name) + ".txt", data)
    #np.savetxt("bayesian_statistics/data.txt", data)

    data_sorted = data[data[:,0].argsort()] # Sorting by the likelihood probability
    data_likelihood = np.where(data_sorted[:,0] < 1)[0]
    lto = data_likelihood[-1] # Last entry which is less than one, use as an index
    max_lh_row = data_sorted[lto] # Row with the maximum likelihood data
    lp_max = max_lh_row[1] # For L_peak
    ol_max = max_lh_row[2] # For Omega_Lambda
    return lp_max, ol_max

def plotter(max_point, name):
    """ Plots into a covariance plot"""
    data = np.loadtxt("bayesian_statistics/runs_simple/data_run" + str(name) + ".txt")
    x = data[:,1]
    y = data[:,2]

    cov = np.cov(x, y) # Covariance matrix

    lambda_, v = np.linalg.eig(cov)
    lambda_ = np.sqrt(lambda_)

    fig, ax = pyplot.subplots()

    for j in range(1, 4):
        ell = Ellipse(xy=(np.mean(x), np.mean(y)),
                      width=lambda_[0]*j*2, height=lambda_[1]*j*2,
                      angle=np.rad2deg(np.arccos(v[0, 0])), lw=2, edgecolor='red')
        ell.set_facecolor('none')
        ax.add_artist(ell)

    #: Labels
    #pyplot.title(r"\textbf{Covariance plot of L_{peak} and Omega_{Lambda}}")
    pyplot.xlabel(r'$L_{peak}$')
    pyplot.ylabel(r'$\Omega_{\Lambda}$')

    pyplot.tick_params(axis='y', which='major', labelsize=15)
    pyplot.tick_params(axis='x', labelsize=15)

    #: Plotting main data
    pyplot.scatter(x, y,marker=".",color="0.1")
    pyplot.scatter(3.60936635 * (10**35),0.78, marker=".", color="red")
    pyplot.scatter(max_point[0],max_point[1], marker=".", color="deepskyblue")

    pyplot.savefig("bayesian_statistics/graphs_simple/ol_lp" + str(name) + ".pdf")
    pyplot.savefig("bayesian_statistics/graphs_simple/ol_lp" + str(name) + 
            "_transparent.png", transparent=True)

def complete(points, number):
    """ Plots a single graph with all our data. """

    fnames = glob.glob("/Users/jackycao/Documents/Projects/degree_level3/physics_problem_solving/program/bayesian_statistics/runs_simple/*.txt") # Where the data files are
    arrays = [np.loadtxt(f) for f in fnames] # Loading the data
    data = np.concatenate(arrays)
    
    fig, ax = pyplot.subplots()

    #: Plotting main data
    x = data[:,1]
    y = data[:,2]

    ax.scatter(x,y, marker=".", color="0.1")

    cov = np.cov(x, y) # Covariance matrix

    lambda_, v = np.linalg.eig(cov)
    lambda_ = np.sqrt(lambda_) 

    for j in range(1, 4):
        ell = Ellipse(xy=(np.mean(x), np.mean(y)),
                      width=lambda_[0]*j*2, height=lambda_[1]*j*2,
                      angle=np.rad2deg(np.arccos(v[0, 0])), lw=2, edgecolor='red')
        ell.set_facecolor('none')
        ax.add_artist(ell)

    #: Labels
    #pyplot.title(r"\textbf{Covariance plot of L_{peak} and Omega_{Lambda}}")
    pyplot.xlabel(r'$L_{peak}$ (W)', fontsize=13)
    pyplot.ylabel(r'$\Omega_{\Lambda}$', fontsize=13)

    pyplot.tick_params(axis='y', which='major', labelsize=15)
    pyplot.tick_params(axis='x', labelsize=15)

    pyplot.scatter(3.60936635 * (10**35),0.78, marker=".", color="red")
    pyplot.scatter(points[:,0],points[:,1], marker=".", color="deepskyblue")
    pyplot.scatter(np.average(points[:,0]), np.average(points[:,1]), marker=".",
        color="limegreen")

    pyplot.savefig("bayesian_statistics/graphs_simple/ol_lp_complete.pdf")
    pyplot.savefig("bayesian_statistics/graphs_simple/ol_lp_complete_transparent.png", 
            transparent=True)



