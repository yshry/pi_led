import sys
sys.path.append('../src')

from buzzer import Buzzer
from led import Led
import json
import time

mybuzzer = Buzzer(12)
myled = Led(21)
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
				myled.on()
			else:
				mybuzzer.softtonestop()
				myled.off()
		except:
			f.close()
			print (sys.exc_info())
			mybuzzer.softtonestop()
			myled.off()
		time.sleep(0.25)
except KeyboardInterrupt:
	pass
