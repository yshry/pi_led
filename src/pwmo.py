import RPi.GPIO as GPIO
import wiringpi

class Pwmo(object):
	def __init__(self, num):
		self.__num = num
		wiringpi.wiringPiSetupGpio()
		wiringpi.pinMode(self.__num, wiringpi.GPIO.PWM_OUTPUT)
		wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

	def __del__(self):
		GPIO.cleanup(self.__num)

	def setclock(self, hertz):
		val = 18750. /hertz 
		wiringpi.pwmSetClock(val)
	
	def pwmWrite(self, duty):
		wiringpi.pwmWrite(self.__num, duty)

