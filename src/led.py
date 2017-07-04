import RPi.GPIO as GPIO

class Led:
	def __init__(self, num):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(num, GPIO.OUT)
		self.__num = num
	
	def __del__(self):
		GPIO.cleanup(self.__num)	

	def on(self):
		GPIO.output(self.__num, GPIO.HIGH)

	def off(self):
		GPIO.output(self.__num, GPIO.LOW)
