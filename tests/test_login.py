import login

def test_login_success():
    assert login.verify_login('admin', 'password123')

def test_login_fail_username():
    assert not login.verify_login('unknown', 'password123')

def test_login_fail_password():
    assert not login.verify_login('admin', 'wrongpassword')
