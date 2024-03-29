import numpy as np

""" The name edata because extension-data, data reader for the extension phase of my 
project!"""

def data_input(file_name):
    """ Opens data .tex file and reads and stores into array. """
    with open(file_name, 'r') as f:
        lines = f.readlines()
    f.close() 
    num_lines = sum(1 for line in open(file_name)) # Number of lines in text file
    data_file = np.zeros([len(lines), 4])

    # For loop, stores and pulls out data
    for i in range(len(lines)):
        line_split = lines[i].split('&') # Split current row in strings
        for k in range(9):
            if k in {0,3,4,5,6,7,8}:
                pass # Not bothering to store the SN name
            else:
                if k == 1:
                    data_file[i][1] = line_split[k] # storing into an array
                elif k == 2:
                    if "nodata" in line_split[k]:
                        pass
                    else:
                        #: Finding mag and it's uncertainty from the file
                        mag = line_split[k].split('(')
                        mag_uncert = line_split[k].split('(', 1)[1].split(')')[0]

                        #: Storing our data
                        data_file[i][2] = mag[0]
                        data_file[i][3] = mag_uncert

    zero_rows = np.where(data_file[:,2] == 0) # Finding where zero mags are
    data_file = np.delete(data_file, zero_rows, axis=0) # Removing first five rows
    data_file = np.delete(data_file, [0], axis=1) # Removing first column
    return data_file

def redshift(file_name):
    """ Sorts and splits the data by redshift. """
    total_file = data_input(file_name) # Calling the data
    total_file = total_file[total_file[:,0].argsort()] # Sorting by redshift

    local_sn = np.where(total_file[:,0] < 0.1)[0] # Location of local supernova, z<0.1
    split_arrays = np.split(total_file, [local_sn[-1]], axis=0) # Splitting at last z<0.1
    low_z = split_arrays[0] # Low redshift as an array
    high_z = split_arrays[1] # High redshift as an array

    low_z_0 = np.zeros([len(low_z),1]) # Zeros arrays instead of names, waste of memory
    high_z_0 = np.zeros([len(high_z),1])
    
    low_z = np.append(low_z_0, low_z, axis=1) # Adding the zeros array because I'm silly
    high_z = np.append(high_z_0, high_z, axis=1) 

    #np.savetxt("program/sn_high_z.txt", high_z) # Save to a text file
    #np.savetxt("program/sn_low_z.txt", low_z) # Save to a text file
    return high_z, low_z





