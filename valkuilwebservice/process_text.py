#!/usr/bin/env python3

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
text = sys.argv[2]

filename = "input-" + str("%x" % random.getrandbits(64)) + ".txt"

with io.open(filename, 'w', encoding='utf-8') as f:
    f.write(text)

#gecco will output JSON to stdout
cmd = "gecco " + shellsafe(VALKUILDIR + '/valkuil.yml','"') + " run -o output.folia.xml " + filename
print("Invoking gecco: " + cmd,file=sys.stderr)
returncode = subprocess.call(cmd,shell=True, stderr=sys.stderr)
os.system("cat output.folia.xml")
sys.exit(returncode)
