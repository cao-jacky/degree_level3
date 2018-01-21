import timeit
import datetime
start = timeit.default_timer() # Keeping track of program time
now = datetime.datetime.now()

import mcmc_extended_model
import mcmc_covariance_plotter

import numpy as np

efile_name = 'data/SCPUnion2.1_mu_vs_z.txt'

#---------- Simple MCMC runner ----------#

# The 'actual' values that the other program calculated
lp_true = 3.60936635 * (10**35) # L_peak 
ol_true = 0.78 # Omega_Lambda
ok_true = -0.0030 # Omega_k
om_true = 0.239 # Omega_m
orad_true = 0.000_041_6 # Omega_r

# Testing values
lp_arnd = 3.40 * (10**35)
ol_arnd = 0.80
ok_arnd = -0.0025
om_arnd = 0.2
orad_arnd = 0.000_05

# Amount of steps for the MCMC function to take - higher number, takes longer
rng = 1500

# Running the MCMC function, the number of times
no = 10

#---------- Saving to a text file ----------#
txt_name = "/Users/jackycao/Documents/Projects/degree_level3/physics_problem_solving/mcmc_extended_model_results.txt"
f = open(txt_name, 'w')
f.write("These values were generated at this date and time: " + str(now) + '\n')
f.write("\n")
f.write("The following values were also calculated in flux space! \n")
f.write("\n")

values_store = np.zeros([no,5])

ollp_store = np.zeros([no,2])

for i in range(no):
    # Running the MCMC function
    dt = mcmc_extended_model.maximum_likelihood(efile_name, lp_arnd, ol_arnd, ok_arnd, 
            om_arnd, orad_arnd, rng, i)
    values_store[i] = dt
    #mcmc_simple_model.plotter([dt[0],dt[1]], i) # Plots as a covariance plot
    
    f.write("Using a basic MCMC method we have calculated on run" + str(i) + ": \n")
    f.write("L_peak: " + str(dt[0]) + "\n")
    f.write("Omega_Lambda: " + str(dt[1]) + "\n")
    f.write("Omega_k: " + str(dt[2]) + "\n")
    f.write("Omega_m: " + str(dt[3]) + "\n")
    f.write("Omega_r: " + str(dt[4]) + "\n")
    f.write("\n")

f.write("Final average values and their uncertainties: \n")
lp_average = np.average(values_store[:,0])
ol_average = np.average(values_store[:,1])
ok_average = np.average(values_store[:,2])
om_average = np.average(values_store[:,3])
orad_average = np.average(values_store[:,4])
lp_std = np.std(values_store[:,0])
ol_std = np.std(values_store[:,1])
ok_std = np.std(values_store[:,2])
om_std = np.std(values_store[:,3])
orad_std = np.std(values_store[:,4])

f.write("L_peak: " + str(lp_average) + " +- " + str(lp_std / np.sqrt(no)) + "\n")
f.write("Omega_Lambda: " + str(ol_average) + " +- " + str(ol_std / np.sqrt(no)) + "\n")
f.write("Omega_k: " + str(ok_average) + " +- " + str(ok_std / np.sqrt(no)) + "\n")
f.write("Omega_m: " + str(om_average) + " +- " + str(om_std / np.sqrt(no)) + "\n")
f.write("Omega_r: " + str(orad_average) + " +- " + str(orad_std / np.sqrt(no)) + "\n")

f.close()

mcmc_covariance_plotter.plotter()

stop = timeit.default_timer()
print("Time this program took: ")
print(stop-start)

