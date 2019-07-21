import requests
import re


class Service:
    def __init__(self, _api, name, request_url):
        self._api = _api
        self.name = name
        self.request_url = request_url

    def summary(self, service_name, user=None, average=False):
        raw = self.get({
            'type': 'summary',
            'service': service_name,
            # This doesn't do anything, but pass it anyway in case that changes
            'user': user,
            # These parameters do not appear to actually do anything, but they have to be here.
            'startdate': '1950-01-01',
            'todate': '3000-01-01',
        })
        if average:
            user = 'Average All Users'
        # Compensate for the user parameter not being respected
        if user:
            return next(item for item in raw if item['user'] == user)
        return raw


class API:
    API_PATH = 'https://gw.its.yale.edu'
    ENDPOINT = '/soa-gateway/Metrics/GatewayServiceMetrics'

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
        request = requests.get(self.API_PATH + self.ENDPOINT,
                               params=params,
                               headers={'Accept': 'application/json'})
        if request.ok:
            return request.json()['ServiceMetrics']['Record']
        else:
            # TODO: Can we be more helpful?
            raise Exception('API request failed. Data returned: ' + request.text)

    def endpoint(self, service_name):
        """
        Get the full URL endpoint of an API given its name.
        """
        return self.API_PATH + self.request_url(service_name)

    def service_name(self, request_url):
        """
        Get the name of a service given its URL endpoint.
        """
        return self.get({
            'type': 'servicename',
            'requesturl': request_url,
        })['service_name']

    def request_url(self, service_name):
        """
        Get the path to a service from the API root.
        You may want to use `endpoint` instead to get the API's full endpoint URL.
        """
        return self.get({
            'type': 'servicename',
            'service': service_name,
        })['request_url']

    def service(self, identifier):
        """
        Initialize a service that you'd like to get data on.
        """
        payload = {
            'type': 'servicename',
            # Add requesturl or name to payload
            'requesturl' if '/' in identifier else 'service': identifier
        }
        response = self.get(payload)
        return Service(self, response['service_name'], response['request_url'])
