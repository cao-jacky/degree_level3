import hcongrid
import numpy as np
from astropy.io import fits

loc = '/run/media/astrolab/JACKY_CAO_H/AT2017hhq'

def aligner():
	# Opening each fits files
	hdulist_b = fits.open(loc + '/B/mosaic.fits')
	hdulist_v = fits.open(loc + '/V/mosaic.fits')
	hdulist_r = fits.open(loc + '/R/mosaic.fits')

	# Selecting out the headers
	b_h = hdulist_b[0].header
	v_h = hdulist_v[0].header
	r_h = hdulist_r[0].header

	#print(hdulist_b.info(),hdulist_v.info(),hdulist_r.info())
	
	# Selecting out the data
	b_d = hdulist_b[0].data
	v_d = hdulist_v[0].data
	r_d = hdulist_r[0].data

	#print(b_d.shape)

	# Using aligner we align V and r bands to B bands
	v = hcongrid.hcongrid(b_d, b_h, v_h)
	r = hcongrid.hcongrid(b_d, b_h, r_h)

	# Closing the opening of the fits files
	hdulist_b.close()
	hdulist_v.close()
	hdulist_r.close()

	# Creating a new FITS File
	## For V
	hdu_v = fits.PrimaryHDU(v)
	hdulist_vv = fits.HDUList([hdu_v])
	hdulist_vv.writeto(loc + '/v_new.fits')

	## For R
	hdu_r = fits.PrimaryHDU(r)
	hdulist_rr = fits.HDUList([hdu_r])
	hdulist_rr.writeto(loc + '/r_new.fits')
	return 
