import sys
sys.path.append('../src')
import threading

from mcp3208 import Mcp3208
from pisocket import sendjson
from time import sleep

mymcp = Mcp3208(11, 10, 9, 8)
enforce = False

class DistanceSensorThreadAuto(threading.Thread):
	def __init__ (self, dict_index, alert_on_value, alert_off_value, send_port):
		super(DistanceSensorThreadAuto, self).__init__()
		self.__aon = alert_on_value
		self.__aoff = alert_off_value
		self.__mcp = Mcp3208(11,10,9,8)
		self.__dindex = dict_index
		#self.__enforce = False
		self.__send_port = send_port
		self.__stop = False
		self.__previous_forward = False

	def __getvalue(self):
		return self.__mcp.readadc(self.__dindex)	

	def stop(self):
		self.__stop = True
	
	def run(self):
		try:
			while not self.__stop:
				value = self.__getvalue()
				print value
				if value > self.__aon and self.__previous_forward:
					print "turn left"
					json_dict = {'direction': 'left', 'enforce': 'cancel'}
					complete = sendjson('localhost', self.__send_port, json_dict)
					#self.__enforce = True
					self.__previous_forward = False
					print "send order to turn right"
				elif value < self.__aoff and not self.__previous_forward:
					print "move straight"
					json_dict = {'direction': 'forward', 'enforce': 'cancel'}
					complete = sendjson('localhost', self.__send_port, json_dict)
					#self.__enforce = False
					self.__previous_forward = True
					print "send order to go forward"
				sleep(0.2)	
		except KeyboardInterrupt:
			pass
