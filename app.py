from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    mobile_number = request.form.get('mobile_number')
    password = request.form.get('password')
    role = request.form.get('role')
    
    # Dummy validation for login
    if mobile_number == '1234567890' and password == 'password':  # Replace with real validation
        return jsonify({'status': 'success', 'message': 'Logged in successfully.'})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid credentials.'}), 401

if __name__ == '_main_':
    app.run(debug=True)  # Enable debug mode