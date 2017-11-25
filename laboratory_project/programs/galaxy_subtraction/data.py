import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot
import aplpy

# Using aplpy module to save the fits files into pdfs to view the images, astropy did 
# not work at all because of the nan's
gc = aplpy.FITSFigure('amosaic.fits')
gc.show_grayscale()
#gc.show_colorscale()
#gc.add_grid()
gc.save('test1234.pdf')
