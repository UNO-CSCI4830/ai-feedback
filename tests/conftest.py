import pytest
import sys
import os

# StackOVerflow said to do this
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app as app_module

@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    # Set testing config
    app_module.app.config.update({
        "TESTING": True,
    })
    
    # Return the app for testing
    yield app_module.app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test CLI runner for the app."""
    return app.test_cli_runner()