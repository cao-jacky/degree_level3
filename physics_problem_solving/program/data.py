from __future__ import division
import numpy as np

def data_input(data):
    """ Opening supernova data text file and storing information in two different 
    arrays: distant supernova data and low redshift data. """
    with open(data) as f:
        lines = f.readlines()
        #print(lines)
    f.close()
    num_lines = sum(1 for line in open(data)) # Number of lines in the text file
    data_file = np.zeros(len(lines)) # Array to store the location of things

    # For loop to find the where the data actually begins
    for i in range(len(lines)):
        if lines[i] == '# distant supernova data.\n':
            data_file[i] = 1
        if lines[i] == '# low redshift supernova data\n':
            data_file[i] = 2 

    # Arrays to store where the data is in the file
    dsn_loc = np.asscalar(np.where(data_file == 1)[0]) # Storing location of distance SNs
    lzsn_loc = np.asscalar(np.where(data_file == 2)[0]) # Storing location of low z SNs

    # Arrays to store the two sets of data
    dsn_data = np.zeros([lzsn_loc-dsn_loc-3,4])
    lzsn_data = np.zeros([num_lines-lzsn_loc-2,4])

    # Storing what rows the data is in
    dsn_initial, lzsn_initial = [], []

    # Copying data from text file into an array, bar the names of the SNs
    for i in range(len(data_file)):
        if lines[i][0].isdigit() == True:
            if i < lzsn_loc: # For distant supernovae data
                if not []:
                    dsn_initial.append(i) # Adds current row to the list
                dsn_split = lines[i].split() # Splits current info line into strings
                for k in range(4):
                    if k == 0:
                        pass
                    else:
                        dsn_data[(dsn_initial[-1]-2)][k] = dsn_split[k]
            if lzsn_loc < i <num_lines: # For low redshift supernovae data
                if not []:
                    lzsn_initial.append(i) # Adds current row to the list
                lzsn_split = lines[i].split() # Splits current line into strings
                for k in range(4):
                    if k == 0:
                        pass
                    else:
                        lzsn_data[len(lzsn_initial)-1][k] = lzsn_split[k]
    
    dsn_data = dsn_data[:,1:] # Removing first column
    lzsn_data = lzsn_data[:,1:] # Removing first column

    # Storing the names of the SN in a separate array
    dsn_names = np.zeros([lzsn_loc-dsn_loc-3,1],dtype='object')
    lzsn_names = np.zeros([num_lines-lzsn_loc-2,1],dtype='object')

    # Creating name array
    for i in range(len(dsn_initial)): # For dsn data 
        j = dsn_initial[i] # Accessing the location of the data
        sn_name = lines[j].split()[0]
        dsn_names[i] = sn_name 
    for i in range(len(lzsn_initial)): # For lzsn data
        k = lzsn_initial[i] # Accessing location of the data
        sn_name = lines[k].split()[0]
        lzsn_names[i] = sn_name

    # Joining name and data arrays together
    dsn_data = np.append(dsn_names, dsn_data, axis=1)
    lzsn_data = np.append(lzsn_names, lzsn_data, axis=1)

    return dsn_data, lzsn_data, dsn_names, lzsn_names
