import sys
sys.path.append('../src')

from led import Led
#from tact import Tact
from mcp3208 import Mcp3208
#import RPi.GPIO as GPIO
import time
from time import sleep

mymcp = Mcp3208(11, 10, 9, 8)
#myled = Led(21)

start = time.time()
current = time.time()

while (current - start) < 20.0:
	value = mymcp.readadc(0)
	print (value)
	#if (value < 3000):
	#	myled.on()
	#else:
	#	myled.off()
	sleep(0.2)
#GPIO.cleanup()
