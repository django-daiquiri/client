class Metadata(object):

    def __init__(self, client):
        self.client = client

    # schemas

    def get_schemas(self, nested=False):
        if nested:
            return self.client.get('/metadata/api/schemas/management/')
        else:
            return self.client.get('/metadata/api/schemas/')

    def get_schema(self, pk):
        return self.client.get('/metadata/api/schemas/%i/' % pk)

    def create_schema(self, data):
        return self.client.post('/metadata/api/schemas/', data)

    def update_schema(self, pk, data):
        obj = self.get_schema(pk)
        obj.update(data)
        return self.client.put('/metadata/api/schemas/%i/' % pk, obj)

    def delete_schema(self, pk):
        return self.client.delete('/metadata/api/schemas/%i/' % pk)

    # tables

    def get_tables(self):
        return self.client.get('/metadata/api/tables/')

    def get_table(self, pk):
        return self.client.get('/metadata/api/tables/%i/' % pk)

    def create_table(self, data):
        return self.client.post('/metadata/api/tables/', data)

    def update_table(self, pk, data):
        obj = self.get_table(pk)
        obj.update(data)
        return self.client.put('/metadata/api/tables/%i/' % pk, obj)

    def delete_table(self, pk):
        return self.client.delete('/metadata/api/tables/%i/' % pk)

    # columns

    def get_columns(self):
        return self.client.get('/metadata/api/columns/')

    def get_column(self, pk):
        return self.client.get('/metadata/api/columns/%i/' % pk)

    def create_column(self, data):
        return self.client.post('/metadata/api/columns/', data)

    def update_column(self, pk, data):
        obj = self.get_column(pk)
        obj.update(data)
        return self.client.put('/metadata/api/columns/%i/' % pk, obj)

    def delete_column(self, pk):
        return self.client.delete('/metadata/api/columns/%i/' % pk)

    # functions

    def get_functions(self):
        return self.client.get('/metadata/api/functions/')

    def get_function(self, pk):
        return self.client.get('/metadata/api/functions/%i/' % pk)

    def create_function(self, data):
        return self.client.post('/metadata/api/functions/', data)

    def update_function(self, pk, data):
        obj = self.get_function(pk)
        obj.update(data)
        return self.client.put('/metadata/api/functions/%i/' % pk, obj)

    def delete_function(self, pk):
        return self.client.delete('/metadata/api/functions/%i/' % pk)
