import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib import rc

def data(sn):
    """ Reads the text files for the supernova. """

    bands = ["B", "V"]

    with open(sn) as f:
        lines = f.readlines()

    data_file = np.zeros([len(lines),4])

    for i in range(len(data_file)):
        # To find the type of data format that was used
        #print(lines[i])
        if "B    +/-" in lines[i]:
            tp = 0 # Type of data file, with +/-
        if "B	Berr" in lines[i]:
            tp = 1 # Type of data file, with err

    for i in range(len(data_file)):
        # Pulling out the data

        split = lines[i].split()
        loc_b = numpy.where
        for i in range(len(bands)):
            print(i)
        
        print(split)




if __name__ == '__main__':
    data('archive_data/sn1998dh_UBVRI.dat')
