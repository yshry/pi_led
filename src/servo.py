import RPi.GPIO as GPIO
import pwmo

class Servo(pwmo.Pwmo):
	def __init__(self, num, val_min, val_max, duty_min, duty_max, orientation = False):
		super(Servo, self).__init__(num)
		self.__vmin = val_min
		self.__vmax = val_max
		self.__dmin = int (duty_min * 1024.0 / 100.0)
		self.__dmax = int (duty_max * 1024.0 / 100.0)
		self.__orientation = orientation	

	def __del__(self):
		super(Servo, self).__del__()

	def servo_write(self, val):
		if self.__orientation:
			duty = int((self.__dmin - self.__dmax)*(val - self.__vmin) / (self.__vmax - self.__vmin) + self.__dmax)
		else:
			duty = int((self.__dmax - self.__dmin)*(val - self.__vmin) / (self.__vmax - self.__vmin) + self.__dmin)
		self.pwmWrite(duty)
		print duty
