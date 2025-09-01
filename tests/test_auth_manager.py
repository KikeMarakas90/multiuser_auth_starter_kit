import pytest
from src.auth_manager import AuthManager

def test_create_and_validate_session():
    auth = AuthManager()
    token = auth.create_session("user123", "admin")
    decoded = auth.validate_session(token)

    assert decoded["user_id"] == "user123"
    assert decoded["role"] == "admin"

def test_has_role():
    auth = AuthManager()
    token = auth.create_session("user456", "user")
    assert auth.has_role(token, "user")
    assert not auth.has_role(token, "admin")
