import requests
import simplejson

from .auth import Auth
from .metadata import Metadata
from .query import Query


class Client(object):

    def __init__(self, base_url, token=None):
        self.base_url = base_url

        self.headers = {}
        if token:
            self.headers['Authorization'] = 'Token %s' % token

        self.auth = Auth(self)
        self.metadata = Metadata(self)
        self.query = Query(self)

    def get(self, url):
        response = requests.get(self.base_url + url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def post(self, url, data):
        response = requests.post(self.base_url + url, data, headers=self.headers)
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            try:
                print(response.json())
            except simplejson.scanner.JSONDecodeError:
                pass
            raise e

    def put(self, url, data):
        response = requests.put(self.base_url + url, data, headers=self.headers)
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(response.json())
            raise e

    def delete(self, url):
        response = requests.delete(self.base_url + url, headers=self.headers)
        response.raise_for_status()
