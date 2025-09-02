import sys
import os
import pytest

# Add the parent directory to the path so we can import login.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from login import hash_password, verify_login, USERS

def test_hash_password():
    """Test that password hashing works correctly."""
    # Test with known password 'password123'
    expected_hash = 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f'
    assert hash_password('password123') == expected_hash

def test_verify_login_success():
    """Test successful login verification."""
    assert verify_login('admin', 'password123') == True

def test_verify_login_wrong_password():
    """Test login verification with wrong password."""
    assert verify_login('admin', 'wrongpassword') == False

def test_verify_login_nonexistent_user():
    """Test login verification with non-existent user."""
    assert verify_login('nonexistent', 'anypassword') == False

