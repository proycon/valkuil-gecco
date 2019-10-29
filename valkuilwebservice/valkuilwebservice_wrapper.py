#!/usr/bin/env python
#-*- coding:utf-8 -*-

###############################################################
# CLAM: Computational Linguistics Application Mediator
# -- CLAM Wrapper script Template --
#       by Maarten van Gompel (proycon)
#       https://proycon.github.io/clam
#       Centre for Language and Speech Technology
#       Radboud University Nijmegen
#
#       Licensed under GPLv3
#
###############################################################

#This is a template wrapper which you can use a basis for writing your own
#system wrapper script. The system wrapper script is called by CLAM, it's job it
#to call your actual tool.

#This script will be called by CLAM and will run with the current working directory set to the specified project directory

#This wrapper script uses Python and the CLAM Data API.
#We make use of the XML settings file that CLAM outputs, rather than
#passing all parameters on the command line.


#import some general python modules:
import sys
import os
import codecs
import re
import string

#import CLAM-specific modules. The CLAM API makes a lot of stuff easily accessible.
import clam.common.data
import clam.common.status

#When the wrapper is started, the current working directory corresponds to the project directory, input files are in input/ , output files should go in output/ .

#make a shortcut to the shellsafe() function
shellsafe = clam.common.data.shellsafe

#this script takes three arguments from CLAM: $DATAFILE $STATUSFILE $OUTPUTDIRECTORY  (as configured at COMMAND= in the service configuration file)
VALKUILDIR = sys.argv[1]
datafile = sys.argv[2]
statusfile = sys.argv[3]
outputdir = sys.argv[4]

#If you make use of CUSTOM_FORMATS, you need to import your service configuration file here and set clam.common.data.CUSTOM_FORMATS
#Moreover, you can import any other settings from your service configuration file as well:

#from yourserviceconf import CUSTOM_FORMATS

#Obtain all data from the CLAM system (passed in $DATAFILE (clam.xml)), always pass CUSTOM_FORMATS as second argument if you make use of it!
clamdata = clam.common.data.getclamdata(datafile)

#You now have access to all data. A few properties at your disposition now are:
# clamdata.system_id , clamdata.project, clamdata.user, clamdata.status , clamdata.parameters, clamdata.inputformats, clamdata.outputformats , clamdata.input , clamdata.output

clam.common.status.write(statusfile, "Starting...")

if 'donate' in clamdata and clamdata['donate']:
    donated = 'yes'
else:
    donated = 'no'

#SOME EXAMPLES (uncomment and adapt what you need)

#-- Iterate over all input files? --

#(Note: This iteration will fail if you change the current working directory, so make sure to set it back to the initial path if you do need to change it)
r = 0
for inputfile in clamdata.input:
    inputtemplate = inputfile.metadata.inputtemplate
    basename = os.path.basename(str(inputfile))
    clam.common.status.write(statusfile, "Processing " + basename + "...")
    if basename[-4:] in ('.txt','.xml'): basename = basename[:-4]
    outputfile = outputdir + '/' + os.path.basename(basename) + '.xml'
    r = os.system("gecco " + shellsafe(VALKUILDIR + '/valkuil.yml','"') + " run -m donated=" + donated + ' -o ' + shellsafe(outputfile,'"') + ' ' + shellsafe(str(inputfile),'"'))
    if r != 0:
        clam.common.status.write(statusfile, "Failed",100) # status update
        sys.exit(r)

#A nice status message to indicate we're done
clam.common.status.write(statusfile, "Done",100) # status update

sys.exit(0) #non-zero exit codes indicate an error and will be picked up by CLAM as such!
