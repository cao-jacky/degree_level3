import numpy as np

def data_file(data):
    """ Opening data_file and storing into a numpy array. """
    with open(data) as f:
        lines = f.readlines()

    data_file = np.zeros(len(lines))
    #print data_file
    
    sn_name_date = lines[1]
    sn_name_date = sn_name_date[2:] # removes the initial hash and space

    sn_name = sn_name_date.split()[0]
    sn_date = sn_name_date.split()[1]
    
    # For loop to find the location of where things are
    for i in range(len(lines)):
        if lines[i] == '# star catalogue objects\n':
            data_file[i] = 1
        if lines[i] == '# v-band\n':
            data_file[i] = 2
        if lines[i] == '# b-band\n':
            data_file[i] = 3

    # need to create different arrays for the data
    loc_1 = np.asscalar(np.where(data_file == 1)[0]) # storing loc of sc objects
    loc_2 = np.asscalar(np.where(data_file == 2)[0]) # storing loc of v-band
    loc_3 = np.asscalar(np.where(data_file == 3)[0]) # storing loc of b-band

    sc_data = np.zeros([loc_2-loc_1-3,5])
    v_data = np.zeros([loc_3-loc_2-4,4]) 
    b_data = np.copy(v_data) # creates exactly the same size array as for b_data
   
    sc_initial, v_initial, b_initial = [], [], [] # storing what rows the data is on

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
    data = data_file(data)

    data_wol = np.delete(data[1], (-1), axis=0) # data without last row
    sn_vband = data[1][-1] # row of data of the supernova

    vr = np.divide(data[0][:,1], data_wol[:,1]) # vmag/relative mag
    vr_av = np.average(vr) # averages all our v/r values together

    v_mag = sn_vband[1] * vr_av # the v band magnitude of the SN
    v_mag_err = sn_vband[2] * vr_av # v band mag uncertainty for SN
    
    return v_mag, v_mag_err, data[3], data[4]

def rel_mag_b(data):
    data = data_file(data)

    data_wol = np.delete(data[2], (-1), axis=0) # data without last row
    sn_bband = data[2][-1] # row of data of the supernova

    br = np.divide(data[0][:,1], data_wol[:,1]) # vmag/relative mag
    br_av = np.average(br) # averages all our v/r values together

    b_mag = sn_bband[1] * br_av # the v band magnitude of the SN
    b_mag_err = sn_bband[2] * br_av # v band mag uncertainty for SN
    
    return b_mag, b_mag_err, data[3], data[4]

def data_return(data):
    v_band = rel_mag_v(data)
    b_band = rel_mag_b(data)

    file_name = '%s-%s.txt' % (v_band[2], b_band[3])  
    f = open(file_name, 'w')
    f.write('Supernova: ' + v_band[2] + '\n')
    f.write('Date of observations: ' + v_band[3] + '\n')
    f.write('v-band magnitude and error: ' + str(v_band[0]) + " +- " + str(v_band[1]) + '\n')
    f.write('b-band magnitude and error: ' + str(b_band[0]) + " +- " + str(b_band[1]) + '\n')
    f.close()


if __name__ == '__main__':
   
    data_return("2017hhz_171023.txt")

