from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulate a user database
class UserService:
    
    users = {} # e.g. {keyur:password}
    
    # @app.route('/register', methods=['POST'])
    def register(self, username, password):
        self.users[username] = password 
        return jsonify({'message': 'User registered successfully'})

    # @app.route('/login', methods=['POST'])
    def login(self, username, password):
        #Compare password with existing users
        if password == self.users[username]:
            return True
        else:
            return jsonify({'message': "Login Incorrect"})