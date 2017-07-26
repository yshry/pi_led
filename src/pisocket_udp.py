import socket
import json

class Pisocket_udp:
	def __init__(self, port, queue_num):
		self.__host = 'localhost'
		self.__port = port
		self.__server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

		self.__server.bind((self.__host,self.__port))
	
	def __del__(self):
		self.__server.close()

	def wait_and_accept(self):
		message,address = self.__server.recvfrom(1024)
                
		retval=json.loads('{}'.format(message))
		return retval
	

def sendjson_udp(host, port, json_dict, timeout=0.3):
	try:
		client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		client.settimeout(timeout)
		addr = ('localhost', 10080)
		client.sendto(json.dumps(json_dict), addr)
	except:
		return -1

	return 1
