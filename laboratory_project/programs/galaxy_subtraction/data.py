import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot

from astropy.utils.data import download_file
from astropy.io import fits

#image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )

hdu_list = fits.open('amosaic.fits')
hdu_list.info()

image_data = hdu_list[0].data

print(type(image_data))
print(image_data.shape)

print(len(image_data))

print(image_data)

np.savetxt('data.txt', image_data)

hdu_list.close()

pyplot.imshow(image_data, cmap='gray')
#pyplot.colorbar()
pyplot.savefig('amosaic2.pdf')

print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))
