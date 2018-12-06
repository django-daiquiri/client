import requests
import simplejson

from .auth import Auth
from .metadata import Metadata
from .query import Query
from .tap import Tap


class Client(object):

    def __init__(self, base_url, token=None):
        self.base_url = base_url

        self.headers = {}
        if token:
            self.headers['Authorization'] = 'Token %s' % token

        self.auth = Auth(self)
        self.metadata = Metadata(self)
        self.query = Query(self)
        self.tap = Tap(self)

    def get(self, url, params={}, json=True):
        response = requests.get(self.base_url + url, params=params, headers=self.headers)
        response.raise_for_status()
        return response.json() if json else response.text

    def post(self, url, data, json=True):
        response = requests.post(self.base_url + url, data, headers=self.headers)

        try:
            response.raise_for_status()
            return response.json() if json else response.text
        except requests.exceptions.HTTPError as e:
            try:
                print(response.json() if json else response.text)
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

    def patch(self, url, data):
        response = requests.patch(self.base_url + url, json=data, headers=self.headers)

        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(response.json())
            raise e

    def delete(self, url):
        response = requests.delete(self.base_url + url, headers=self.headers)
        response.raise_for_status()
