import sys
sys.path.append('../src')

from time import sleep
from adt7410 import Adt7410

adt = Adt7410(1, 0x48, 0x00)

try:
	while True:
		temp = adt.read()
		print temp
		sleep(0.5)
except KeyboardInterrupt:
	pass

