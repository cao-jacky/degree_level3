import numpy as np
import sys
sys.path.insert(0, '/Users/jackycao/Documents/Projects/degree_level3/laboratory_project/programs/templated_light_curves')

import plotter # Importing plotter program which has a function wcih reads data

""" TO CHANGE BETWEEN 2017hhz and 2017hle, YOU MUST CHANGE 0.1 TO 0.8, OR VICE-VERSA!"""

def data():
    """ Returns data from our plotter module. """
    sn = ['2017hhz']
    return plotter.data(sn[0])

def chi_sq_data_b():
    """ Returns data to use to calculate B band chi^2 Hopefully. """
    dt = data()
    
    # Specifing models and data
    b_model = dt[1] 
    b_data = dt[0]
    v_model = dt[3]
    v_data = dt[2]
    
    t_min, t_max = b_data[0][0], b_data[-1][0] # Minimum and maximum time
    to_use = np.zeros([b_data.shape[0],3]) # Array to store information 
    model_store = np.zeros([int(t_max - t_min + 1), 2])
    
    bm_count = -1 # If in the range below, blue model

    for i in range(b_model.shape[0]):
        time = b_model[i][0] # Pulling times from time column 
        if t_min + 0.1 <= time <= t_max + 0.1:
            bm_count = bm_count + 1
            t_loc = np.where(b_model[:,0] == time)# Finding location of the time
            mag_model = b_model[:,1][t_loc] # Model magnitude
            model_store[bm_count][0] = time - 0.1 # Storing time
            model_store[bm_count][1] = mag_model # Storing magnitude
        else:
            pass

    for i in range(b_data.shape[0]):
        time = b_data[i][0]
        td_loc = np.where(model_store[:,0] == time) # Location of corresponding time in model data
        tm_mag = model_store[td_loc][0][1] # Pulling out model magnitude
        to_use[i][0] = tm_mag # Storing model mag in array
        to_use[i][1] = b_data[i][1] # Storing data mag in array
        to_use[i][2] = b_data[i][2] # Storing error into array
    return to_use

def chi_sq_b():
    """ Calculating chi_squared for B magnitude. """
    dt = chi_sq_data_b()

    subt = dt[:,0] - dt[:,1] # Subtraction
    err = dt[:,2] # Uncertainty of data

    chi_sq = (subt ** 2) / (err**2)
    chi_sq = np.sum(chi_sq)
    return chi_sq

def chi_sq_data_v():
    """ Returns data to use to calculate V band chi^2 Hopefully. """
    dt = data()
    
    # Specifing models and data
    v_model = dt[3]
    v_data = dt[2]
    
    t_min, t_max = v_data[0][0], v_data[-1][0] # Minimum and maximum time
    to_use = np.zeros([v_data.shape[0],3]) # Array to store information 
    model_store = np.zeros([int(t_max - t_min + 1), 2])
    
    vm_count = -1 # If in the range below, blue model

    for i in range(v_model.shape[0]):
        time = v_model[i][0] # Pulling times from time column 
        if t_min + 0.1 <= time <= t_max + 0.1:
            vm_count = vm_count + 1
            t_loc = np.where(v_model[:,0] == time)# Finding location of the time
            mag_model = v_model[:,1][t_loc] # Model magnitude
            model_store[vm_count][0] = time - 0.1 # Storing time
            model_store[vm_count][1] = mag_model # Storing magnitude
        else:
            pass

    for i in range(v_data.shape[0]):
        time = v_data[i][0]
        td_loc = np.where(model_store[:,0] == time) # Location of corresponding time in model data
        tm_mag = model_store[td_loc][0][1] # Pulling out model magnitude
        to_use[i][0] = tm_mag # Storing model mag in array
        to_use[i][1] = v_data[i][1] # Storing data mag in array
        to_use[i][2] = v_data[i][2] # Storing error into array
    return to_use

def chi_sq_v():
    """ Calculating chi_squared for B magnitude. """
    dt = chi_sq_data_v()

    subt = dt[:,0] - dt[:,1] # Subtraction
    err = dt[:,2] # Uncertainty of data

    chi_sq = (subt ** 2) / (err**2)
    chi_sq = np.sum(chi_sq)
    return chi_sq

def final_chisq():
    b = chi_sq_b() 
    v = chi_sq_v()

    print("normal chi^2:")
    print("B: ", b)
    print("V: ", v) 
    print("\n")
    print("reduced chi^2:")
    print("B: ", b / (10-4))
    print("V: ", v / (10-4))


if __name__ == '__main__':
    final_chisq()
