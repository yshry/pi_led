import sys
sys.path.append('../src')

from mcp3208 import Mcp3208
from servo import Servo
from time import sleep

myservo = Servo(18, 0, 4095, 3.5, 10.0, False)
mymcp = Mcp3208(11, 10, 9, 8)
myservo.setclock(50.0)

try:
	while True:
		inputVal0 = mymcp.readadc(0)
		print inputVal0
		myservo.servo_write(inputVal0)
		sleep(0.2)
except KeyboardInterrupt:
	pass


