import sys
sys.path.append('../src')
import threading

from mcp3208 import Mcp3208
from pisocket import sendjson
from time import sleep

mymcp = Mcp3208(11, 10, 9, 8)
enforce = False

class DistanceSensorThread(threading.Thread):
	def __init__ (self, dict_index, alert_on_value, alert_off_value, send_port):
		super(DistanceSensorThread, self).__init__()
		self.__aon = alert_on_value
		self.__aoff = alert_off_value
		self.__mcp = Mcp3208(11,10,9,8)
		self.__dindex = dict_index
		self.__enforce = False
		self.__send_port = send_port
		self.__stop = False

	def __getvalue(self):
		return self.__mcp.readadc(self.__dindex)	

	def stop(self):
		self.__stop = True
	
	def run(self):
		try:
			while not self.__stop:
				value = self.__getvalue()
				if not self.__enforce:
					if value > self.__aon:
						json_dict = {'direction': 'backward', 'enforce': 'enforce'}
						complete = sendjson('localhost', self.__send_port, json_dict)
						self.__enforce = True
				elif self.__enforce:
					if value <self.__aoff:
						json_dict = {'direction': 'stop', 'enforce': 'cancel'}
						complete = sendjson('localhost', self.__send_port, json_dict)
						self.__enforce = False
				sleep(0.2)	
		except KeyboardInterrupt:
			pass
