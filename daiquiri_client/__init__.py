import requests

from auth import Auth
from metadata import Metadata


class Client(object):

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            'Authorization': 'Token %s' % token
        }

        self.auth = Auth(self)
        self.metadata = Metadata(self)

    def get(self, url):
        response = requests.get(self.base_url + url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def post(self, url, data):
        response = requests.post(self.base_url + url, data, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def put(self, url, data):
        response = requests.put(self.base_url + url, data, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def delete(self, url):
        response = requests.delete(self.base_url + url, headers=self.headers)
        response.raise_for_status()
        return response.json()
