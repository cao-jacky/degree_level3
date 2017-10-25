import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from astropy.utils.data import download_file
from astropy.io import fits

#image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )

hdu_list = fits.open('amosaic.fits')
hdu_list.info()

image_data = hdu_list[0].data

print(type(image_data))
print(image_data.shape)

hdu_list.close()

plt.imshow(image_data, cmap='gray')
plt.colorbar()
plt.show()
