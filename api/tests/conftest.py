"""
conftest.py provides a fixture that can be used by
all tests in the api/tests directory.
"""

import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SERVER_NAME"] = "localhost:8000"

    with app.test_client() as test_client:
        yield test_client
