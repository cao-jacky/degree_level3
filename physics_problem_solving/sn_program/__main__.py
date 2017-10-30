import data 
import l_peak

""" Module to calculate the dark energy density, Omega_Lambda."""

file_name = 'sn_data.txt'
cm_data = [75, (3*(10**8))] # In the order [hubbles_constant (km s^-1 Mpc^-1), speed_of_light (ms^-1)]

data = data.data_input(file_name)
l_peak.luminosity_peak(cm_data[0], cm_data[1], data)
