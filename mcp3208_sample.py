import sys
sys.path.append('./src')

#from led_control import Led
#from tact import Tact
from mcp3208 import Mcp3208
#import RPi.GPIO as GPIO
import time
from time import sleep

mymcp = Mcp3208(11, 10, 9, 8)

start = time.time()
current = time.time()

while (current - start) < 20.0:
	print (mymcp.readadc(0))
	sleep(0.2)
#GPIO.cleanup()
