import sys
sys.path.append('./src')

from led import Led
#import RPi.GPIO as GPIO
import time

start = time.time()
current = start
myled1 = Led(21)
myled2 = Led(2)
switch1 = False
switch2 = False
t1 = 0.0
t2 = 0.0
myled1.off()
myled2.off()
print type(start)

while (current - start) < 30:
	current = time.time()
	if (current - start -t1) > 1.0:
		t1= t1+1.0
		if switch1:
			myled1.off()
		else:
			myled1.on()
		switch1 = not switch1

	if (current - start - t2) > 0.4:
		t2 = t2+0.4
		if switch2:
			myled2.off()
		else:
			myled2.on()
		switch2 = not switch2
#GPIO.cleanup()
