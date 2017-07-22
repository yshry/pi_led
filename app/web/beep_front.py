#!/usr/bin/python

import json
import cgi
import sys

data = cgi.FieldStorage()

tone = data.getvalue('tone', 'na')
level = data.getvalue('level', 0)
level = int(level)

json_dict = {'tone': tone, 'level': level}

print "Content-type: text\n\n"

complete = False
while not complete:
	try:
		fname = './beep.json'
		f=open(fname,'w')
		json.dump(json_dict, f)
		f.close()
		complete = True
	except:
		f.close()
		print (sys.exc_info())
		complete = True

print json_dict
