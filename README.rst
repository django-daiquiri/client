Daiquiri Client
===============

Daiquiri Client is a python library meant to be used with the Daiquiri Framework.

Daiquiri can be downloaded from
`https://github.com/django-daiquiri/daiquiri <https://github.com/django-daiquiri/daiquiri>`_.

Daiquiri Client provides a set of functions to use the API of a Daiquiri-powered
website in a script. The necessary HTTP requests are abstracted in a transparent way.

For example, the following script gets the emails of all users:

.. code:: python

    from daiquiri_client import Client

    client = Client('http://localhost:8000', '6f3d17e17e46c8e188b4c285ebb53a3fa3ce98c6')

    for profile in client.auth.get_profiles():
        print(profile['user']['email'])
