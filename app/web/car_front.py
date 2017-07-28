#!/usr/bin/python
import json
import cgi
import sys

sys.path.append('../../src')
from pisocket import sendjson

#data = cgi.FieldStorage()

#direction = data.getvalue('direction', 'stop')

json_dict = {'direction': 'back'}

print "Content-type: text\n\n"

complete = (sendjson('localhost', 10080, json_dict) == 1) 

print complete
