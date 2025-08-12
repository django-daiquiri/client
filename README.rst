Daiquiri Client
===============

Daiquiri Client is a python library meant to be used with the Daiquiri Framework.

Daiquiri can be downloaded from
`https://github.com/django-daiquiri/daiquiri <https://github.com/django-daiquiri/daiquiri>`_.

Daiquiri Client provides a set of functions to use the API of a Daiquiri-powered
website in a script. The necessary HTTP requests are abstracted in a transparent way.

Additionally, Daiquiri Client provides a Command Line Interface (CLI) to manage the metadata
in a terminal.

For example, the following script gets the emails of all users:

.. code:: python

    from daiquiri_client import Client

    client = Client('http://localhost:8000', '6f3d17e17e46c8e188b4c285ebb53a3fa3ce98c6')

    for profile in client.auth.get_profiles():
        print(profile['user']['email'])



Command Line Interface
----------------------


The CLI version of Daiquiri Client can be installed by cloning the 
repository and running ``pip install``


.. code:: bash

    clone https://github.com/django-daiquiri/client.git
    cd client && pip install .[cli]


**Examples**:

List all metadata

.. code:: bash

    dqclient metadata ls -h <host> -t <token>

- ``<host>``: Site url, for instance `https://gaia.aip.de`
- ``<token>``: API token that is provided by every Daqiuiri app in the user settings



Pull all metadata:

.. code:: bash

    dqclient metadata pull -h <host> -t <token> -o <output_file>

- ``<output_file>``: output yaml file, for instance `metadata.yaml`


The updated metadata can be pushed back to the Daiquiri website with:

.. code:: bash

    dqclient metadata push -h <host> -t <token> -i <input_file>



It is possible to push/pull specific metadata by choosing the schemas or tables

.. code:: bash

    dqclient metadata push -h <host> -t <token> -i <input_file> --schemas schemaname1,schemaname2 --tables tablename1



