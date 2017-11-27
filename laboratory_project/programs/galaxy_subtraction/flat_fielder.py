import numpy as np
import os
import subprocess
from subprocess import call

sne = ['2017hhz'] # Supernova data to flat field
obms = [10,11] # Months observed in
ptd = '/Volumes/JACKY_CAO/Laboratory_Project/data/far-east-16/' # Path to data

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

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
        dir_q = True
        call("export STARLINK_DIR=/Users/jackycao/Documents/star-2017A", shell=True)
        call("source $STARLINK_DIR/etc/profile", shell=True)
    
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
                    #print(cur_loc) 
                    if os.path.isdir(cur_loc) == True:
                        for l in range(2):
                            if l == 0:
                                # Copying B flat into B data directory for that day
                                os.system("cp " + ptd + "flats/B/flat_b_new.sdf " + 
                                        cur_loc + "/B")
                                # Making tmp directory
                                if os.path.isdir(cur_loc + "/B/tmp") == 1: 
                                    with cd(cur_loc + "/B"):
                                        os.system("cp fd*.sdf tmp")
                                        os.system("rm fd*.sdf")
                                    #os.system('div')

                                else:
                                    os.system("mkdir " + cur_loc + "/B/tmp")

                            if l == 1:
                                os.system("cp " + ptd + "flats/V/flat_v_new.sdf " + 
                                        cur_loc + "/V")
                                # Making tmp directory
                                if os.path.isdir(cur_loc + "/V/tmp") == 1:
                                    with cd(cur_loc + "/B"):
                                        os.system("cp fd*.sdf tmp")
                                        os.system("rm fd*.sdf")
                                else:
                                    os.system("mkdir " + cur_loc + "/V/tmp")

                        # Apply command

        else:
            print("Supernova does not exist, please add data.")
            return

    
    #os.system("ls /Volumes/JACKY_CAO/Laboratory_Project/data/far-east-16/" + sne[i])
    #print(ptd + sne[i] + "/17_" + str(obms[j]) + "_" + str(k+1))                

    #os.system("ls -l")
    #os.system("ls /Volumes/JACKY_CAO/Laboratory_Project/data/far-east-16/")

if __name__ == '__main__':
    de()
