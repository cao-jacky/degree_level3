import numpy as np
import os

sne = ['2017hhz'] # Supernova data to flat field
obms = [10,11] # Months observed in
ptd = '/Volumes/JACKY_CAO/Laboratory_Project/data/far-east-16/' # Path to data

def de():
    """ Function to check where the data exists, and then to copy the correct flat 
    fields.  """

    dwd = [] # List to store which days have data

    for i in range(len(sne)):
        # Checking if folder to the data exists
        if os.path.isdir(ptd + sne[i]) == True:
            pass
        else:
            pass

    if os.path.isdir("/Users/jackycao") == True:
        # Checking if on my Mac or not
        os.system("export STARLINK_DIR=/Users/jackycao/Documents/star-2017A")
        os.system("source $STARLINK_DIR/etc/profile")

    print(type(str(obms[0])), type(sne[0]))
    
    for i in range(len(sne)):
        if os.path.isdir(ptd + sne[i]) == True:
            for j in range(len(obms)):
                for k in range(31):
                    if (k+1) < 10:
                        # Account for single digits in the day of the dates: 17_11_05
                        cur_loc = ptd + sne[i] + "/17_" + str(obms[j]) + "_0" + str(k+1)
                    else: 
                        cur_loc = ptd + sne[i] + "/17_" + str(obms[j]) + "_" + str(k+1)
                    if os.path.isdir(cur_loc) == True:
                        for l in range(2):
                            if l == 0:
                                # Copying B flat into B data directory for that day
                                os.system("cp " + ptd + "flats/B/flat_b_new.sdf " + 
                                        cur_loc + "/B")

                            if l == 1:
                                os.system("cp " + ptd + "flats/V/flat_v_new.sdf " + 
                                        cur_loc + "/V")

                        
                            #os.system("cp " + cur_loc)
                            print(cur_loc)
                            print("True")
                    
                    

        else:
            print("Supernova does not exist, please add data.")
            return

    
    #os.system("ls /Volumes/JACKY_CAO/Laboratory_Project/data/far-east-16/" + sne[i])
    #print(ptd + sne[i] + "/17_" + str(obms[j]) + "_" + str(k+1))                

    #os.system("ls -l")
    #os.system("ls /Volumes/JACKY_CAO/Laboratory_Project/data/far-east-16/")

if __name__ == '__main__':
    de()
