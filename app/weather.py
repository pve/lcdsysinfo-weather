#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pylcdsysinfo import BackgroundColours, TextColours, TextAlignment, TextLines, LCDSysInfo

d = LCDSysInfo()
d.clear_lines(TextLines.ALL, BackgroundColours.BLACK)
d.dim_when_idle(False)
d.set_brightness(127)
d.save_brightness(127, 255)
d.set_text_background_colour(BackgroundColours.BLACK)

import urllib2, json
import os

from time import gmtime, strftime
today = strftime("%Y-%m-%d", gmtime())

nkey = os.getenv('WMNKEY', 'novalidkey' )
# the command environment will hold the Authentication NKEY
#startdate = today()

mytags = "&tags=myproduction"

startdate = "&start_date=" + today

url = "https://api.cloudmonitor.ca.com/1.6/rule_stats?nkey=" + nkey + mytags + startdate + "&callback=json"

totalerrors =""
totalchecks ="No data"

try:
  jsonp = urllib2.urlopen(url).read()
  jsondata = jsonp[ jsonp.index("(")+1 : jsonp.rindex(")") ]
  data = json.loads(jsondata)
  totalchecks = data['result']['stats'][0]['checks'] 
  totalerrors = data['result']['stats'][0]['check_errors']
except urllib2.URLError, e:
  print 'no valid data received' 

print json.dumps(data)


bad = " "
line = str("WatchM err " + totalerrors + "/" + totalchecks )
print line

col = TextColours.GREEN
d.display_text_on_line(6, line, False, TextAlignment.LEFT, col)

f = open('yw', 'r')
c = 1
for line in f:
        if c == 2:
                col = TextColours.PURPLE
        if c == 3:
                col = TextColours.PURPLE
        if c == 4:
                col = TextColours.LIGHT_BLUE
        if c == 5:
                col = TextColours.LIGHT_BLUE
	if c == 6:
		col = TextColours.RED
        d.display_text_on_line(c, line, False, TextAlignment.LEFT, col)
        c = c + 1
        if c > 5:
                break
