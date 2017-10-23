import numpy as np

def data_file(data):
    """ Opening data_file and storing into a numpy array. """
    with open(data) as f:
        lines = f.readlines()
        print lines

    data_file = np.zeros(len(lines))
    print data_file
    
    sn_name = lines[1]
    print sn_name

    for i in range(len(lines)):
        cmmt = 0 # to see if there was a comment before
        if lines[i] == '# star catalogue objects\n':
            data_file[i] = 1
        if lines[i] == '# v-band\n':
            data_file[i] = 2
        if lines[i] == '# b-band\n':
            data_file[i] = 3

    # need to create different arrays for the data
    loc_1 = np.asscalar(np.where(data_file == 1)[0])
    loc_2 = np.asscalar(np.where(data_file == 2)[0])
    loc_3 = np.asscalar(np.where(data_file == 3)[0])

    print loc_1,loc_2,loc_3

    sc_data = np.zeros([loc_2-loc_1-3,5])
    v_data = np.zeros([loc_3-loc_2-4,4])
    print v_data

    sc_data[0][0] = 1
    sc_data[1][0] = 2

    sc_no = 0 # required so that I can keep count of how what element to access 
    
    for i in range(len(data_file)):
        if lines[i][0].isdigit() == True:
            sc_no += 1
            if i < loc_2: # for star catalogue
                sc_no = sc_no -1 
                sc_split = lines[i].split()
                print "huh, ", sc_split[sc_no]
                #print sc_data[sc_no]
                sc_data[sc_no][0] = sc_split[sc_no]
                """
                for i in range(5):
                    if i == 1:
                        sc_data[i] = sc_split[i]
                    else:
                        sc_data[i] = sc_split[i]"""
            if loc_2 < i < loc_3: # for v-band
                print lines[i].split()
            if i > loc_3: # for b-band
                print lines[i].split()   

    print sc_data
    
if __name__ == '__main__':
   
    data_file("2017hhz_171020.txt")
