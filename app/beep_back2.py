import os
import sys
sys.path.append('../src')

from buzzer import Buzzer
from led import Led
from pisocket import Pisocket
import json
import time

mybuzzer = Buzzer(12)
myled = Led(21)
mysocket = Pisocket(10080,1)

try:
	while True:
		json_dict = mysocket.wait_and_accept()
		tone = json_dict['tone']
		level = int(json_dict['level'])
		if tone != 'na':
				#print json_dict
			mybuzzer.softtonewrite(tone, level)
			myled.on()
		else:
			mybuzzer.softtonestop()
			myled.off()
		#print json_dict
except KeyboardInterrupt:
	pass
