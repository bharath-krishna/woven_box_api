from api.modules import BaseModule
from api.exceptions import APIError

class Profile(BaseModule):
    collection_name: str = 'profile'

    async def get_profile(self, user):
        return user
        
