from tests.e2e import CustomClient
from api.main import app
import pytest

# Create CustomClient by passing app to fastapi's TestClient
@pytest.fixture(scope='function')
def function_client():
    return CustomClient(app)
