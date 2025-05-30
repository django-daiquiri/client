from daiquiri_client import Client
import yaml


class MetadataCLI:
    def ls(self, host: str, token: str, verbose: bool) -> dict:
        client = Client(host, token)
        metadata = client.metadata.get_schemas(nested=True)
        print(f'Metadata from "{host}":')
        for schema in metadata:
            print(schema['name'])
            if verbose:
                for table in schema['tables']:
                    print(f' - {table["name"]}')
        return metadata

    def push(
        self,
        host: str,
        token: str,
        input: str,
        schemas: 'list[str]',
        tables: 'list[str]',
        verbose: bool,
    ) -> None:
        full_metadata = []
        with open(input, 'r') as fd:
            full_metadata = yaml.load(fd, yaml.Loader)
        try:
            self._names_are_unique(full_metadata)
        except ValueError as e:
            print('Some of the objects in the input file are not unique!')
            print('The script supports only unique schemas, tables and columns!')
            print(e)
            return

        client = Client(host, token)
        remote_metadata = client.metadata.get_schemas(nested=True)
        if verbose:
            print(f'Pushing metadata to {host}')
        for remote_schema in remote_metadata:
            for local_schema in full_metadata:
                if remote_schema['name'] == local_schema['name']:
                    print(f'Schema {local_schema["name"]}')
                    client.metadata.update_schema(remote_schema['id'], local_schema)
                    for remote_table in remote_schema['tables']:
                        for local_table in local_schema['tables']:
                            if remote_table['name'] == local_table['name']:
                                print(f' - {local_table["name"]}')
                                client.metadata.update_table(remote_table['id'], local_table)
                                for remote_column in remote_table['columns']:
                                    for local_column in local_table['columns']:
                                        if remote_column['name'] == local_column['name']:
                                            client.metadata.update_column(remote_column['id'], local_column)
        if verbose:
            print('Done!')

    def pull(
        self,
        host: str,
        token: str,
        output: str,
        schemas: 'list[str]',
        tables: 'list[str]',
        verbose: bool,
    ) -> None:
        client = Client(host, token)
        sorted_metadata = client.metadata.get_schemas(nested=True)
        try:
            self._names_are_unique(sorted_metadata)
        except ValueError as e:
            print('Some of the objects are not unique! The script supports only unique schemas, tables and columns!')
            print(e)
            return
        full_metadata = []
        if verbose:
            print(f'Pulling metadata from {host}')
        for remote_schema in sorted_metadata:
            if len(schemas) == 0 or remote_schema['name'] in schemas:
                if verbose:
                    print(f'Schema: {remote_schema["name"]}')
                new_schema = client.metadata.get_schema(remote_schema['id'])
                new_schema.pop('id')
                new_schema['tables'] = []
                for remote_table in remote_schema['tables']:
                    if len(tables) == 0 or remote_table['name'] in tables:
                        if verbose:
                            print(f' - {remote_table["name"]}')
                        new_table = client.metadata.get_table(remote_table['id'])
                        new_table.pop('id')
                        new_table.pop('schema')
                        new_table['columns'] = []
                        for remote_column in remote_table['columns']:
                            new_col = client.metadata.get_column(remote_column['id'])
                            new_col.pop('id')
                            new_col.pop('table')
                            new_table['columns'].append(new_col)
                        new_schema['tables'].append(new_table)
                full_metadata.append(new_schema)
        with open(output, 'w+') as fd:
            yaml.dump(full_metadata, fd, sort_keys=False)

    def _names_are_unique(self, metadata: 'list[dict]') -> bool:
        """Checks that schema, table, and column names are unique within their respective scopes."""
        error_message = ''
        schema_names = [schema['name'] for schema in metadata]
        duplicate_schema_names = [s for s in schema_names if schema_names.count(s) > 1]
        if len(duplicate_schema_names) > 0:
            error_message += 'Duplicate schemas: ' + ', '.join(set(duplicate_schema_names)) + ';\n'
        duplicate_table_names = []
        duplicate_column_names = []
        for schema in metadata:
            table_names = [f'{schema["name"]}.{table["name"]}' for table in schema['tables']]
            duplicate_table_names.extend([t for t in table_names if table_names.count(t) > 1])
            for table in schema['tables']:
                column_names = [f'{schema["name"]}.{table["name"]}.{column["name"]}' for column in table['columns']]
                duplicate_column_names.extend([c for c in column_names if column_names.count(c) > 1])

        if len(duplicate_table_names) > 0:
            error_message += 'Duplicate tables: ' + ', '.join(set(duplicate_table_names)) + ';\n'
        if len(duplicate_column_names) > 0:
            error_message += 'Duplicate columns: ' + ', '.join(set(duplicate_column_names)) + ';\n'

        if error_message != '':
            raise ValueError(error_message)

        return True
