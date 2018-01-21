import numpy as np
import glob

import edata
import extended_model

# Our parameters 
H0 = (75 /3.09) * (1.0 / (10**19)) # Hubble's constant
c = (3*(10**8)) # Speed of light in a vacuum

step = 0.01

def data(file_name):
    sn_data = edata.redshift(file_name)
    sn_data = [np.delete(sn_data[0], 4, axis=1), np.delete(sn_data[1], 4, axis=1)]
    return sn_data[0]

def error_function(file_name, lp, ol, ok, om, orad):
    dt = data(file_name)
    m_mdl = np.zeros([len(dt[:,1]),1]) # Storing the model magnitudes
    #: Producing model data with the redshifts from file
    for i in range(len(dt[:,1])):
        m_mdl[i] = extended_model.model(H0, c, dt[:,1][i], lp, ol, ok, om, orad)

    # Joining data and model values array
    total_data = np.concatenate((dt,m_mdl), axis=1)

    # Chi^2: (data-model)**2/(error**2)
    chi_sq = ((total_data[:,2] - total_data[:,4])**2) / (total_data[:,3]**2)
    total_chi_sq = np.sum(chi_sq) # Sums all the values together
    return total_chi_sq

def likelihood_ratio(chi_sq_crrnt, chi_sq_prpsed):
    return np.exp(- chi_sq_prpsed + chi_sq_crrnt)

def current_values(file_name, lp, ol, ok, om, orad):
    chi_sq_crrnt = error_function(file_name, lp, ol, ok, om, orad) / 2 # Current chi^2

    #: Proposed values for new Omega_Lambda and L_peak
    ol_prpsed = np.random.normal(ol, 0.15, 1)
    lp_prpsed = np.random.normal(lp, 0.25*(10**35), 1)
    ok_prpsed = np.random.normal(ok, 0.002, 1)
    om_prpsed = np.random.normal(om, 0.1, 1)
    orad_prpsed = np.random.normal(orad, 0.000_02, 1)
    print(ol_prpsed,lp_prpsed,ok_prpsed,om_prpsed,orad_prpsed)
    if ol_prpsed > 1.0:
        ol_prpsed = np.random.normal(ol, 0.15, 1)

    chi_sq_prpsed = error_function(file_name, lp_prpsed, ol_prpsed, ok_prpsed, om_prpsed,
             orad_prpsed) / 2 # Proposed chi^2

    ratio = likelihood_ratio(chi_sq_crrnt, chi_sq_prpsed) # Calcualting the ratio
    return ratio, lp_prpsed, ol_prpsed, ok_prpsed, om_prpsed, orad_prpsed

def mcmc(file_name, lp, ol, ok, om, orad, rng):
    values = np.zeros([rng, 6]) # Storing all our values

    for i in range(len(values)):
        lp_n = lp
        ol_n = ol
        ok_n = ok
        om_n = om
        orad_n = orad

        if i == 0:
            values[i][1] = lp
            values[i][2] = ol
            values[i][3] = ok
            values[i][4] = om
            values[i][5] = orad
        else:
            ratio_value = current_values(file_name,lp_n,ol_n,ok_n,om_n,orad_n)
            values[i][0] = ratio_value[0]
            values[i][1] = ratio_value[1]
            values[i][2] = ratio_value[2]
            values[i][3] = ratio_value[3]
            values[i][4] = ratio_value[4]
            values[i][5] = ratio_value[5]
            if ratio_value[0] > np.random.rand(1):
                lp = ratio_value[1]
                ol = ratio_value[2]
                ok = ratio_value[3]
                om = ratio_value[4]
                orad = ratio_value[5]
            else:
                lp = lp
                ol = ol
                ok = ok 
                om = om
                orad = orad
    return values

def maximum_likelihood(file_name, lp, ol, ok, om, orad, rng, name):
    data = mcmc(file_name, lp, ol, ok, om, orad, rng)
    #: Saving data to a textfile to then plot
    np.savetxt("runs_extended/data_run" + str(name) + ".txt", data)
    #np.savetxt("bayesian_statistics/data.txt", data)

    data_sorted = data[data[:,0].argsort()] # Sorting by the likelihood probability
    data_likelihood = np.where(data_sorted[:,0] < 1)[0]
    lto = data_likelihood[-1] # Last entry which is less than one, use as an index
    max_lh_row = data_sorted[lto] # Row with the maximum likelihood data
    lp_max = max_lh_row[1] # For L_peak
    ol_max = max_lh_row[2] # For Omega_Lambda
    ok_max = max_lh_row[3]
    om_max = max_lh_row[4]
    orad_max = max_lh_row[5]
    return lp_max, ol_max, ok_max, om_max, orad_max
