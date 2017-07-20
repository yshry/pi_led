import sys
sys.path.append('../src')

from led import Led
import json
import time

myled = Led(21)
fname ='./led.json'

try:
	while True:
		try:
			f=open(fname, 'r')
			json_dict = json.load(f)
			if json_dict['status'] == 'on':
				myled.on()
			else:
				myled.off()
		except ValueError:
			print ('ValueError')
		time.sleep(0.2)
except KeyboardInterrupt:
	pass
