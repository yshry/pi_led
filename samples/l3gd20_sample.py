import sys
sys.path.append('../src')

from time import sleep
from l3gd20 import L3gd20

l3gd = L3gd20(1, 0x6a)

l3gd.change_range('500dps')

try:
	while True:
		temp = l3gd.read()
		print temp
		sleep(0.5)
except KeyboardInterrupt:
	pass

