#!python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 11, 2017 Fri
# Last update :
# Est time    :

# Imports
import glob
import gzip
import shutil
import os

# Global Variable
folders = ['doneall2','ivydoneall3']
to_decompress = 'bulge_f8_missing_headers'

def compress_files():
    for folder in folders:
        for fni in glob.glob('{}/*.fits'.format(folder)):
            fno = fni + '.gz'
            if not os.path.isfile(fno):
                print('Compressing {}'.format(fni))
                with open(fni, 'rb') as fi, gzip.open(fno, 'wb') as fo:
                    shutil.copyfileobj(fi, fo)
                    os.remove(fni)

def decompress_files():
    for fni in glob.glob('{}/*.fits.gz'.format(to_decompress)):
        fno = fni[0:-3]
        if not os.path.isfile(fno):
            print('deCompressing {}'.format(fni))
            with gzip.open(fni, 'rb') as fi, open(fno, 'wb') as fo:
                file_content = fi.read()
                fo.write(file_content)



def main():
    """Run main function."""
    compress_files()
    # decompress_files()

if __name__ == "__main__":
    main()
