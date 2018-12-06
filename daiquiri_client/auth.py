class Auth():

    def __init__(self, client):
        self.client = client

    def get_profiles(self):
        return self.client.get('/auth/api/profiles/', {'page_size': 10000})['results']

    def get_groups(self):
        return self.client.get('/auth/api/groups/')

    def get_group_map(self):
        return {group['id']: group['name'] for group in self.get_groups()}

    def activate_profile(self, pk):
        return self.client.put('/auth/api/profiles/%d/activate/' % pk, {})

    def update_profile_attributes(self, pk, attributes):
        return self.client.patch('/auth/api/profiles/%d/' % pk, {'attributes': attributes})
