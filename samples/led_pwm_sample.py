import sys
sys.path.append('../src')

from led import Led
from mcp3208 import Mcp3208
from time import sleep

myled = Led(21)
mymcp = Mcp3208(11, 10, 9, 8)
myled.pwm_on(50)

try:
	while True:
		inputVal0 = mymcp.readadc(0)
		duty = (inputVal0 - 1000)/((3000 - 1000)/100)
		if duty <0:
			duty= 0
		print "%i, %i" %(inputVal0, duty)
		myled.pwm_change_duty(duty)
		sleep(0.2)
except KeyboardInterrupt:
	pass

myled.pwm_off()
	
