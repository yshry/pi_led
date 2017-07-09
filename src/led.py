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

	def pwm_on(self, hertz, duty=0):
		self.__p = GPIO.PWM(self.__num, hertz)
		self.__p.start(duty)

	def pwm_change_duty(self, duty):
		self.__p.ChangeDutyCycle(duty)

	def pwm_off(self):
		self.__p.stop()
