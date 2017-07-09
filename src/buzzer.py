import RPi.GPIO as GPIO

class Buzzer:
	
	def __init__(self, num, duty=0):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(num, GPIO.OUT)
		self.__num = num
		self.doremi = {'do':131, 're':147, 'mi':165, 'fa':175, 'so':196 ,'la':220, 'si':247, 'Do':262}
		self.__duty=duty
	
	def on(self, hertz):
		self.__p = GPIO.PWM(self.__num, hertz)
		self.__p.start(self.__duty)

	def change_duty(self, duty):
		self.__duty = duty
		self.__p.ChangeDutyCycle(self.__duty)

	def off(self):
		self.__p.stop()

	def sound_on(self, key, mul):
		self.__p = GPIO.PWM(self.__num, self.doremi[key]*mul)
		self.__p.start(self.__duty)
