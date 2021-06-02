import pytest


pytestmark = pytest.mark.info

def test_uploads(user_client):
    response = user_client.get("/api/info")
    assert response.status_code == 200
