import socket
import json

class Pisocket:
	def __init__(self, port, queue_num):
		self.__host = 'localhost'
		self.__port = port
		self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

		self.__server.bind((self.__host,self.__port))
		self.__server.listen(5)
	
	def __del__(self):
		self.__server.close()

	def wait_and_accept(self):
		retval = '{}'
		try:
			clientsock, (client_address, client_port) = self.__server.accept()
			str_client_address = ('{}'.format(client_address))
			client_address = 'localhost'
			if str_client_address != '127.0.0.1':
				clientsock.sendall('invalid address')
				return '{client_address: \"invalid\"}'

                	message = clientsock.recv(1024)
                	retval=json.loads('{}'.format(message))
		
			clientsock.sendall('received: %s' % retval)
			clientsock.close()		
		except ValueError:
			pass
		return retval
	

def sendjson(host, port, json_dict, timeout = 0.1):
	try:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(timeout)
		client.connect(("localhost", 10080))
		addr = ('localhost', 10080)
		client.send(json.dumps(json_dict))
		response = client.recv(1024)
	except socket.timeout:
		return -2
	#except:
	#	import traceback
	#	print(repr(traceback.extract_stack()))
	#	return -1
	if response =="":
		return -1
	return 1
