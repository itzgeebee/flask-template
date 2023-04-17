from flask import (
    Blueprint, request, jsonify, current_app
)
from src import bcrypt

from src.db import get_db

bp = Blueprint('user', __name__, url_prefix='/auth')

@bp.route('/register/', methods=['POST'])
def register():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    user_data = request.get_json()
    name = user_data.get("name")
    email = user_data.get("email")
    password = user_data.get("password")

    try:
        cursor.execute(
            'INSERT INTO user'
            '(name,password, email) '
            'VALUES (%s, %s, %s)',
            (name, password, email))

        db.commit()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify({"error": "Something went wrong"}), 500

    user_id = cursor.lastrowid
    cursor.execute(
        'SELECT * FROM user WHERE id = %s',
        (user_id,))
    user = cursor.fetchone()
    return jsonify({"user": user}), 201


@bp.route('/', methods=['GET'])
def get_users():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute('SELECT * FROM user')
        users = cursor.fetchall()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify({"error": "Something went wrong"}), 500

    return jsonify({"users": users}), 200

@bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute('SELECT * FROM user WHERE id = %s', (id,))
        user = cursor.fetchone()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify({"error": "Something went wrong"}), 500

    return jsonify({"user": user}), 200


@bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    user_data = request.get_json()
    name = user_data.get("name")
    email = user_data.get("email")
    password = user_data.get("password")

    try:
        cursor.execute(
            'UPDATE user SET name = %s, email = %s, password = %s WHERE id = %s',
            (name, email, password, id))
        db.commit()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify({"error": "Something went wrong"}), 500

    cursor.execute(
        'SELECT * FROM user WHERE id = %s',
        (id,))
    user = cursor.fetchone()
    return jsonify({"user": user}), 200








