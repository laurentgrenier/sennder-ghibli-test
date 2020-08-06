from src.app import create_app
import pytest


@pytest.fixture
def client():
    client = create_app().test_client()
    return client
