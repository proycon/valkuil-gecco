#!/bin/bash
if [ -z $PYTHONPATH ]; then
    export PYTHONPATH=/home/proycon/work/valkuil-gecco/valkuilwebservice
else
    export PYTHONPATH=/home/proycon/work/valkuil-gecco/valkuilwebservice:$PYTHONPATH
fi
clamservice valkuilwebservice
