import numpy as np
from astropy.io import fits

import sys
sys.path.insert(0, '/Users/jackycao/Documents/Projects/degree_level3/laboratory_project/programs/aligner/marks_scripts')

import hcongrid

def bands_info():
    loc = '/run/media/astrolab/JACKY_CAO_H/AT2017hhq'
    bands = ['B','V']
    return loc, bands

def same_info():
    loc = '/Volumes/JACKY_CAO_H/2017hhz/'
    files = ['171022_v.fits', '171123_v.fits']
    return loc, files

def align_same():
    """ Aligning for the same band, just different days of data. """
    s_i = same_info() # Calling info from function
    loc = s_i[0]
    files = s_i[1]

    # Open our fits files
    h_1 = fits.open(loc + files[0]) # Opening main frame that is not adjusted
    h_2 = fits.open(loc + files[1]) # Frame that will be adjusted to frame 1

    # Selecting the headers out
    one_head = h_1[0].header
    two_head = h_2[0].header

    # Selecting the data
    one_data = h_1[0].data
    two_data = h_2[0].data

    # Aligning frame 2 to frame 1
    al = hcongrid.hcongrid(one_data, one_head, two_head)

    # Closing the fits files
    h_1.close()
    h_2.close()

    # Saving aligned frame 2 to a new fits file
    two_al = fits.PrimaryHDU(al)
    two_al_n = fits.HDUList([two_al])
    two_al_n.writeto(loc + files[1] + '_new.fits')


def aligner_bands():
    """ Aligning for data in different bands for colour image producing. """
    b_i = bands_info() # Calling information stored in function
    loc = b_i[0]
    bands = b_i[1]

    # Opening each fits files
    hdulist_b = fits.open(loc + '/B/mosaic.fits')
    hdulist_v = fits.open(loc + '/V/mosaic.fits')
    if 'R' in bands:
        hdulist_r = fits.open(loc + '/R/mosaic.fits')

    # Selecting out the headers
    b_h = hdulist_b[0].header
    v_h = hdulist_v[0].header
    if 'R' in bands:
        r_h = hdulist_r[0].header
	
    # Selecting out the data
    b_d = hdulist_b[0].data
    v_d = hdulist_v[0].data
    if 'R' in bands:
        r_d = hdulist_r[0].data

    # Using aligner we align V and r bands to B bands
    v = hcongrid.hcongrid(b_d, b_h, v_h)
    if 'R' in bands:
        r = hcongrid.hcongrid(b_d, b_h, r_h)

    # Closing the opening of the fits files
    hdulist_b.close()
    hdulist_v.close()
    if 'R' in bands:
        hdulist_r.close()

    # Creating a new FITS File
    ## For V
    hdu_v = fits.PrimaryHDU(v)
    hdulist_vv = fits.HDUList([hdu_v])
    hdulist_vv.writeto(loc + '/v_new.fits')

    if 'R' in bands:
        ## For R
        hdu_r = fits.PrimaryHDU(r)
        hdulist_rr = fits.HDUList([hdu_r])
        hdulist_rr.writeto(loc + '/r_new.fits')

if __name__ == '__main__':
    align_same()
