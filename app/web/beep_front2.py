#!/usr/bin/python
import json
import cgi
import sys

sys.path.append('../../src')
from pisocket import sendjson

data = cgi.FieldStorage()

tone = data.getvalue('tone', 'na')
level = data.getvalue('level', 0)
level = int(level)

json_dict = {'tone': tone, 'level': level}

print "Content-type: text\n\n"

complete = (sendjson('localhost', 10080, json_dict) == 1) 

print complete
