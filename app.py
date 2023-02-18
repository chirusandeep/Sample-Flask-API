from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample route to get a list of users in JSON format
@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {'id': 1, 'name': 'Alice', 'age': 25},
        {'id': 2, 'name': 'Bob', 'age': 30},
        {'id': 3, 'name': 'Charlie', 'age': 35},
    ]
    return jsonify(users)

# Sample route to get details of a specific user in JSON format
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = {
        1: {'id': 1, 'name': 'Alice', 'age': 25},
        2: {'id': 2, 'name': 'Bob', 'age': 30},
        3: {'id': 3, 'name': 'Charlie', 'age': 35},
    }
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

# Sample route to create a new user in JSON format
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    # Add validation to ensure name and age are provided
    user = {'id': 4, 'name': name, 'age': age}
    return jsonify(user)

# Sample route to update an existing user in JSON format
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    name = data.get('name')
    age = data.get('age')
    # Add validation to ensure name and age are provided
    users = {
        1: {'id': 1, 'name': 'Alice', 'age': 25},
        2: {'id': 2, 'name': 'Bob', 'age': 30},
        3: {'id': 3, 'name': 'Charlie', 'age': 35},
    }
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    user['name'] = name
    user['age'] = age
    return jsonify(user)

# Sample route to delete an existing user in JSON format
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = {
        1: {'id': 1, 'name': 'Alice', 'age': 25},
        2: {'id': 2, 'name': 'Bob', 'age': 30},
        3: {'id': 3, 'name': 'Charlie', 'age': 35},
    }
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    del users[user_id]
    return jsonify(user)

if __name__ == '__main__':
    app.run()
