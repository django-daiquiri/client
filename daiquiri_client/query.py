class Query():

    def __init__(self, client):
        self.client = client

    def get_jobs(self):
        return self.client.get('/query/api/jobs/')

    def get_job(self, pk):
        return self.client.get('/query/api/jobs/%s/' % pk)

    def create_job(self, data):
        return self.client.post('/query/api/jobs/', data)

    def update_job(self, pk, data):
        return self.client.put('/query/api/jobs/%s/' % pk, {
            'table_name': data['table_name']
        })

    def delete_job(self, pk):
        self.client.delete('/query/api/jobs/%s/' % pk)
        return {'id': pk}

    def abort_job(self, pk):
        return self.client.put('/query/api/jobs/%s/abort/' % pk, {})
