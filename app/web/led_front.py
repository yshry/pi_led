#!/usr/bin/python
import json
import os
import cgi
import sys

print "Content-type: text\n\n"

fname = './led.json'
data = cgi.FieldStorage()

status = data.getvalue('status', 'off')
json_dict = {'status': status}

complete = False	
while not complete:
	try:
		f=open(fname, 'w')
		json.dump(json_dict, f)
		f.close()
		complete = True
	except:
		f.close()
		print (sys.exec_info())
		complete = False
print json_dict
