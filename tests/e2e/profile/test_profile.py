import pytest


pytestmark = pytest.mark.profile

def test_profile(user_client):
    response = user_client.get("/api/profile")
    print(response.json())
    assert response.status_code == 200
