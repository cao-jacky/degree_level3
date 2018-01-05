import numpy as np

""" The name edata because extension-data, data reader for the extension phase of my 
project!"""

def data_input(file_name):
    """ Opens data file and stores it into one single array. """
    with open(file_name) as f:
        lines = f.readlines()
    f.close() # Closing reader to save memory
    num_lines = sum(1 for line in open(file_name)) # Number of lines in text file
    data_file = np.zeros([len(lines), 5]) # Creates an array to store the text file

    # For loop, stores and pulls out data
    for i in range(len(lines)):
        if "systematic" in lines[i]:
            mag_split = lines[i].split() # Pulling out the systematic magnitude
            mag = np.float64(mag_split[-1]) # Selecting magnitude string
        if i in {0,1,2,3,4}: 
            pass # Ignoring the comment rows
        else:
            line_split = lines[i].split() # Split current row in strings
            for k in range(5):
                if k == 0:
                    pass # Not bothering to store the SN name
                else:
                    data_file[i][k] = line_split[k] # storing into an array

    data_file = np.delete(data_file, [0,1,2,3,4], axis=0) # Removing first five rows
    data_file = np.delete(data_file, [0], axis=1) # Removing first column
    data_file[:,1] = np.add(data_file[:,1], mag) # Adding magnitude to mag column
    return data_file

def data_splitter(file_name):
    """ Sorts and splits the data by redshift. """
    total_file = data_input(file_name) # Calling the data
    total_file = total_file[total_file[:,0].argsort()] # Sorting by redshift

    local_sn = np.where(total_file[:,0] < 0.1)[0] # Location of local supernova, z<0.1
    split_arrays = np.split(total_file, [local_sn[-1]], axis=0) # Splitting at last z<0.1
    low_z = split_arrays[0] # Low redshift as an array
    high_z = split_arrays[1] # High redshift as an array

    low_z_0 = np.zeros([len(low_z),1])# Zeros arrays instead of names, waste of memory
    high_z_0 = np.zeros([len(high_z),1])
    
    low_z = np.append(low_z_0, low_z, axis=1) # Adding the zeros array because I'm silly
    high_z = np.append(high_z_0, high_z, axis=1) 

    np.savetxt("program/sn_high_z.txt", high_z) # Save to a text file
    np.savetxt("program/sn_low_z.txt", low_z) # Save to a text file
    return high_z, low_z
