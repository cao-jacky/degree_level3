import numpy as np
import matplotlib.pyplot as pyplot
from matplotlib import rc
import glob

pyplot.rc('text', usetex=True)
pyplot.rc('font', family='serif')
pyplot.rcParams['text.latex.preamble'] = [r'\boldmath']

def data_location():
    """ Finding all the supernova data files and outputs into a list"""
    path = "/Users/jackycao/Documents/Projects/degree_level3/laboratory_project/programs/light_curves/archive_data" # Dat files to go over
    return glob.glob(path + "/*.dat")

def data(sn):
    """ Reads the text files for the supernova and stores. """    
    with open(sn) as f:
        lines = f.readlines()

    for i in range(len(lines)):
        # To find the type of data format that was used
        split1 = lines[i].split() # Splitting the line up
        if "B" in lines[i]:
            tp = 0 # Type of data file, with +/-
            loc_b = split1.index('B')
            loc_v = split1.index('V')
        if "B     Berr" in lines[i]:
            tp = 1 # Type of data file, with err
            loc_b = split1.index('B')
            loc_v = split1.index('V')

    data_file = np.zeros([len(lines),len(split1)]) # Storing all our data

    for i in range(len(data_file)):
        # Pulling out the data
        if lines[i][0].isdigit() == True:
            split = lines[i].split()
            for k in range(np.shape(data_file)[1]):
                if k == 0:
                    data_file[i][k] = split[k]
                else:
                    data_file[i][k] = split[k]

    fc = data_file[:,0] # First column
    zlocs = np.where([fc == 0])# Locations for zeros
    data_file = np.delete(data_file, zlocs[1], axis=0) # Deleting zeros from array
    
    # Selecting out all our data
    data_b = data_file[:,loc_b]
    data_b_err = data_file[:,loc_b+1]
    data_v = data_file[:,loc_v]
    data_v_err = data_file[:,loc_v+1]

    data_bv = np.column_stack([data_file[:,0], data_b, 
        data_b_err, data_v, data_v_err]) # Final data

    return data_bv

def models():
    """ Model data to plot. """
    model_b = 1.0
    model_v = 1.0

    # Template for B 
    with open("data/b_model.dat") as g:
        DataInModelLinesB = g.readlines()

    data_in_model_B = np.zeros([len(DataInModelLinesB),2]) # Create storage array

    for i in range(len(data_in_model_B)):
        if i in {0,1}:
            pass # Ignore first rows from files
        else:
            split = DataInModelLinesB[i].split()
            for k in range(2):
                if k == 0:
                    split[k] = split[k].replace(",", "") # Removing commas
                data_in_model_B[i][k] = split[k] # Storing into array
    
    model_b = np.delete(data_in_model_B, [0,1], axis=0) # Delete comment rows


    return model_b, model_v

def plot():
    sn = data_location() # List of supernovae

    fig1 = pyplot.figure()
    #fig1.gca().invert_yaxis()

    # x- and y- axis limits
    pyplot.xlim((-20,90))
    pyplot.ylim((20,13))

    pyplot.xlabel(r'\textbf{Days Since Peak Magnitude}', fontsize=13)
    pyplot.ylabel(r'\textbf{Absolute Magnitude}', fontsize=15)

    pyplot.tick_params(axis='y', which='major', labelsize=15)
    pyplot.tick_params(axis='x', labelsize=15)

    tr = 49_685 # Translation factor

    for i in range(len(sn)):
        sne = sn[i] # The supernova currently being used
        dt = data(sne) # Data
        if i == 0:
            pyplot.scatter(dt[:,0]-tr, dt[:,1], color='grey', marker='.') # Plotting B band data
            pyplot.scatter(dt[:,0]-tr, dt[:,3]+3, color='0.1', marker='.') # Plotting V band data
        if i == 1:
            pyplot.scatter(dt[:,0]+168-tr, dt[:,1]-1.6, color='grey', marker='.') # Plotting B band data
            pyplot.scatter(dt[:,0]+165-tr, dt[:,3]+1.3, color='0.1', marker='.') # Plotting V band data
        if i == 2:
            pyplot.scatter(dt[:,0]-401-tr, dt[:,1]-4, color='grey', marker='.')
            pyplot.scatter(dt[:,0]-401-tr, dt[:,3]-0.4, color='0.1', marker='.')
        if i == 3:
            pyplot.scatter(dt[:,0]-701-tr, dt[:,1]-3, color='grey', marker='.')
            pyplot.scatter(dt[:,0]-702-tr, dt[:,3]+0.3, color='0.1', marker='.')
        if i == 4:
            pyplot.scatter(dt[:,0]+48_755-tr, dt[:,1]+0.8, color='grey', marker='.')
            pyplot.scatter(dt[:,0]+48_755-tr, dt[:,3]+3.6, color='0.1', marker='.')
    
    pyplot.savefig("graphs/typeia.pdf")



if __name__ == '__main__':
    plot()
