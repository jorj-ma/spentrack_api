from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import User

user_bp = Blueprint("user", __name__)


@user_bp.route("/profile", methods=["GET", "PUT"])
@jwt_required()
def manage_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    if request.method == "GET":
        return jsonify({"username": user.name, "email": user.email}), 200

    if request.method == "PUT":
        data = request.get_json()
        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)
        db.session.commit()
        return jsonify({"message": "Profile updated!"}), 200


@user_bp.route("/profile", methods=["DELETE"])
@jwt_required()
def delete_account():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    db.session.delete(
        user
    )
    db.session.commit()
    return jsonify({"message": "Account deleted successfully"}), 200
