#!/usr/bin/python
import json
print "Content-type: text\n\n"

json_dict = {'status':'off'}

fname='./led.json'
f = open(fname, 'w')
json.dump(json_dict, f)
f.close()
print json_dict['status']
