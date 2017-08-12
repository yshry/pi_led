import sys
sys.path.append('../src')

from time import sleep
from l3gd20 import L3gd20

l3gd = L3gd20(1, 0x6a)

try:
	while True:
		temp = l3gd.read_x()
		print temp
		sleep(0.5)
except KeyboardInterrupt:
	pass

