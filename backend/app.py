from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os
from dotenv import load_dotenv
from models import db, init_db
from models.user import User
from models.schemas import user_schema, users_schema
# Charger les variables d'environnement depuis le fichier .env
load_dotenv()  

app = Flask(__name__)

# Configuration
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

# Initialiser la base de données
init_db(app)

ma = Marshmallow(app)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.json['name']
    email = request.json['email']
    new_user = User(name, email)
    db.session.add(new_user)
    db.session.commit()
    # serialize the new user
    result = user_schema.dump(new_user)
    return jsonify({"message": "User added successfully", "user": result})


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result)

@app.route('/userdetails/<id>',methods =['GET'])
def userdetails(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"})
    result = user_schema.dump(user)
    return jsonify(result)
@app.route('/update_user/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    name = request.json.get('name', user.name)
    email = request.json.get('email', user.email)

    user.name = name
    user.email = email

    db.session.commit()

    result = user_schema.dump(user)
    return jsonify({"message": "User updated successfully", "user": result})

@app.route('/delete_user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"})

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"})
# Enable CORS for all domains
CORS(app) 

if __name__ == "__main__":
    app.run(debug=True)
