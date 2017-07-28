#!/usr/bin/python
import json
import cgi
import sys

sys.path.append('../../src')
from pisocket import sendjson

data = cgi.FieldStorage()
direction = data.getvalue('direction', 'stop')

print "Content-type: text\n\n"
json_dict = {'direction' : direction}
complete = (sendjson('localhost', 10080, json_dict) == 1) 

print complete
