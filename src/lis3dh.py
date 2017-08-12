import smbus

class Lis3dh:
	def __init__(self, bus_number, address):
		self.__bus = smbus.SMBus(bus_number)
		self.__address = address
		#read WHO_AM_I
		whoami = self.__bus.read_byte_data(self.__address, 0x0F)
		if whoami == 0x33:
			print 'WHO_AM_I success: %x' % whoami
		else:
			err_str =  'WHO_AM_I failed: %x' % whoami	
			print err_str
			raise ValueError(err_str)
		#write CTRL_REG1
		self.__bus.write_byte_data(self.__address, 0x20, 0x7F)

	def __del__(self):
		self.change_scale('2g')

	def change_scale(self, scale):
		if scale == '2g':
			self.__bus.write_byte_data(self.__address, 0x23, 0x00)
		elif scale == '4g':
			self.__bus.write_byte_data(self.__address, 0x23, 0x10)
		elif scale == '8g':
			self.__bus.write_byte_data(self.__address, 0x23, 0x20)
		elif scale == '16g':
			self.__bus.write_byte_data(self.__address, 0x23, 0x30)

	def s12(self, value):
		if (value & 0x0800) == 0:
			return value
		else:
			return ((~value & 0x0fff) + 1) * -1

	def read_out(self, address_l, address_h):
		value_l = self.__bus.read_byte_data(self.__address, address_l)
		value_h = self.__bus.read_byte_data(self.__address, address_h)
		value = (value_h << 8 | value_l) >> 4
		return value

	def read(self):
		out_x = self.s12(self.read_out(0x28, 0x29))
		out_y = self.s12(self.read_out(0x2a, 0x2b))
		out_z = self.s12(self.read_out(0x2c, 0x2d))

		#out_x = self.read_out(0x28, 0x29)
		#out_y = self.read_out(0x2a, 0x2b)
		#out_z = self.read_out(0x2c, 0x2d)
		return out_x, out_y, out_z
