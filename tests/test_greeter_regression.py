import pytest
from app.greeter import greet

pytestmark = pytest.mark.regression

def test_greet_basic():
    assert greet("Josh") == "Hello, Josh!"

def test_greet_trims_whitespace():
    assert greet("  Ada  ") == "Hello, Ada!"

def test_greet_default_when_empty_string():
    assert greet("") == "Hello, World!"

def test_greet_default_when_none():
    assert greet(None) == "Hello, World!"
