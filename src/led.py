import RPi.GPIO as GPIO
import gpiopin

class Led(gpiopin.Gpiopin):
	def __init__(self, num):
		super(Led, self).__init__(num)
	
	def __del__(self):
		super(Led, self).__del__()	
