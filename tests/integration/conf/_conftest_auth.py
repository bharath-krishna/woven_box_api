from api.models.profile import FirebaseModel, UserModel
from api.models.auth import User
import pytest

from tests.integration import CustomClient, MockUser

# Creates TestClient with user and does setting headers for requests.
@pytest.fixture(scope='function')
def user_client(function_client: CustomClient, mock_user):
    """Function scoped. Get client for a user."""
    function_client.user = mock_user
    return function_client


@pytest.fixture
def mock_user_token():
    return 'mock_user_token'


@pytest.fixture
def mock_user(monkeypatch, mock_user_token):
    def mock__init__(self, *args, **kwargs):
        self.access_token = mock_user_token

    monkeypatch.setattr(User, '__init__', mock__init__)

    @classmethod
    def mock_log_user_in(cls, *args, **kwargs):        
        return UserModel(
            iss="iss",
            aud="str",
            auth_time=0,
            user_id="str",
            sub="str",
            iat=0,
            exp=0,
            email="str",
            email_verified=False,
            firebase=FirebaseModel(
                identities = {"str": ["str"]},
                sign_in_provider="str"
            ),
            uid="str",
        )

    monkeypatch.setattr(User, 'log_user_in', mock_log_user_in)

    return MockUser(mock_user_token)
