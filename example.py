import yalegatewayservicemetrics
import os

# "api" name can be whatever is most convenient for your program
api = yalegatewayservicemetrics.YaleGatewayServiceMetrics(os.environ['YALE_API_KEY'])

print(api.service_name())
