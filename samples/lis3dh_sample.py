import sys
sys.path.append('../src')

from time import sleep
from lis3dh import Lis3dh

m_sensor = Lis3dh(1, 0x18)

#m_sensor.change_scale('8g')

try:
	while True:
		out_x, out_y, out_z =  m_sensor.read()
		#print '%s, %s, %s' % (bin(out_x), bin(out_y), bin(out_z))
		print '%f, %f, %f' % (out_x, out_y, out_z)
		print '%s, %s, %s' % (type(out_x), type(out_y), type(out_z))
		sleep(0.5)
except KeyboardInterrupt:
	pass

