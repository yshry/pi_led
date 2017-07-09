import sys
sys.path.append('../src')

from mcp3208 import Mcp3208
from servo import Servo

myservo = Servo(18, 0, 4095, 3.5, 10.0, True)
mymcp = Mcp3208(11, 10, 9, 8)
myservo.setclock(50.0)

try:
	while True:
		inputVal0 = mymcp.readadc(0)
		myservo.servo_write(inputVal0)
		sleep(0.5)
except KeyboardInterrupt:
	pass


