import yalegatewayservicemetrics
import os
from pprint import pprint

# "api" name can be whatever is most convenient for your program
api = yalegatewayservicemetrics.YaleGatewayServiceMetrics(os.environ['YALE_API_KEY'])

"""
print(api.service_name('/soa-gateway/energy/data'))
print(api.request_url('EnergyData'))
print(api.endpoint('EnergyData'))
"""
pprint(api.summary('Laundry-school', user=os.environ['YALE_API_KEY']))
