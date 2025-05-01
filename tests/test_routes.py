import json
import pytest

def test_index_route(client):
    """Test the index route returns the index.html template."""
    response = client.get('/')
    assert response.status_code == 200