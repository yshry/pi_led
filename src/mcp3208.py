import RPi.GPIO as GPIO

class Mcp3208:
	def __init__(self, clockpin, mosipin, misopin, cspin):
		self.__clockpin = clockpin
		self.__mosipin = mosipin
		self.__misopin = misopin
		self.__cspin = cspin
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.__clockpin, GPIO.OUT)
		GPIO.setup(self.__mosipin, GPIO.OUT)
		GPIO.setup(self.__misopin, GPIO.IN)
		GPIO.setup(self.__cspin, GPIO.OUT)
	
	def __del__(self):
		GPIO.cleanup(self.__clockpin)
		GPIO.cleanup(self.__mosipin)
		GPIO.cleanup(self.__misopin)
		GPIO.cleanup(self.__cspin)
	
	def readadc(self, adcnum):
		if adcnum > 7 or adcnum < 0:
			return -1

		GPIO.output(self.__cspin, GPIO.HIGH)
		GPIO.output(self.__clockpin, GPIO.LOW)
		GPIO.output(self.__cspin, GPIO.LOW)

		commandout = adcnum
		commandout |= 0x18
		commandout <<= 3
		for i in range(5):
			if commandout & 0x80:
				GPIO.output(self.__mosipin, GPIO.HIGH)
			else:
				GPIO.output(self.__mosipin, GPIO.LOW)
			commandout <<=1
			GPIO.output(self.__clockpin, GPIO.HIGH)
			GPIO.output(self.__clockpin, GPIO.LOW)
		adcout = 0

		for i in range(13):
			GPIO.output(self.__clockpin, GPIO.HIGH)
			GPIO.output(self.__clockpin, GPIO.LOW)
			adcout <<= 1
			if i>0 and GPIO.input(self.__misopin) == GPIO.HIGH:
				adcout |= 0x1
		GPIO.output(self.__cspin, GPIO.HIGH)
		return adcout

