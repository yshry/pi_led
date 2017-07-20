import sys
sys.path.append('../src')

from buzzer import Buzzer
from time import sleep

mybuzzer = Buzzer(12)

scale = ['c', 'd', 'e', 'f', 'g', 'a', 'b']

for i in range(2,4):
	for tone in scale:
		mybuzzer.softtonewrite(tone, i)
		sleep(1)


