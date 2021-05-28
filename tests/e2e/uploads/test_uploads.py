import pytest


pytestmark = pytest.mark.uploads

def test_uploads(user_client):
    response = user_client.get("/api/uploads")
    print(response.json())
    assert response.status_code == 200
