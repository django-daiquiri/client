class Metadata(object):

    def __init__(self, client):
        self.client = client

    # databases

    def get_databases(self, nested=False):
        if nested:
            return self.client.get('/metadata/api/databases/management/')
        else:
            return self.client.get('/metadata/api/databases/')

    def get_database(self, pk):
        return self.client.get('/metadata/api/databases/%i/' % pk)

    def create_database(self, data):
        return self.client.post('/metadata/api/databases/', data)

    def update_database(self, pk, data):
        obj = self.get_database(pk)
        obj.update(data)
        return self.client.put('/metadata/api/databases/%i/' % pk, obj)

    def delete_database(self, pk):
        return self.client.delete('/metadata/api/databases/%i/' % pk)

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
