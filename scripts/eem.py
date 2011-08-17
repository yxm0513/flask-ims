#!/usr/bin/env python

import re

f = open('./a', 'r+')
lines = f.readlines()

sum = 0

for line in lines:
   #print line
   line = line.replace(",","")
   m = re.search(r"""(?P<num>[\d\.\,]+)\s+CNY""", line)
   
   if m:   
      print m.group('num')
      a = m.group('num')
      sum += float(a)
   else:
      print "No Matched";


print sum

f.close
