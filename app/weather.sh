#!/bin/sh
echo Feeling Utrecht  weather..
date "+%a %b %d   %H:%M" >> yw
echo Displaying..
. ./keystore
sudo -E ./weather.py
echo Done
