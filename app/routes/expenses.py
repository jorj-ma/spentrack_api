from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Expense, Category
from datetime import datetime

expenses_bp = Blueprint("expenses", __name__)


@expenses_bp.route("", methods=["GET"])
@jwt_required()
def get_expenses():
    current_user_id = get_jwt_identity()
    expenses = (
        Expense.query.filter_by(user_id=current_user_id)
        .order_by(Expense.date.desc())
        .all()
    )

    output = []
    for exp in expenses:
        output.append(
            {
                "id": exp.id,
                "amount": float(exp.amount),
                "description": exp.description,
                "date": exp.date.strftime("%Y-%m-%d"),
                "category": exp.category.name if exp.category else "Uncategorized",
            }
        )
    return jsonify(output), 200


@expenses_bp.route("", methods=["POST"])
@jwt_required()
def add_expense():
    current_user_id = get_jwt_identity()
    data = request.get_json() or {}

    if "amount" not in data or "category_id" not in data:
        return jsonify({"error": "Amount and Category ID are required"}), 400

    try:
        date_obj = (
            datetime.strptime(data.get("date"), "%Y-%m-%d").date()
            if data.get("date")
            else datetime.utcnow().date()
        )

        new_expense = Expense(
            user_id=current_user_id,
            category_id=data["category_id"],
            amount=data["amount"],
            description=data.get("description"),
            date=date_obj,
        )
        db.session.add(new_expense)
        db.session.commit()
        return (
            jsonify({"message": "Expense added successfully", "id": new_expense.id}),
            201,
        )
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


@expenses_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_expense(id):
    current_user_id = get_jwt_identity()
    expense = Expense.query.filter_by(id=id, user_id=current_user_id).first_or_404()
    data = request.get_json() or {}

    try:
        if "amount" in data:
            expense.amount = data["amount"]
        if "category_id" in data:
            expense.category_id = data["category_id"]
        if "description" in data:
            expense.description = data["description"]
        if "date" in data:
            expense.date = datetime.strptime(data["date"], "%Y-%m-%d").date()

        db.session.commit()
        return jsonify({"message": "Expense updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


@expenses_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_expense(id):
    current_user_id = get_jwt_identity()
    expense = Expense.query.filter_by(id=id, user_id=current_user_id).first_or_404()

    db.session.delete(expense)
    db.session.commit()
    return jsonify({"message": "Expense deleted successfully"}), 200
