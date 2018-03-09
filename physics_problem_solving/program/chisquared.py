import numpy as np
import edata

""" Quick program to calculate chi_squared between our two models and data. """

# Calling experimental data
data_name = 'data/SCPUnion2.1_AllSNe.tex'
data = edata.redshift(data_name)
data = np.concatenate((data[1],data[0]),axis=0)
data = data[data[:,2].argsort()]

mdl_one = np.loadtxt('graphs/hubble/model_one.txt')
mdl_two = np.loadtxt('graphs/hubble/model_two.txt')

mdl_one = np.loadtxt('lcdm_model.txt')

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]

def chisq_one():
    """ Chi squared for model one. """
    mdl_one_store = np.zeros([len(mdl_one),3]) # Storing difference in model and observed

    for i in range(len(mdl_one)):
        nrst = find_nearest(data[:,2], mdl_one[i])
        mdl_one_store[i][0] = nrst

    for i in range(len(mdl_one_store)):
        mdone_loc = np.where(data[:,2] == mdl_one_store[i][0])[0][0]
        mdl_one_store[i][1] = mdone_loc

    mdl_one_mags = mdl_one_store[:,0].flatten()

    for i in range(len(mdl_one_store[:,1])):
        one_index = int(mdl_one_store[i][1])
        mdl_one_uncert = data[one_index][3]
        mdl_one_store[i][2] = mdl_one_uncert 

    mdl_one_diff = mdl_one_mags - mdl_one
    mdl_one_chisqall = (mdl_one_diff)**2 / (mdl_one_store[:,2])**2
    mdl_one_chisq = np.sum(mdl_one_chisqall) / len(mdl_one) 
    return mdl_one_chisq

def chisq_two():
    """ Chi squared for model two. """
    mdl_two_store = np.zeros([len(mdl_two),3]) # Storing difference in model and observed

    for i in range(len(mdl_two)):
        nrst = find_nearest(data[:,2], mdl_two[i])
        mdl_two_store[i][0] = nrst

    for i in range(len(mdl_two_store)):
        mdtwo_loc = np.where(data[:,2] == mdl_two_store[i][0])[0][0]
        mdl_two_store[i][1] = mdtwo_loc

    mdl_two_mags = mdl_two_store[:,0].flatten()

    for i in range(len(mdl_two_store[:,1])):
        two_index = int(mdl_two_store[i][1])
        mdl_two_uncert = data[two_index][3]
        mdl_two_store[i][2] = mdl_two_uncert 

    mdl_two_diff = mdl_two_mags - mdl_two
    mdl_two_chisqall = (mdl_two_diff)**2 / (mdl_two_store[:,2])**2
    mdl_two_chisq = np.sum(mdl_two_chisqall) / len(mdl_two) 
    return mdl_two_chisq

one = chisq_one()
two = chisq_two()

print(one,two)
print((two-one)/one * 100)

