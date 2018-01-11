import timeit
import datetime
start = timeit.default_timer() # Keeping track of program time
now = datetime.datetime.now()

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
rng = 10

# Running the MCMC function
dt = mcmc_simple.maximum_likelihood(efile_name, lp_arnd, ol_arnd, rng)
mcmc_simple.plotter([dt[0],dt[1]]) # Plots as a covariance plot

#---------- Saving to a text file ----------#
txt_name = "/Users/jackycao/Documents/Projects/degree_level3/physics_problem_solving/mcmc_results.txt"
f = open(txt_name, 'w')
f.write("These values were generated at this date and time: " + str(now) + '\n')
f.write("\n")
f.write("The following values were also calculated in flux space! \n")
f.write("\n")

f.write("Using a basic MCMC method we have calculated: \n")
f.write("L_peak: " + str(dt[0]) + "\n")
f.write("Omega_Lambda: " + str(dt[1]) + "\n")
f.close()

stop = timeit.default_timer()
print("Time this program took: ")
print(stop-start)
