class Auth():

    def __init__(self, client):
        self.client = client

    def fetch_profiles(self):
        return self.client.get('/auth/api/profiles/')['results']
