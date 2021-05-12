import pytest

from tests.e2e import CustomClient, MockUser

# Creates TestClient with user and does setting headers for requests.
@pytest.fixture(scope='function')
def user_client(function_client: CustomClient, mock_user):
    """Function scoped. Get client for a user."""
    function_client.user = mock_user
    return function_client


# Update mock_user_token with actual user's JWT token
@pytest.fixture
def mock_user_token():
    return 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6InNvbWVfbmFtZSIsImlkIjoic29tZWlkIiwiaWF0IjoxNjE5NTA1ODIxLCJleHAiOjE2MzA1MDU4MjF9.WswHF59S7iU7oonfI1gdQhcI1TzsXW1ryhjEU4WjWfk'


# Create MockUser fixture with prebuild test token
@pytest.fixture
def mock_user(mock_user_token):
    return MockUser(mock_user_token)
