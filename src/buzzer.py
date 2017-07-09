import RPi.GPIO as GPIO
import pwmo
import wiringpi

class Buzzer(pwmo.Pwmo):
	
	#scale = {'c':190, 'd':240, 'e':265, 'f':315, 'g':365, 'a':390, 'b':415}

	scale = {'c':261.6, 'd':293.7, 'e':329.6, 'f':349.2, 'g':392, 'a':440, 'b':493.9}
	silent = 0


	def __init__(self, num):
		super(Buzzer, self).__init__(num)
		self.__num = num
		wiringpi.softToneCreate(self.__num)
	def softtonewrite(self, tone, mul):
		tmptone = int(self.scale[tone] * mul)
		wiringpi.softToneWrite(self.__num, tmptone)
	def softtonewrite_hertz(self, tone):
		wiringpi.softToneWrite(self.__num, tone)
	def softtonestop(self):
		self.softtonewrite_hertz(self.silent)
