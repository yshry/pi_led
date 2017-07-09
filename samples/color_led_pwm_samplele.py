import sys
sys.path.append('../src')

from led import Led
from mcp3208 import Mcp3208
from time import sleep

myled = (Led(21), Led(20),  Led(16))

mymcp = Mcp3208(11, 10, 9, 8)

for i in range(3):
	myled[i].pwm_on(50)

try:
	while True:
		inputVal0 = mymcp.readadc(0)
		#base_duty = (inputVal0 - 1000)/((3000 - 1000)/100)
		base_duty = inputVal0 *100 / 4095
		duty = [0,0,0]
		if base_duty > 0:
			duty[1] = base_duty
			duty[2] = 100 -base_duty
			duty[0] = base_duty*2 if base_duty<50 else 100 - ((base_duty-50)*2)
		print "%i, %i" %(inputVal0, base_duty)
		
		for i in range(3):
			myled[i].pwm_change_duty(duty[i])
		sleep(0.05)
except KeyboardInterrupt:
	pass
for i in range(3):
	myled[i].pwm_off()
	
