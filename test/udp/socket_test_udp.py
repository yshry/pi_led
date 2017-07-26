import sys
sys.path.append('../../src')

from pisocket_udp import Pisocket_udp

mysocket = Pisocket_udp(10080, 5)

while True:
	try:
		print mysocket.wait_and_accept()
	except KeyboardInterrupt:
		break	
		#import traceback
		#print (repr(traceback.extract_stack()))
		#print sys.exc_info()
		#break
