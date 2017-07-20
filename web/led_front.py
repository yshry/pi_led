#!/usr/bin/python
import json
import os
print "Content-type: text\n\n"

fname = './led.json'

if not os.path.exists(fname):
	json_dict = {'status':'on'}
else:
	f=open(fname, 'r')
	json_dict = json.load(f)
	f.close()
	if json_dict['status'] == 'on':
		json_dict['status'] = 'off'
	else:
		json_dict['status'] = 'on'

f = open(fname, 'w')
json.dump(json_dict, f)
f.close()
print json_dict['status']
