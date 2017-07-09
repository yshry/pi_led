import sys
sys.path.append('../src')

from mcp3208 import Mcp3208
from buzzer import Buzzer
from time import sleep

mymcp = Mcp3208(11, 10, 9, 8)
mybuzzer = Buzzer(18)

scale = ['c', 'd', 'e', 'f', 'g', 'a', 'b']

for i in range(1,3):
	for tone in scale:
		mybuzzer.softtonewrite(tone, i)
		sleep(1)


