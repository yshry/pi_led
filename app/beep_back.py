import sys
sys.path.append('../src')

from buzzer import Buzzer
import json
import time

mybuzzer = Buzzer(12)
fname ='./web/beep.json'

try:
	while True:
		try:
			f=open(fname, 'r')
			json_dict = json.load(f)
			f.close()
			tone = json_dict['tone']
			level = int(json_dict['level'])
			if tone != 'na':
				print json_dict
				mybuzzer.softtonewrite(tone, level)
			else:
				mybuzzer.softtonestop()
		except:
			f.close()
			print (sys.exc_info())
			mybuzzer.softtonestop()
		time.sleep(0.2)
except KeyboardInterrupt:
	pass
