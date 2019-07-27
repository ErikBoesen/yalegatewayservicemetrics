import yalegatewayservicemetrics
import os
from pprint import pprint

# 'api' name can be whatever is most convenient for your program
api = yalegatewayservicemetrics.API(os.environ['YALE_API_KEY'])

print('Requesting an invalid service:')
print(api.service_name('aoisdiasd'))
print('Requesting a valid service:')
service = api.service('Laundry-room')
print(service.detail(start_date='2000-01-01', to_date='2000-01-02'))
print('Getting summary records:')
service = api.service('Laundry-school')
print(service.summary(user=os.environ['YALE_API_KEY']))
print('Getting detailed records:')
print(len(service.detail()))
print('Now a few helper methods...')
print('Converting URL to service name: ' + api.service_name('/soa-gateway/energy/data'))
print('Converting name back to URL: ' + api.request_url('EnergyData'))
print('Getting a full URL from just the path: ' + api.endpoint('EnergyData'))
