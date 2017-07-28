import os
import sys
sys.path.append('../src')

from gpiopin import Gpiopin
from pisocket import Pisocket
import json
import time

mygpio = [Gpiopin(23), Gpiopin(24), Gpiopin(20), Gpiopin(21)]

mysocket = Pisocket(10080,1)

for i in range(0,4):
	mygpio[i].pwm_on(50,0)

try:
	while True:
		json_dict = mysocket.wait_and_accept()
		direction= json_dict['direction']
		if direction=='neutral':
			print 'neutral'
			for i in range(0,4):
				mygpio[i].pwm_change_duty(0)
		elif direction=='stop':
			print 'stop'
			for i in range(0,4):
				mygpio[i].pwm_change_duty(70)
		elif direction =='forward':
			print 'forward'
			for i in (0,2):
                        	mygpio[i].pwm_change_duty(0)
                        	mygpio[i+1].pwm_change_duty(70)
                elif direction =='back':
                        print 'back'
                        for i in (0,2):
                                mygpio[i].pwm_change_duty(70)
                                mygpio[i+1].pwm_change_duty(0)
                elif direction =='left':
                        print 'left'
                        mygpio[0].pwm_change_duty(0)
                        mygpio[1].pwm_change_duty(70)
                        mygpio[2].pwm_change_duty(70)
                        mygpio[3].pwm_change_duty(0)
                elif direction =='right':
                        print 'right'
                        mygpio[0].pwm_change_duty(70)
                        mygpio[1].pwm_change_duty(0)
                        mygpio[2].pwm_change_duty(0)
                        mygpio[3].pwm_change_duty(70)
		print json_dict
except KeyboardInterrupt:
	pass
