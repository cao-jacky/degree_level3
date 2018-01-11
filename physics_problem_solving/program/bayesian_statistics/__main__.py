import timeit
start = timeit.default_timer() # Keeping track of program time

import mcmc_simple

efile_name = 'data/SCPUnion2.1_mu_vs_z.txt'

#---------- Simple MCMC runner ----------#

# The 'actual' values that the other program calculated
lp_true = 3.60936635 * (10**35) # L_peak 
ol_true = 0.78 #Omega_Lambda

# Testing values
lp_arnd = 3.40 * (10**35)
ol_arnd = 0.80

# Amount of steps for the MCMC function to take - higher number, takes longer
rng = 1500

# Running the MCMC function
dt = mcmc_simple.maximum_likelihood(efile_name, lp_arnd, ol_arnd, rng)
mcmc_simple.plotter() # Plots as a covariance plot

#---------- Saving to a text file ----------#

stop = timeit.default_timer()
print("Time this program took: ")
print(stop-start)
