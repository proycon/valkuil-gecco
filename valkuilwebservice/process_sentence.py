#!/usr/bin/env python3


#If we run on Python 2.7, behave as much as Python 3 as possible
from __future__ import print_function, unicode_literals, division, absolute_import

#import some general python modules:
import sys
import os
import string
import shutil
import io

#import CLAM-specific modules. The CLAM API makes a lot of stuff easily accessible.
import clam.common.data
import clam.common.status

from pynlpl.formats import folia

#make a shortcut to the shellsafe() function
shellsafe = clam.common.data.shellsafe

#this script takes three arguments from CLAM: $PARAMETERS  (as configured at COMMAND= in the service configuration file)
VALKUILDIR = sys.argv[1]
sentence = sys.argv[2]

tmpdir = ".process_sentence." + "%032x" % random.getrandbits(128) + '/'
os.mkdir(tmpdir)
with io.open(tmpdir + '/sentence.txt', 'w', encoding='utf-8') as f:
    f.write(sentence)

#gecco will output JSON to stdout
r = os.system("gecco " + shellsafe(VALKUILDIR + '/valkuil.yml','"') + " run --json " + shellsafe(tmpdir+'/sentence.txt','"'))
if r != 0:
    clam.common.status.write(statusfile, "Failed",100) # status update
    shutil.rmtree(tmpdir)
    sys.exit(r)

shutil.rmtree(tmpdir)
sys.exit(0)





