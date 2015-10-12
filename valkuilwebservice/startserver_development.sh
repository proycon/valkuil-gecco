#!/bin/bash
if [ -z $PYTHONPATH ]; then
    export PYTHONPATH=`pwd`
else
    export PYTHONPATH=`pwd`:$PYTHONPATH
fi
clamservice valkuilwebservice
