class Auth():

    def __init__(self, client):
        self.client = client

    def get_profiles(self):
        return self.client.get('/auth/api/profiles/')['results']

    def get_groups(self):
        return self.client.get('/auth/api/groups/')
