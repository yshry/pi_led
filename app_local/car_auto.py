import os
import sys
sys.path.append('../src')

from gpiopin import Gpiopin
from pisocket import Pisocket
import json
import time
from car_dict_thread_auto import DistanceSensorThreadAuto

mygpio = [Gpiopin(23), Gpiopin(24), Gpiopin(20), Gpiopin(21)]

myport = 10080
mysocket = Pisocket(myport , 1)

for i in range(0,4):
	mygpio[i].pwm_on(50,0)

enforce = False

dist_th = DistanceSensorThreadAuto(0, 1100, 800, myport)
dist_th.start()

try:
	while True:
		print "waiting for connection"
		json_dict = mysocket.wait_and_accept()
		json_keys = json_dict.keys
		
		direction = ''
		tmp_enforce = ''
		for key,value in json_dict.items():
			if key == 'direction':
				direction = value
			elif key == 'enforce':
				tmp_enforce = value
	
                if tmp_enforce =='cancel':
			enforce = False
		
		if enforce:
			continue

		if direction=='neutral':
			#print 'neutral'
			for i in range(0,4):
				mygpio[i].pwm_change_duty(0)
		elif direction=='stop':
			#print 'stop'
			for i in range(0,4):
				#mygpio[i].pwm_change_duty(70)
				mygpio[i].pwm_change_duty(0)
		#elif direction =='forward':
		elif direction == 'backward':
			#print 'forward'
			for i in (0,2):
                        	mygpio[i].pwm_change_duty(0)
                        	mygpio[i+1].pwm_change_duty(70)
                #elif direction =='backward':
		elif direction == 'forward':
                        #print 'backward'
                        for i in (0,2):
                                mygpio[i].pwm_change_duty(70)
                                mygpio[i+1].pwm_change_duty(0)
                #elif direction =='right':
		elif direction == 'left':
                        #print 'left'
                        mygpio[0].pwm_change_duty(0)
                        mygpio[1].pwm_change_duty(70)
                        mygpio[2].pwm_change_duty(30)
                        #mygpio[2].pwm_change_duty(0)
			mygpio[3].pwm_change_duty(0)
                elif direction == 'right':
		#elif direction =='left':
                        #print 'right'
                        mygpio[0].pwm_change_duty(30)
                        mygpio[1].pwm_change_duty(0)
                        mygpio[2].pwm_change_duty(0)
                        mygpio[3].pwm_change_duty(70)
		print json_dict
		
                if tmp_enforce == 'enforce':
                        enforce = True

except KeyboardInterrupt:
	dist_th.stop()
	join()
	pass
