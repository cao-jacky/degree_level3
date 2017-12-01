import numpy
import math
from astropy import wcs
from astropy.io import fits
import datetime
import sys
#from photutils import SigmaClip, MeanBackground
from photutils import make_source_mask
from astropy.stats import sigma_clipped_stats
"""
def ABtomJy(mag):
    mJy = 10**(-2/5.*mag)*3631*1000.
    return mJy

def ABtoJy(mag):
    Jy = 10**(-2/5.*mag)*3631
    return Jy

def getrange(img,frac):
    gd = numpy.where(img != 0)
    vals = img[gd]
    type(vals)
    out = sorted(vals)
    n = len(vals)
    lo_i = round(n*(1-frac))
    hi_i = round(n*frac)
    lov = out[lo_i]
    hiv = out[hi_i]
    out = numpy.array([lov,hiv])
    return out
    
def nan1d(img,val):
    bad = numpy.isnan(img)
    img[bad]=val
    return img

def nan2d(img,val):
    bad = numpy.isnan(img)
    img[bad]=val
    return img

def nan3d(img,val):
    bad = numpy.isnan(img)
    img[bad]=val
    return img

def getscale(hdr):
    w = wcs.WCS(hdr)
    ra0,dec0 = w.wcs_pix2world(0,0,1)
    ra1,dec1 = w.wcs_pix2world(0,1,1)
    asecpix = dec1-dec0
    asecpix = abs(3600*asecpix)
    return asecpix

def ad2xy(hdr,ra,dec):
    w = wcs.WCS(hdr)
    xc,yc = w.wcs_world2pix(ra,dec,1)
    return xc,yc

def xy2ad(hdr,x,y):
    w = wcs.WCS(hdr)
    ra,dec = w.wcs_pix2world(x,y,1)
    return ra,dec

def hextract(img,hdr,x0,x1,y0,y1):
    x0 = int(round(x0))
    x1 = int(round(x1))
    y0 = int(round(y0))
    y1 = int(round(y1))
    sz = img.shape
    xsize = round(sz[1])
    ysize = round(sz[0])
    print('Original array size is ' + str(xsize) + ' by ' + str(ysize))
    if (x1 <= x0 ) or (x0 <0) or (x1 >= xsize ):
        print('Error: Illegal pixel range: X direction')
    if (y1 <= y0) or (y0 <0) or (y1 >= ysize):
        print('Error: Illegal pixel range: Y direction')
    naxis1 = x1 - x0 + 1
    naxis2 = y1 - y0 + 1   #New dimensions
    print('Now extracting a '+ str(naxis1) + ' by ' + str(naxis2) + ' subarray')
    #print(x0,x1,y0,y1,naxis1,naxis2)
    #sys.exit()
    newim = img[y0:y1,x0:x1]
    newhdr = hdr
    newhdr['NAXIS1'] = naxis1
    newhdr['NAXIS2'] = naxis2
    newhdr['pyEXTRACT'] = (str(datetime.datetime.now()), 'PY-EXTRACTED time')
    newhdr['OrigAxis1'] = (str(xsize), 'Original naxis1')
    newhdr['OrigAxis2'] = (str(ysize), 'Original naxis2')
    newhdr['Ext_x0'] = (str(x0), 'Extracted at x0')
    newhdr['Ext_x1'] = (str(x1), 'Extracted to x1')
    newhdr['Ext_y0'] = (str(y0), 'Extracted at y0')
    newhdr['Ext_y1'] = (str(y1), 'Extracted to y1')
    orig_crpix1 = hdr['CRPIX1']
    orig_crpix2 = hdr['CRPIX2']    
    new_crpix1 = orig_crpix1 - x0
    new_crpix2 = orig_crpix2 - y0
    newhdr['CRPIX1'] = (new_crpix1, 'Reference pixel on axis 1')
    newhdr['CRPIX2'] = (new_crpix2, 'Reference pixel on axis 2')
    return newim,newhdr
"""

def getstats(img,ff):
    
    gd = numpy.where(img != 0)
    print('there are ',len(gd),' elements')
    arr = img[gd]
    arr = sorted(arr)
    n = len(arr)
    print('array is ',n,' elements')
    i = round(ff*n)
    vmax = arr[i]
    print(ff,' signal range value is ',vmax)
    
    print('making mask')
    mask = make_source_mask(img, snr=2, npixels=5, dilate_size=11)
    print('calculating stats')
    vmean, vmedian, vstd = sigma_clipped_stats(img, sigma=3.0, mask=mask,mask_value=0.)
    print('mean: ',vmean)
    print('median: ',vmedian)
    print('sigma: ',vstd)
    return vmean,vmedian,vstd,vmax


def mkcol(b,v,r,ff,gamma):

    bmean,bmedian,bstd,bmax = getstats(b,ff)
    vmean,vmedian,vstd,vmax = getstats(v,ff)
    rmean,rmedian,rstd,rmax = getstats(r,ff)

    bmin = bmean
    vmin = vmean
    rmin = rmean

    gdb = numpy.where(b != 0)
    gdv = numpy.where(v != 0)
    gdr = numpy.where(r != 0)

    b[gdb] = (b[gdb]-bmin)/(bmax-bmin)
    v[gdb] = (v[gdb]-vmin)/(vmax-vmin)
    r[gdb] = (r[gdb]-rmin)/(rmax-rmin)

    lo = 0.
    hi = 1.

    bad = numpy.where(b <= lo)
    b[bad]=0.
    bad = numpy.where(b >= hi)
    b[bad]=1.

    bad = numpy.where(v <= lo)
    v[bad]=0
    bad = numpy.where(v >= hi)
    v[bad]=1.

    bad = numpy.where(r <= lo)
    r[bad]=0
    bad = numpy.where(r >= hi)
    r[bad]=1.

    b = b**gamma
    v = v**gamma
    r = r**gamma

#    b = b*254.
#    v = v*254.
#    r = r*254.

    sz = b.shape
    print(sz[1],sz[0])
    
    col = numpy.zeros((sz[0],sz[1],3))
    col[:,:,0] = b
    col[:,:,1] = v
    col[:,:,2] = r

    return col
