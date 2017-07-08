import smbus

class Adt7410:
	def __init__(self, bus_number, address, register):
		self.__bus = smbus.SMBus(bus_number)
		self.__address = address
		self.__register = register 
	
#	def __del__(self):
#

	def read(self):
		word_data = self.__bus.read_word_data(self.__address, self.__register)
		data = (word_data & 0xff00) >> 8 | (word_data & 0xff) << 8
		data = data >> 3
		if data & 0x1000 == 0:
			temp = data * 0.0625
		else:
			temp = ((~data&0x1fff)+1)*-0.0625
		return temp
