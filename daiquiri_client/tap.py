class Tap():

    def __init__(self, client):
        self.client = client

    def sync(self, query, query_language='ADQL'):
        return self.client.post('/tap/sync', {
            'QUERY': query,
            'LANG': query_language
        }, json=False)
