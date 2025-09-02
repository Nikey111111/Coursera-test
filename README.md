# Coursera-test

This repository contains sample code.

## User Login

`login.py` provides a user login form with a graphical interface using Tkinter.

Features:
- Required fields: username, password, email
- Buttons: Login, Cancel
- Basic input validation
- Secure password handling with SHA-256 hashing

Run the script:

```bash
python3 login.py
```

Default credentials:
- username: `admin`
- password: `password123`
- email: `admin@example.com` (only for demonstration, not checked during login)

## Tests

Run tests with `pytest`:

```bash
pip install pytest
python3 -m pytest
```

