import os
import data_copy
import galaxy_subtractor

def commands():
    sn = ['2017hhz']
    band = ['V'] # Band used in this galaxy subtraction
    files = ['171022_v_al.fits', '171123_v.fits'] 

    obj = ['512-002599'] # Object used to compare counts
    counts = [103.87, 149.53]
    
    src = '/Volumes/JACKY_CAO_H/'
    dest = '/Users/jackycao/Documents/Projects/degree_level3/laboratory_project/programs/galaxy_subtraction/' 

    for i in range(len(sn)):
        # Copying files over 
        data_copy.copy_fol(src + sn[i], dest)
        #print("Folder from data storage has been copied to this module folder. ")
    # ----------------------------------------------------------------------------#
        # Performs the galaxy subtraction
        galaxy_subtractor.saver(dest + sn[i], files, counts)

if __name__ == '__main__':
    commands()
