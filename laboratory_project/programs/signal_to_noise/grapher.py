import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib import rc

pyplot.rc('text', usetex=True)
pyplot.rc('font', family='serif')
pyplot.rcParams['text.latex.preamble'] = [r'\boldmath']

def data():
    """ Reads the data file and outputs into a numpy array without any calculation. """

    data_in = "2017hhz.txt"
    with open(data_in) as f:
        data_in_line = f.readlines()
    data_raw = np.zeros([len(data_in_line),3]) # Creates array the same size as file
    
    for i in range(len(data_in_line)):
        if i in {0}:
            pass
        else:
            split = data_in_line[i].split()
            for k in range(3):
                data_raw[i][k] = split[k]

    data_raw = np.delete(data_raw, 0, axis=0)
    return data_raw

def calculations():
    """ Performs calculations to get signal-to-noise values. """

    dt = data()

    new_data = np.zeros([len(dt),2]) # Storing radius and S/N value
    
    for i in range(len(dt)):
        curr_row = dt[i] # Pulling current row
        curr_sig = curr_row[1] # Pulling current number of counts
        curr_rad = curr_row[0] # Pulling current radius
        curr_sky = curr_row[2] # Pulling current sky
    
        area = np.pi * (curr_rad ** 2) # The area of the aperture
        sky = curr_sky * area # Counts in that sky area

        s_n = curr_sig / np.sqrt(curr_sig + sky) # The singal to noise value

        new_data[i][0] = curr_rad # Storing radius
        new_data[i][1] = s_n # Storing signal to noise

    new_data = np.delete(new_data, [10,11,12,13,14,15,16,17,18,19], axis=0)
    return new_data

def plot():
    dt = calculations()

    fig1 = pyplot.figure(figsize=(5.3, 3))

    pyplot.xlabel(r'\textbf{Radius of the aperture (pixels)}', fontsize=13)
    pyplot.ylabel(r'\textbf{S/N}', fontsize=15)

    pyplot.tick_params(axis='y', which='major', labelsize=15)
    pyplot.tick_params(axis='x', labelsize=15)

    pyplot.xticks(np.arange(0, 21, 1))

    pyplot.plot(dt[:,0], dt[:,1], color='0.1')
    pyplot.savefig("2017hhz.pdf")

if __name__ == '__main__':
    plot()

