import sys
sys.path.append('../src')

from pisocket import sendjson

json_dict = {'status': 'on'}

print sendjson('localhost', 10080, json_dict, 0.1)

