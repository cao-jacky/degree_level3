import os
import data_copy

def commands():
    sn = ['2017hhz']

    src = '/Volumes/JACKY_CAO_H/'
    dest = '/Users/jackycao/Documents/Projects/degree_level3/laboratory_project/programs/galaxy_subtraction/' 

    for i in range(len(sn)):
        """
        # Checking if location to store galaxy subtracted images exists
        if os.path.isdir(dest + sn[i]) == True:
            print("True, can proceed to copy files into folder")
        else:
            print("False, creating folder before copying files over.")
            os.system("mkdir " + dest + sn[i])"""

        # Copying files over 
        data_copy.copy(src + sn[i], dest)
        print("Folder from data storage has been copied to this module folder. ")

if __name__ == '__main__':
    commands()
