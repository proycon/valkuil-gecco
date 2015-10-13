#!/bin/bash
cd models
if [ $? -ne 0 ]; then
    echo "Run from within the gecco-valkuil directory!" >&2
    exit 2
fi

echo "Downloading big data"
PREDOWNLOAD=`stat --printf='%X' valkuil-gecco-data.tar.bz2 2> /dev/null`
wget -c -N http://lst.science.ru.nl/~proycon/valkuil-gecco-data.tar.bz2
POSTDOWNLOAD=`stat --printf='%X' valkuil-gecco-data.tar.bz2 2> /dev/null`
if [ "$PREDOWNLOAD" != "$POSTDOWNLOAD" ]; then
    tar -xvjf valkuil-gecco-data.tar.bz2
fi

