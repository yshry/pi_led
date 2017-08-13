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
		self.__unit = 0.00875
		self.change_range('250dps')

	def __del__(self):
		self.change_range('250dps')		

	def __s16(self, value):
		if (value & 0x8000) == 0:
			return value
		else:
			return ((~value & 0xffff) + 1) * -1

	def change_range(self, range):
		if range == '250dps':
			self.__bus.write_byte_data(self.__address, 0x23, 0x00)
			self.__unit = 0.00875
		elif range == '500dps':
			self.__bus.write_byte_data(self.__address, 0x23, 0x10)
			self.__unit = 0.0175
		elif range == '2000dps':
			self.__bus.write_byte_data(self.__address, 0x23, 0x20)
			self.__unit = 0.07
		else:
			print ('Lis3dh.change_range() given wrong range value.')
			print ('range data must be 250dps, 500dps, or 2000 dps.')

	def read_out(self, address_l, address_h ):
		value_l = self.__bus.read_byte_data(self.__address, address_l)
		value_h = self.__bus.read_byte_data(self.__address, address_h)
		value = value_h << 8 | value_h
		return value

	def read(self):
		out_x = self.__s16(self.read_out(0x28, 0x29)) * self.__unit
		out_y = self.__s16(self.read_out(0x2a, 0x2b)) * self.__unit
		out_z = self.__s16(self.read_out(0x2c, 0x2d)) * self.__unit
		return out_x, out_y, out_z
