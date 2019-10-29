#!/usr/bin/env python
#-*- coding:utf-8 -*-

###############################################################
# CLAM: Computational Linguistics Application Mediator
# -- Service Configuration File (Template) --
#       by Maarten van Gompel (proycon)
#       Centre for Language and Speech Technology / Language Machines
#       Radboud University Nijmegen
#
#       https://proycon.github.io/clam
#
#       Licensed under GPLv3
#
###############################################################

#Consult the CLAM manual for extensive documentation

#If we run on Python 2.7, behave as much as Python 3 as possible
from __future__ import print_function, unicode_literals, division, absolute_import

from clam.common.parameters import *
from clam.common.formats import *
from clam.common.converters import *
from clam.common.viewers import *
from clam.common.data import *
from clam.common.digestauth import pwhash
import clam
from base64 import b64decode as D
import sys
import os

REQUIRE_VERSION = 3.0

CLAMDIR = clam.__path__[0] #directory where CLAM is installed, detected automatically
WEBSERVICEDIR = os.path.dirname(os.path.abspath(__file__)) #directory where this webservice is installed, detected automatically

# ======== GENERAL INFORMATION ===========

# General information concerning your system.

#The System ID, a short alphanumeric identifier for internal use only
SYSTEM_ID = "valkuil"

#System name, the way the system is presented to the world
SYSTEM_NAME = "Valkuil.net"

SYSTEM_AUTHOR = "Maarten van Gompel, Antal van den Bosch"

SYSTEM_AFFILIATION = "Centre for Language and Speech Technology, Radboud University"

SYSTEM_URL = "https://github.com/proycon/valkuil-gecco"

SYSTEM_EMAIL = "lamasoftware@science.ru.nl"

#An informative description for this system:
SYSTEM_DESCRIPTION = "Valkuil doet context-gevoelige spellingcorrectie voor het Nederlands, aangedreven door Gecco."

SYSTEM_LICENSE = "Affero GNU General Public License v3"

SYSTEM_COVER_URL = "https://raw.githubusercontent.com/proycon/valkuil-frontend/master/valkuilnet/static/valkuil_logo.png"


# ======== AUTHENTICATION & SECURITY ===========

#Users and passwords

#set security realm, a required component for hashing passwords (will default to SYSTEM_ID if not set)
#REALM = SYSTEM_ID


#If you want to enable user-based security, you can define a dictionary
#of users and (hashed) passwords here. The actual authentication will proceed
#as HTTP Digest Authentication. Although being a convenient shortcut,
#using pwhash and plaintext password in this code is not secure!!

#USERS = { user1': '4f8dh8337e2a5a83734b','user2': pwhash('username', REALM, 'secret') }

#Amount of free memory required prior to starting a new process (in MB!), Free Memory + Cached (without swap!)
REQUIREMEMORY = 20

#Maximum load average at which processes are still started (first number reported by 'uptime')
MAXLOADAVG = 25

#load external configuration file
loadconfig(__name__)

# ======== WEB-APPLICATION STYLING =============

#Choose a style (has to be defined as a CSS file in clam/style/ ). You can copy, rename and adapt it to make your own style
STYLE = 'classic'

# ======== ENABLED FORMATS ===========

#In CUSTOM_FORMATS you can specify a list of Python classes corresponding to extra formats.
#You can define the classes first, and then put them in CUSTOM_FORMATS, as shown in this example:

#class MyXMLFormat(CLAMMetaData):
#    attributes = {}
#    name = "My XML format"
#    mimetype = 'text/xml'

# CUSTOM_FORMATS = [ MyXMLFormat ]

# ======= INTERFACE OPTIONS ===========

#Here you can specify additional interface options (space separated list), see the documentation for all allowed options
INTERFACEOPTIONS = "inputfromweb,centercover" #allow CLAM to download its input from a user-specified url

CUSTOMCSS = """
#cover {
    background: transparent;
}
"""

CUSTOMHTML_INDEX = """
<p>Valkuil.net is een automatische spellingcorrector voor het
Nederlands die zowel gewone typefouten als grammaticale fouten en
verwarringen tussen bestaande woorden opspoort.</p>

<p>Valkuil.net is gebaseerd op grote hoeveelheden Nederlandse
tekst, en niet op taalkundige kennis of een vaste woordenlijst. De
meeste modules in valkuil.net zijn
<i>contextgebaseerd</i> en <i>statistisch</i>: ze slaan alarm wanneer
ze een woord tegenkomen dat ze niet verwachten op basis van de
omgeving waarin dat woord staat. Het enthousiasme waarmee ze alarm
slaan is instelbaar.</p>

<p>Valkuil.net bevat modules voor hele specifieke verwarringen,
zoals <i>zei</i>-<i>zij</i>, maar ook voor fouten met vervoegingen
zoals de bekende <i>d</i>-<i>t</i>-fout. Valkuil.net doet ook zijn best om
vergeten spaties of teveel gezette spaties op te sporen.</p>
"""

# ======== PREINSTALLED DATA ===========

#INPUTSOURCES = [
#    InputSource(id='sampledocs',label='Sample texts',path=ROOT+'/inputsources/sampledata',defaultmetadata=PlainTextFormat(None, encoding='utf-8') ),
#]

# ======== PROFILE DEFINITIONS ===========

#Define your profiles here. This is required for the project paradigm, but can be set to an empty list if you only use the action paradigm.

PROFILES = [
    Profile(
        InputTemplate('textinput', PlainTextFormat,"Input text",
            StaticParameter(id='encoding',name='Encoding',description='The character encoding of the file', value='utf-8'),
            CharEncodingConverter(id='latin1',label='Convert from Latin-1',charset='iso-8859-1'),
            PDFtoTextConverter(id='pdfconv',label='Convert from PDF Document'),
            MSWordConverter(id='docconv',label='Convert from MS Word Document'),
            acceptarchive=True,
            extension='.txt',
            multi=True
        ),
        #------------------------------------------------------------------------------------------------------------------------
        OutputTemplate('foliaoutput',FoLiAXMLFormat,'FoLiA Document with spelling suggestions',
            FLATViewer(url=FLATURL,  configuration="valkuil", mode='viewer'),
            FoLiAViewer(),
            removeextension=['.txt'],
            extension='.xml',
            multi=True
        ),
    ),
    Profile(
        InputTemplate('foliainput', FoLiAXMLFormat,"FoLiA Document (tokenised)",
            extension='.xml',
            acceptarchive=True,
            multi=True
        ),
        #------------------------------------------------------------------------------------------------------------------------
        OutputTemplate('foliaoutput',FoLiAXMLFormat,'FoLiA Document with spelling suggestions',
            FLATViewer(url=FLATURL, configuration="valkuil", mode='viewer'),
            FoLiAViewer(),
            removeextension=['.xml'],
            extension='.xml',
            multi=True
        ),
    )
]

# ======== COMMAND ===========

#The system command for the project paradigm.
#It is recommended you set this to small wrapper
#script around your actual system. Full shell syntax is supported. Using
#absolute paths is preferred. The current working directory will be
#set to the project directory.
#
#You can make use of the following special variables,
#which will be automatically set by CLAM:
#     $INPUTDIRECTORY  - The directory where input files are uploaded.
#     $OUTPUTDIRECTORY - The directory where the system should output
#                        its output files.
#     $STATUSFILE      - Filename of the .status file where the system
#                        should output status messages.
#     $DATAFILE        - Filename of the clam.xml file describing the
#                        system and chosen configuration.
#     $USERNAME        - The username of the currently logged in user
#                        (set to "anonymous" if there is none)
#     $PARAMETERS      - List of chosen parameters, using the specified flags
#
COMMAND = WEBSERVICEDIR + "/valkuilwebservice_wrapper.py " + VALKUILDIR + " $DATAFILE $STATUSFILE $OUTPUTDIRECTORY"

#Or for the shell variant:
#COMMAND = WEBSERVICEDIR + "/valkuilwebservice_wrapper.sh $STATUSFILE $INPUTDIRECTORY $OUTPUTDIRECTORY $PARAMETERS"

#Or if you only use the action paradigm, set COMMAND = None

#The parameters are subdivided into several groups. In the form of a list of (groupname, parameters) tuples. The parameters are a list of instances from common/parameters.py
PARAMETERS =  [
    ('Instellingen', [
        #BooleanParameter(id='createlexicon',name='Create Lexicon',description='Generate a separate overall lexicon?'),
        #ChoiceParameter(id='casesensitive',name='Case Sensitivity',description='Enable case sensitive behaviour?', choices=['yes','no'],default='no'),
        #StringParameter(id='author',name='Author',description='Sign output metadata with the specified author name',maxlength=255),
        FloatParameter(id='sensitivity', name='Foutgevoeligheid',description="Hoe gevoelig moet de spellingcorrector zijn en iets als fout aan merken? (0.5 - Sla heel snel alarm, 1 - Sla nooit alarm)", minvalue=0.5, maxvalue=1.0, default=0.75, required=True),
        BooleanParameter(id='donate', name='Fouten doneren',description="Gevonden fouten doneren voor wetenschappelijk onderzoek?")
    ] )
]


# ======== ACTIONS ===========

ACTIONS = [
    Action(id="process", name="Tekstcorrectie", description="Controleer een Nederlandse tekst op spelfouten.",
        command=WEBSERVICEDIR + "/process_text.py "  + VALKUILDIR + " $PARAMETERS",
        allowanonymous=True,
        tmpdir=True,
        mimetype="application/xml",
        parameters=[
            TextParameter(id="text",name="Tekst",description="Voer hier je tekst in:",required=True),
        ],
        viewers=[
            FLATViewer(url=FLATURL, configuration="valkuil", mode='viewer'),
        ]
    ),
    Action(id="process_sentence", name="Snelle zinscorrectie (geavanceerd)", description="Verwerkt één voorgetokeniseerde zin en geeft een JSON antwoord terug met suggesties voor correctie.",
        command=WEBSERVICEDIR + "/process_sentence.py "  + VALKUILDIR + " $PARAMETERS",
        allowanonymous=True,
        tmpdir=True,
        mimetype="application/json",
        parameters=[
        StringParameter(id="sentence",name="Zinsinvoer",description="Één zin om te controleren, moet al getokeniseerd zijn! (losgesplitse woorden en punctuatie)",required=True),
    ])
]
# ======== DISPATCHING (ADVANCED! YOU CAN SAFELY SKIP THIS!) ========

#The dispatcher to use (defaults to clamdispatcher.py), you almost never want to change this
#DISPATCHER = 'clamdispatcher.py'

#DISPATCHER_POLLINTERVAL = 30   #interval at which the dispatcher polls for resource consumption (default: 30 secs)
#DISPATCHER_MAXRESMEM = 0    #maximum consumption of resident memory (in megabytes), processes that exceed this will be automatically aborted. (0 = unlimited, default)
#DISPATCHER_MAXTIME = 0      #maximum number of seconds a process may run, it will be aborted if this duration is exceeded.   (0=unlimited, default)
#DISPATCHER_PYTHONPATH = []        #list of extra directories to add to the python path prior to launch of dispatcher

#Run background process on a remote host? Then set the following (leave the lambda in):
#REMOTEHOST = lambda: return 'some.remote.host'
#REMOTEUSER = 'username'

#For this to work, the user under which CLAM runs must have (passwordless) ssh access (use ssh keys) to the remote host using the specified username (ssh REMOTEUSER@REMOTEHOST)
#Moreover, both systems must have access to the same filesystem (ROOT) under the same mountpoint.
