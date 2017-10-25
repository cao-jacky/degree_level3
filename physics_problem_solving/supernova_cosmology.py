import numpy as np

""" Module to calculate the dark energy density, Omega_Lambda."""

def data_input(data):
    """ Opening supernova data text file and storing information in two different 
    arrays: distant supernova data and low redshift data. """
    with open(data) as f:
        lines = f.readlines()
        #print lines 

    num_lines = sum(1 for line in open(data)) # Number of lines in the text file

    data_file = np.zeros(len(lines)) # Array to store the location of things

    # For loop to find the where the data actually begins
    for i in range(len(lines)):
        if lines[i] == '# distant supernova data.\r\n':
            data_file[i] = 1
        if lines[i] == '# low redshift supernova data\r\n':
            data_file[i] = 2 
    
    return 

def calculate_flux():
    return b

def comoving_distances():
    return b

def luminosity_peak():
    return c


if __name__ == '__main__':

    data_input('sn_data.txt')
