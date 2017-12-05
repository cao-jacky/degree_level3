import glob
import numpy as np
from astropy.io import fits
from scipy.ndimage.filters import gaussian_filter
from astropy.convolution import convolve, Gaussian2DKernel, AiryDisk2DKernel
from astropy.modeling.models import Gaussian2D

def data_namer(loc):
    """ Outputting the data in location, loc. """
    print(glob.glob(loc + "/*.fits"))
    return glob.glob(loc + "/*.fits")

def data(loc, fl):
    """ Opens the files and stores data as arrays. """
    f_1 = fits.open(loc + '/' + fl[0]) # Frame 1 to remove galaxy from
    f_2 = fits.open(loc + '/' + fl[1]) # Frame 2 to use as the remover

    # Selecting the data out of the fits files
    f_1_d = f_1[0].data 
    f_2_d = f_2[0].data
    
    # Closing the fits files
    f_1.close()
    f_2.close()
    return f_1_d, f_2_d

def scaler(data, counts):
    """ Scales the second frame so that it correct removes the galaxy. """

    f_1_c = counts[0] # Counts of object from frame 1
    f_2_c = counts[1] # Counts of object from frame 2

    ratio = f_2_c / f_1_c # The ratio we would need to get from frame 1 to frame 2
    sc = data[0] * ratio # Frame 1 scaled to frame 2
    return sc

def psf(data, counts):
    """ Tries to change the PSF so that it is perfectly subtracted. """
    dt = scaler(data, counts)
    gauss_kernel = Gaussian2DKernel(2) + Gaussian2DKernel(1) + Gaussian2DKernel(1) + Gaussian2DKernel(1) + Gaussian2DKernel(1) + Gaussian2DKernel(1) + Gaussian2DKernel(1)
    smoothed_data_gauss = convolve(dt, gauss_kernel)
    return smoothed_data_gauss

def subtractor(data, counts):
    """ Performing the galaxy subtraction and returning subtracted frame. """
    d_psf = psf(data, counts) # Applying the PSF scaler thing
    #d_scl = scaler(data, counts) # Scaled data for frame 1
    return d_psf - data[1]

def saver(loc, fl, counts):
    """ Saves galaxy subtracted data to a fits file. """
    dt = data(loc, fl) # Returning data to variable

    f_1_sub = subtractor(dt, counts) # Subtracted data
    
    new = fits.PrimaryHDU(f_1_sub)
    new_n = fits.HDUList([new])
    new_n.writeto(loc + '/subtracted_psfed38.fits')
