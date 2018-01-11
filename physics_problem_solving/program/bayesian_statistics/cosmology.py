import numpy as np
from scipy.integrate import quad
import scipy.optimize as op

import matplotlib.pyplot as pyplot
from matplotlib import rc

import emcee
import corner

import edata

pyplot.rc('text', usetex=True)
pyplot.rc('font', family='serif')
pyplot.rcParams['text.latex.preamble'] = [r'\boldmath']

# Choosing the 'true' parameters 
H0_true = (75 /3.09) * (1.0 / (10**19)) # Hubble's constant
c_true = (3*(10**8)) # Speed of light in a vacuum
lp_true = 2.92936635 * (10**35) # L_peak 
ol_true = 0.82 #Omega_Lambda

step = 0.01

efile_name = 'data/SCPUnion2.1_mu_vs_z.txt'

def data():
    sn_data = edata.redshift(efile_name)
    sn_data = [np.delete(sn_data[0], 4, axis=1), np.delete(sn_data[1], 4, axis=1)]
    return sn_data

def com_integral(x, ol):
    """ The integral required to find the comoving distance, with: 
        x - our variable
        ol - Value of Omega_Lambda being changed from two limits """
    z1 = (1 + x) ** 3 # Part of the integral
    B = ol * (z1 - 1) # Another part of the integral
    return 1.0 / ( (z1 - B) ** 0.5 ) 

def m_function(H0, c, z, lp, ol):
    """ Function to calculate magnitude for a given redshift. """
    m_0 = -20.45 
    val_n = lp # Numerator of fraction
    cmv = quad(com_integral, 0, z, args=(ol))
    cmv = (c / H0) * cmv[0]
    val_d = 4 * np.pi * (cmv**2) * ((1+z)**2) # Denominator of fraction
    frac = val_n / val_d # Calculating the fraction
    return m_0 - (2.5 * np.log10(frac))

def model(H0, c, z, lp, ol):
    """ Our model"""  
    m = m_function(H0, c, z, lp, ol)
    return m

# Model data
z = np.linspace(0, 1.5, num=150) # Generating redshift values to plot agianst
model_one = np.zeros([len(z),1]) # Storing magnitudes for model_1, milestone
for i in range(len(z)):
    model_one[i] = model(H0_true, c_true, z[i], lp_true, ol_true)

# Actual data
z_ac = data()[0][:,1]
m_ac = data()[0][:,2]
m_err_ac = data()[0][:,3]
 
fig = pyplot.figure()
pyplot.title(r"\textbf{Magnitude agaisnt Redshift}")
pyplot.xlabel(r'$z$')
pyplot.ylabel(r'\textbf{mag}')

dt = data(); odt = dt[0]; edt = dt[1]
pyplot.errorbar(edt[:,1],edt[:,2],yerr=edt[:,3],marker=".",color="0.1",
        elinewidth=0.5,linestyle="None", alpha=0.5)
pyplot.errorbar(edt[:,1],edt[:,2],yerr=edt[:,3],marker=".",color="0.1",
        elinewidth=0.5,linestyle="None", alpha=0.5)
pyplot.errorbar(odt[:,1],odt[:,2],yerr=odt[:,3],marker=".",color="grey",
        elinewidth=0.5,linestyle="None", alpha=0.5)
pyplot.errorbar(odt[:,1],odt[:,2],yerr=odt[:,3],marker=".",color="grey",
        elinewidth=0.5,linestyle="None", alpha=0.5)

pyplot.plot(z, model_one, color="red")
pyplot.savefig('hubble_diagram.pdf')

def like(theta, z, m, merr):
    """ Likelihood function. """
    lp, ol = theta
    m_model = model(H0_true, c_true, z, lp, ol) # The model
    exp_fact = 1 / (np.sqrt(2 * np.pi) * merr)# Factor multiplying the exponential
    exp_term = -0.5 * ((m-m_model)**2) / (merr**2)# Term inside exponential
    return exp_fact * np.exp(exp_term)

def running_like(theta):
    """ To ignore nan's. """
    lp, ol = theta
    for i in range(len(z_ac)):
        value = like(theta, z_ac[i], m_ac[i], m_err_ac[i])
        print(value)

#running_like([lp_true, ol_true])

#test = like([lp_true, ol_true], 0.458, 23.11, 0.46)
#print(test)

#test2 = model(H0_true, c_true, 0.458, lp_true, ol_true)
#print(test2)

#test3 = like([lp_true, ol_true], z_ac, m_ac, m_err_ac)
#print(test3)


lp_ol_list = []


nll = lambda *args: -like(*args)
for i in range(len(z_ac)):
    result = op.minimize(nll, [lp_true, ol_true], args=(z_ac[i], m_ac[i], m_err_ac[i]))
    lp_ml, ol_ml = result["x"]
    lp_ol_list.append(result["x"])

def prior(theta):
    lp, ol = theta
    if (2.8*(10**35)) < lp < (3.2*(10**35)) and 0.6 < ol < 0.9: 
        return 0.0
    return -np.inf

def prob(theta, z, m, merr):
    lp = prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + like(theta, z, m, merr)

ndim, nwalkers = 2, 100
pos = [result["x"] + 1e-4*np.random.randn(ndim) for i in range(nwalkers)]
sampler = emcee.EnsembleSampler(nwalkers, ndim, prob, args=(z_ac, m_ac, m_err_ac))
print(sampler)
sampler.run_mcmc(pos, 500)

samples = sampler.chain[:, 50:, :].reshape((-1, ndim))

fig = corner.corner(samples, labels=["$lp$", "$ol$"], truths=[lp_true, ol_true])
fig.savefig("triangle.png")

