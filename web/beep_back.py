import sys
sys.path.append('../src')

from buzzer import Buzzer
import json
import time

mybuzzer = Buzzer(12)
fname ='./beep.json'

try:
	while True:
		try:
			f=open(fname, 'r')
			json_dict = json.load(f)
			tone = json_dict['tone']
			level = int(json_dict['level'])
			if tone != 'na':
				print json_dict
				mybuzzer.softtonewrite(tone, level)
			else:
				mybuzzer.softtonestop()
		except ValueError:
			print ('ValueError')
		time.sleep(0.1)
except KeyboardInterrupt:
	pass
