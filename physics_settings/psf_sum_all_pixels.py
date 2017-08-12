#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Aug 09, 2016
# Last update :
#
# Inputs      : a fitsfile
# Outputs     : the total number
#
# Info:
# 1. This program will get the sum of all the pixels in a fitsfile.
#
# Estimated time : 1 min 30 sec
#


# Imports
from astropy.io import fits
import numpy as np
import time


def psf_sum_of_all_pixels(infits):

        infile = infits
        data = fits.getdata(infile)
        shape = data.shape

        rows = data.shape[0]
        total = 0.0
        for i in range(rows):
            total += sum(data[i])
        print('{} {} {}'.format(infile, ' sum_of_all_pixels = ', total))


# ==============================================================================
# Main program
# ==============================================================================
if __name__ == '__main__':

    # run main program
    psf_sum_of_all_pixels('psf_scalednew.fits')
    psf_sum_of_all_pixels('psf_decam.fits')
