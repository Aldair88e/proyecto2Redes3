#!/usr/bin/env python
import rrdtool
ret = rrdtool.create("../media/traficoTCP.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:insegs:COUNTER:120:U:U",
                     "DS:outsegs:COUNTER:120:U:U",
		     "DS:inoctets:COUNTER:120:U:U",
		     "DS:outoctets:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:1:25")

if ret:
    print (rrdtool.error())
