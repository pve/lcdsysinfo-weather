#!/bin/sh
echo Feeling Utrecht  weather..
date "+%a %b %d   %H:%M" > yw
. ./keystore
sudo -E ./weather.py
