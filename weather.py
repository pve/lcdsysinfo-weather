#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pylcdsysinfo import BackgroundColours, TextColours, TextAlignment, TextLines, LCDSysInfo
from time import sleep
import urllib

d = LCDSysInfo()
d.clear_lines(TextLines.ALL, BackgroundColours.BLACK)
d.dim_when_idle(False)
d.set_brightness(127)
d.save_brightness(127, 255)
d.set_text_background_colour(BackgroundColours.BLACK)

f = open('yw', 'r')
c = 1
col = TextColours.GREEN
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
        if c > 6:
                break
