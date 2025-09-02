# Login System

A simple login system with a web-based login form.

## Features

- Web-based login form with HTML, CSS, and JavaScript
- Flask backend for handling authentication
- Integration with existing login verification logic
- Session management for logged-in users
- Responsive design

## Setup and Installation

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Access the login form at http://localhost:3000

## Default Credentials

- Username: admin
- Password: password123

## Testing

Run the tests using pytest:
```
pytest
```

## Implementation Details

- The login form is implemented as a responsive HTML page with CSS styling
- Client-side validation ensures required fields are filled
- Server-side authentication uses the existing SHA-256 hashing mechanism
- Flask sessions maintain user login state
- RESTful API endpoint for login authentication

