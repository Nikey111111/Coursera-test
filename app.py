from flask import Flask, request, jsonify, send_from_directory, redirect, url_for, session
import os
import login  # Import the existing login module

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key in production

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return send_from_directory('.', 'login_form.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('index'))
    return f'''
    <h1>Welcome, {session['username']}!</h1>
    <p>You have successfully logged in.</p>
    <a href="/logout">Logout</a>
    '''

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if login.verify_login(username, password):
        session['username'] = username
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password'})

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

