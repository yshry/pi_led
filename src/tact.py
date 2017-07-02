import RPi.GPIO as GPIO

class Tact:
	def __init__(self, num):
		self.__num = num
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(num, GPIO.IN)

	def get(self):
		return GPIO.input(self.__num)
