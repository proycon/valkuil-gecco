#!/usr/bin/env python3


#If we run on Python 2.7, behave as much as Python 3 as possible
from __future__ import print_function, unicode_literals, division, absolute_import

#import some general python modules:
import sys
import os
import random
import shutil
import subprocess
import io

#import CLAM-specific modules. The CLAM API makes a lot of stuff easily accessible.
import clam.common.data
import clam.common.status

#make a shortcut to the shellsafe() function
shellsafe = clam.common.data.shellsafe

#this script takes three arguments from CLAM: $PARAMETERS  (as configured at COMMAND= in the service configuration file)
VALKUILDIR = sys.argv[1]
sentence = sys.argv[2]

with io.open('sentence.txt', 'w', encoding='utf-8') as f:
    f.write(sentence)

#gecco will output JSON to stdout
cmd = "gecco " + shellsafe(VALKUILDIR + '/valkuil.yml','"') + " run --json " + shellsafe('sentence.txt','"')
print("Invoking gecco: " + cmd,file=sys.stderr)
returncode = subprocess.call(cmd, stderr=sys.stderr)
sys.exit(returncode)





