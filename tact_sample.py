import sys
sys.path.append('./src')

from led_control import Led
from tact import Tact
import RPi.GPIO as GPIO
import time

myled = Led(20)
mytact = Tact(21)

start = time.time()
current = time.time()

while (current - start) < 20.0:
	if mytact.get():
		myled.on()
	else:
		myled.off()

	current = time.time()
GPIO.cleanup()
