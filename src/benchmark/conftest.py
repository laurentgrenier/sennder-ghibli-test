import pytest
import sys
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)
from app import create_app

@pytest.fixture
def client():
    client = create_app().test_client()
    return client
