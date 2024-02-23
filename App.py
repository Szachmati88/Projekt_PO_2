from flask import Flask, jsonify, request
from data_layer import UserDB
from User_logic import UserLogic

app = Flask(__name__)
user_db = UserDB()
user_logic = UserLogic(user_db)


@app.route('/users', methods=['GET'])
def get_users():
    users = user_logic.get_users()
    return jsonify(users), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_logic.get_user(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    created_user = user_logic.create_user(data)
    if created_user:
        return jsonify(created_user), 201
    else:
        return jsonify({"error": "Invalid user data"}), 400


@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    data = request.json
    updated_user = user_logic.update_user(user_id, data)
    if updated_user:
        return jsonify(updated_user), 200
    else:
        return jsonify({"error": "User not found or invalid data"}), 404


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted = user_logic.delete_user(user_id)
    if deleted:
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
