import logging
import numpy as np
import os 

""" Not an elegant program, but it works"""

# Stuff to log the whole process
LOG_FILENAME = 'data_copy.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')

# Telescope data location on remote server
p5 = "/remote/archive/pt5m/2017/"
e14 = "/remote/archive/West-14/2017/"
w14 = "/remote/archive/East-14/2017/"

# Required Information
date = "17_10_19"
objt = "AT2017bvm"

source = p5 + date + "/" # Format: telescope + date + "/"
destination = "/home/"


def files(limit1, limit2):
    logging.info('files fn: Finding all the required data files')
    f = open('data_files.txt', 'w')
    for i in range((limit2+1)-limit1):
        f.write(('dbr' + str(i) + '.fits' + '\n'))
    logging.info('files fn: Finished finding data, exported into data_files.txt')
    f.close()

def copier(file_list):
    logging.info('copier fn: Opening data_files.txt')
    f = open("data_files.txt", 'r')
    for i in f:
        #os.system(("cp" + " " + source + i + " " + destination))
        print "cp" + " " + source + i + " " + destination
    logging.info('copier fn: Finished copying every file')


if __name__ == '__main__':
    # The ranges of the files that we would like to copy over from loc1 to loc2
    limit1 = 57
    limit2 = 103

    files(limit1,limit2)
    copier("data_files.txt")
