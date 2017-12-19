import numpy as np
import matplotlib
import matplotlib.pyplot as pyplot
import aplpy

frame1 = '2017hhz_201017'
frame2 = '2017hhz_231117'
frame3 = '2017hhz_231117gs'
frame4 = '2017hhz_231117_new'
frame5 = '2017hhz_231117al'
frame6 = 'subtracted'
frame7 = 'subtracted_psfed2'

frame = frame7

# Using aplpy module to save the fits files into pdfs to view the images, astropy did 
# not work at all because of the nan's
gc = aplpy.FITSFigure(frame + '.fits')
gc.show_grayscale()
#gc.recenter(26.0758, 12.2550, radius=0.02)  # degrees
#gc.show_colorscale()
#gc.add_grid()
#gc.set_theme('publication')
gc.save(frame + '.pdf')
