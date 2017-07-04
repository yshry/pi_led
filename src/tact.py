import RPi.GPIO as GPIO

class Tact:
	def __init__(self, num):
		self.__num = num
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(num, GPIO.IN)
	
	def __del__(self):
		GPIO.cleanup(self.__num)

	def get(self):
		return GPIO.input(self.__num)
