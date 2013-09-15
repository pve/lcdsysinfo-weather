#!/bin/sh
echo Feeling Utrecht  weather..
wget -O yw.htm http://weather.yahooapis.com/forecastrss?w=734047\&u=c -o log.txt
echo Processing..
grep -A4 -i 'Current' yw.htm > yw
sed '1d' yw > yw2
sed '2d' yw2 > yw
sed -i 's/<br \/>//g' yw
sed -i 's/<BR \/>//g' yw
sed -i 's/High/\nHigh/g' yw
date "+%a %b %d   %H:%I" >> yw
echo Displaying..
sudo ./weather.py
echo Done
