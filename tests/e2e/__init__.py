from fastapi.testclient import TestClient


class CustomClient(TestClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Set authorization headers 
    def get_headers(self):
        access_token = self.user.access_token
        if access_token and not access_token.startswith('Bearer '):
            access_token = f'Bearer {access_token}'

        headers = {
            'Authorization': access_token,
        }
        return headers

    # Overriden request method, sets authorization headers
    def request(self, *args, **kwargs):
        """
            *args
                method, url,
            **kwargs
            
            params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None
        """
        headers = self.get_headers()
        kwargs.update({"headers": headers})
        return super().request(*args, **kwargs)


# MockUser for mocking a complex User class
class MockUser():
    def __init__(self, access_token):
        self.access_token = access_token
