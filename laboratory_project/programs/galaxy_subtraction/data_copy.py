import os 

def copy(src, dest):
    """ Copies fits files from source to a destination. """
    os.system("cp " + src + " " + dest)

def copy_fol(src, dest):
    """ Copies folders from source to a destination. """
    os.system("cp -r " + src + " " + dest)

