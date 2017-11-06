import data 
import l_peak
import omega_lambda
import plotter

""" Module to calculate the dark energy density, Omega_Lambda."""

pc = 3.09 * 10 ** 16 # Parsec in m

file_name = 'sn_data.txt'
cm_data = [75, (3*(10**8))] # In the order [hubbles_constant (km s^-1 Mpc^-1), speed_of_light (ms^-1)]
# Convert H_0 into SI
cm_data[0] = (cm_data[0] * (10**3)) / (pc)

data = data.data_input(file_name)
l_peak.flux_uncertainty(data)
l_peak = l_peak.chi_sq_one(cm_data[0], cm_data[1], data, 100)
#omega_lambda.flux_obs(cm_data[0], cm_data[1], data, l_peak)

plotter.plot(cm_data[0], cm_data[1], data, 100)
