Daiquiri Client
===============

Daiquiri Client is a python library meant to be used with the Daiquiri Framework.

Daiquiri can be downloaded from [https://github.com/aipescience/django-daiquiri](https://github.com/aipescience/django-daiquiri).

Daiquiri Client provides a set of functions which can be used to use the API of a Daiquiri powered website inside a script. The nessesarry http requests are abstracted in a transparent way.

A script for getting the emails of all users using Daiquiri Client could look like this:

```python
from daiquiri_client import Client

client = Client('http://localhost:8000', '6f3d17e17e46c8e188b4c285ebb53a3fa3ce98c6')

for profile in client.auth.get_profiles():
    print(profile['user']['email'])
```
