import numpy as np

def data_file(data):
    """ Opening the supernova data text file and then returning: star catalogue
    data (array), v-band and b-band data taken from photometry (arrays), the name of the
    supernova (string), and the date that it was observed (string). """

    with open(data) as f:
        lines = f.readlines()

    sn_name_date = lines[1]
    sn_name_date = sn_name_date[2:] # removes the initial hash and space

    sn_name = sn_name_date.split()[0]
    sn_date = sn_name_date.split()[1]

    data_file = np.zeros(len(lines)) # Storing where locations of things are

    # For loop to find the location of where things are
    for i in range(len(lines)):
        if lines[i] == '# star catalogue objects\n':
            data_file[i] = 1
        if lines[i] == '# v-band\n':
            data_file[i] = 2
        if lines[i] == '# b-band\n':
            data_file[i] = 3
    
    # Arrays to store where the data is located in the file
    loc_1 = np.asscalar(np.where(data_file == 1)[0]) # storing loc of sc objects
    loc_2 = np.asscalar(np.where(data_file == 2)[0]) # storing loc of v-band
    loc_3 = np.asscalar(np.where(data_file == 3)[0]) # storing loc of b-band

    # Arrays to store data
    sc_data = np.zeros([loc_2-loc_1-3,5])
    v_data = np.zeros([loc_3-loc_2-4,4])
    b_data = np.copy(v_data) # creates exactly the same size array as for b_data

    sc_initial, v_initial, b_initial = [], [], [] # storing what rows the data is on

    # Copying data from text file into an array, ignoring the names of the SNs
    for i in range(len(data_file)):
        if lines[i][0].isdigit() == True:
            if i < loc_2: # for star catalogue
                if not []:
                    sc_initial.append(i) # adds current row to the list
                sc_split = lines[i].split() # splits the row of info into strings
                for k in range(5):
                    if k == 0:
                        pass
                    else:
                        sc_data[(sc_initial[-1]-5)][k] = sc_split[k] # sc data into an array
            if loc_2 < i < loc_3: # for v-band
                if not []:
                    v_initial.append(i) # adds current row to the list
                v_split = lines[i].split() # splits the row of info into strings
                for k in range(4):
                    if k == 0:
                        pass
                    else:
                        v_data[len(v_initial)-1][k] = v_split[k] # v-band data into an array
            if i > loc_3: # for b-band
                if not []:
                    b_initial.append(i) # adds current row to the list
                b_split = lines[i].split() # splits the row of info into strings
                for k in range(4):
                    if k == 0:
                        pass
                    else:
                        b_data[len(b_initial)-1][k] = b_split[k] #b-band data into an array

    return sc_data, v_data, b_data, sn_name, sn_date

def rel_mag_v(data):
    """ Returns the v-band magnitude of the supernova and it's uncertainty,
    data originally taken using photometry. """

    data = data_file(data)

    data_wol = np.delete(data[1], (-1), axis=0) # data without last row
    sn_vband = data[1][-1] # row of data of the supernova    

    v_mag = sn_vband[1] # the counts value for v band of the SN
    v_mag_err = sn_vband[2] # counts value for error of the SN

    return v_mag, v_mag_err, data_wol, data[3], data[4]

def rel_mag_b(data):
    """ Returns the b-band magnitude of the supernova and it's uncertainty,
    data originally taken using photometry. """

    data = data_file(data)

    data_wol = np.delete(data[2], (-1), axis=0) # data without last row
    sn_bband = data[2][-1] # row of data of the supernova

    b_mag = sn_bband[1] # the b band counts of the SN
    b_mag_err = sn_bband[2] # b band mag count of the SN

    return b_mag, b_mag_err, data_wol, data[3], data[4]

def data_return(data):
    """ Storing the data into a text file for easy access. """

    v_band = rel_mag_v(data)
    b_band = rel_mag_b(data)

    data = data_file(data)
    sc_data = data[0]

    print sc_data

    v_band_cal = v_band[2]
    b_band_cal = b_band[2]

    z_1_v = sc_data[0][1] + (2.5 * np.log10(v_band_cal[0][1]))
    z_2_v = sc_data[1][1] + (2.5 * np.log10(v_band_cal[1][1]))

    z_1_b = sc_data[0][2] + (2.5 * np.log10(b_band_cal[0][1]))
    z_2_b = sc_data[1][2] + (2.5 * np.log10(b_band_cal[1][1]))

    z_v_av = np.average([z_1_v, z_2_v])
    z_b_av = np.average([z_1_b, z_2_b])

    # Calculating magnitudes of v and b band
    m_v = z_v_av - (2.5 * np.log10(v_band[0]))
    m_b = z_b_av - (2.5 * np.log10(b_band[0]))

    # Calculating the uncertainties
    m_v_uncert = 2.5 * np.log10(1 + (1 / np.sqrt(v_band[0])))
    m_b_uncert = 2.5 * np.log10(1 + (1 / np.sqrt(b_band[0])))

    print m_v_uncert, m_b_uncert

    file_name = '%s-%s.txt' % (v_band[3], b_band[4])
    f = open(file_name, 'w')
    f.write('Supernova: ' + v_band[3] + '\n')
    f.write('Date of observations: ' + v_band[4] + '\n')
    f.write('b-band magnitude and error: ' + str(m_b) + " +- " + str(m_b_uncert) + '\n')
    f.write('v-band magnitude and error: ' + str(m_v) + " +- " + str(m_v_uncert) + '\n')
    f.close()


if __name__ == '__main__':

    data_return("AT2017gvb/AT2017gvb--17_10_22.txt")
