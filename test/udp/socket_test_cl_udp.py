import sys
sys.path.append('../../src')

from pisocket_udp import sendjson_udp

json_dict = {'status': 'on'}

print sendjson_udp('localhost', 10080, json_dict)

