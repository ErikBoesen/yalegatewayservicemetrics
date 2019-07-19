import requests
import re



class YaleGatewayServiceMetrics:
    API_TARGET = 'https://gw.its.yale.edu/soa-gateway/Metrics/GatewayServiceMetrics'

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get(self, params: dict = {}):
        """
        Make a GET request to the API.

        :param params: dictionary of custom params to add to request.
        """
        params.update({
            'apikey': self.api_key,
            'environment': 'Production',
        })
        request = requests.get(self.API_TARGET, params=params, headers={'Accept': 'application/json'})
        if request.ok:
            return request.json()
        else:
            # TODO: Can we be more helpful?
            raise Exception('API request failed. Data returned: ' + request.text)

    def service_name(self, request_url):
        return self.get({
            'type': 'servicename',
            'requesturl': request_url,
        })

    def request_url(self, service_name):


    def test(self):
        return self.get({
            'type': 'summary',
            'service': 'EnergyData',
        })
