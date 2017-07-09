import sys
sys.path.append('../src')

from buzzer import Buzzer
import time

sounds = ['do', 're', 'mi', 'do' , 'mi', 'do', 'mi']

mybuzzer = Buzzer(18,50)

for i in range(len(mybuzzer.doremi)):
	mybuzzer.sound_on(mybuzzer.doremi.keys()[i], 5)
	time.sleep(1)

mybuzzer.off()
	
