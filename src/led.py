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

	def pwm_on(self, hertz, duty):
		self.__p = GPIO.PWM(self.__num, hertz)
		self.__p.ChangeDutyCycle(duty)
		self.__p.start()

	def pwm_off(self):
		self.__p.stop()
