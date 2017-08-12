import smbus

class L3gd20:
	def __init__(self, bus_number, address):
		self.__bus = smbus.SMBus(bus_number)
		self.__address = address
		#read WHO_AM_I
		whoami = self.__bus.read_byte_data(self.__address, 0x0F)
		if whoami == 0xd4:
			print 'WHO_AM_I success: %x' % whoami
		else:
			err_str =  'WHO_AM_I failed: %x' % whoami	
			print err_str
			raise ValueError(err_str)
		#write CTRL_REG1
		self.__bus.write_byte_data(self.__address, 0x20, 0x0F)
#	def __del__(self):
#

	def read_x(self):
		value = self.__bus.read_word_data(self.__address, 0x28)
		return value
