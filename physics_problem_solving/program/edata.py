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

    data_file = np.delete(data_file, [0,1,2,3,4], 0) # Removing first five rows
    data_file = np.delete(data_file, [0], 1) # Removing first column
    
    data_file[:,1] = np.add(data_file[:,1], mag) # Adding magnitude to mag column

    return data_file
