import data 
import l_peak
import omega_lambda
import plotter

""" Module to calculate the dark energy density, Omega_Lambda."""

pc = 3.09 * 10 ** 16 # Parsec in m
# l_sol = 3.84 * (10**26) # Luminosity of the Sun in Watts, W

file_name = 'sn_data.txt'
cm_data = [75, (3*(10**8))] # In the order [hubbles_constant (km s^-1 Mpc^-1), speed_of_light (ms^-1)]
# Convert H_0 into SI
cm_data[0] = (cm_data[0] * (10**3)) / (pc)

rnge = [0,1] # Range to test Omega_Lambda values in


data = data.data_input(file_name)

l_peak = l_peak.chi_sq_min(cm_data[0], cm_data[1], data, 100)

omega_lambda.chi_sq_min(cm_data[0], cm_data[1], data, 0.01, float(l_peak[1]))

plotter.plot_l(cm_data[0], cm_data[1], data, 100)
plotter.plot_o(cm_data[0], cm_data[1], data, 0.01, float(l_peak[1]))
plotter.plot_redmag(cm_data[0], cm_data[1], data, 0.01, float(l_peak[1]))
