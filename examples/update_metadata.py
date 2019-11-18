import yaml
from daiquiri_client import Client

DAIQUIRI_URL = 'http://localhost:8000'
TOKEN = ''

with open('update_metadata.yml') as f:
    local_schemas = yaml.safe_load(f.read())

client = Client(DAIQUIRI_URL, TOKEN)

for remote_schema in client.metadata.get_schemas(nested=True):
    for local_schema in local_schemas:
        if remote_schema['name'] == local_schema['name']:
            client.metadata.update_schema(remote_schema['id'], local_schema)

            for remote_table in remote_schema['tables']:
                for local_table in local_schema['tables']:

                    if remote_table['name'] == local_table['name']:
                        client.metadata.update_table(remote_table['id'], local_table)

                        for remote_column in remote_table['columns']:
                            for local_column in local_table['columns']:

                                if remote_column['name'] == local_column['name']:
                                    client.metadata.update_column(remote_column['id'], local_column)
