import sys
sys.path.append('../src')

from gpiopin import Gpiopin
from mcp3208 import Mcp3208
from time import sleep

mygpio0 = Gpiopin(24)
mygpio1 = Gpiopin(25)

mymcp = Mcp3208(11, 10, 9, 8)

mygpio0.pwm_on(50,0)
mygpio1.pwm_on(50,0)

try:
	while True:
		inputVal0 = mymcp.readadc(0)
		
		if inputVal0 > 100 and inputVal0 <2048:
			mygpio1.pwm_change_duty(0)
			duty = (2048 - inputVal0) * 70 / 2048
			mygpio0.pwm_change_duty(duty)

                elif inputVal0 >= 2048 and inputVal0 <4000:
                        mygpio0.pwm_change_duty(0)
                        duty = (inputVal0-2048) * 70 / 2048
                        mygpio1.pwm_change_duty(duty)
		print (inputVal0)
		sleep(0.5)
except KeyboardInterrupt:
	pass


