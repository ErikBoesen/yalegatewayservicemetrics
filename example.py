import yalegatewayservicemetrics
import os
from pprint import pprint

# "api" name can be whatever is most convenient for your program
api = yalegatewayservicemetrics.API(os.environ['YALE_API_KEY'])

print("Converting URL to service name: " + api.service_name('/soa-gateway/energy/data'))
print("Converting name back to URL: " + api.request_url('EnergyData'))
print("Getting a full URL from just the path: " + api.endpoint('EnergyData'))
print("Getting actual records:")
print(api.service('Laundry-school').records())
