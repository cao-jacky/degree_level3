import aligner
import amstools
from astropy.io import fits

loc = '/run/media/astrolab/JACKY_CAO_H/AT2017hhq/'

b = loc + 'b_new.fits'
v = loc + 'v_new.fits'
r = loc + 'r_new.fits'

def data():
	""" Opening the data from FITs files. """
	h_b = fits.open(b)
	h_v = fits.open(v)
	h_r = fits.open(r)

	b_d = h_b[0].data
	v_d = h_v[0].data
	r_d = h_r[0].data
	
	return b_d, v_d, r_d

def colour():
	dt = data()
	colour = amstools.mkcol(dt[0], dt[1], dt[2], 0.95, 1)
	print(colour)  

if __name__ == '__main__':
	colour()
