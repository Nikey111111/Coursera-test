import hashlib
import getpass

# Simple user database with SHA-256 hashed passwords
USERS = {
    'admin': 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f'
}

def hash_password(password: str) -> str:
    """Return the SHA-256 hash of the provided password."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def verify_login(username: str, password: str) -> bool:
    """Verify if the username and password match the stored credentials."""
    hashed = USERS.get(username)
    return hashed == hash_password(password)


if __name__ == '__main__':
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    if verify_login(username, password):
        print('Login successful.')
    else:
        print('Invalid username or password.')
