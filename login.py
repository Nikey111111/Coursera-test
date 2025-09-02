import hashlib
import tkinter as tk
from tkinter import messagebox

# Simple user database with SHA-256 hashed passwords
# Format: 'username': {'password_hash': 'hash', 'email': 'user@example.com'}
USERS = {
    'admin': {
        'password_hash': 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f',
        'email': 'admin@example.com'
    }
}

def hash_password(password: str) -> str:
    """Return the SHA-256 hash of the provided password."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def verify_login(username: str, password: str) -> bool:
    """Verify if the username and password match the stored credentials."""
    user_data = USERS.get(username)
    if not user_data:
        return False
    return user_data['password_hash'] == hash_password(password)


class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("User Login")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Create a frame to hold the form elements
        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        self.title_label = tk.Label(self.frame, text="Login Form", font=("Arial", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="w")
        
        # Username
        self.username_label = tk.Label(self.frame, text="Username:", font=("Arial", 12))
        self.username_label.grid(row=1, column=0, sticky="w", pady=5)
        self.username_entry = tk.Entry(self.frame, font=("Arial", 12), width=25)
        self.username_entry.grid(row=1, column=1, sticky="w", pady=5)
        
        # Password
        self.password_label = tk.Label(self.frame, text="Password:", font=("Arial", 12))
        self.password_label.grid(row=2, column=0, sticky="w", pady=5)
        self.password_entry = tk.Entry(self.frame, font=("Arial", 12), width=25, show="*")
        self.password_entry.grid(row=2, column=1, sticky="w", pady=5)
        
        # Email
        self.email_label = tk.Label(self.frame, text="Email:", font=("Arial", 12))
        self.email_label.grid(row=3, column=0, sticky="w", pady=5)
        self.email_entry = tk.Entry(self.frame, font=("Arial", 12), width=25)
        self.email_entry.grid(row=3, column=1, sticky="w", pady=5)
        
        # Buttons frame
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.grid(row=4, column=0, columnspan=2, pady=(20, 0))
        
        # Login button
        self.login_button = tk.Button(
            self.button_frame, 
            text="Login", 
            font=("Arial", 12),
            width=10,
            command=self.login
        )
        self.login_button.grid(row=0, column=0, padx=10)
        
        # Cancel button
        self.cancel_button = tk.Button(
            self.button_frame, 
            text="Cancel", 
            font=("Arial", 12),
            width=10,
            command=self.root.destroy
        )
        self.cancel_button.grid(row=0, column=1, padx=10)
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        
        # Validate inputs
        if not username or not password or not email:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        # Validate email format (basic check)
        if '@' not in email or '.' not in email:
            messagebox.showerror("Error", "Please enter a valid email address!")
            return
        
        # Check credentials
        if verify_login(username, password):
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password!")


if __name__ == '__main__':
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()

