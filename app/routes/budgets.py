from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Budget, Expense
from sqlalchemy import func

budgets_bp = Blueprint('budgets', __name__)

@budgets_bp.route('/summary', methods=['GET'])
@jwt_required()
def get_summary():
    current_user_id = get_jwt_identity()
    
    budget = Budget.query.filter_by(user_id=current_user_id).order_by(Budget.created_at.desc()).first()
    limit = float(budget.monthly_limit) if budget else 0.0

    total_spent = db.session.query(func.sum(Expense.amount)).filter(Expense.user_id == current_user_id).scalar() or 0.0
    total_spent = float(total_spent)

    return jsonify({
        "monthly_limit": limit,
        "actual_spending": total_spent,
        "remaining_budget": max(0.0, limit - total_spent)
    }), 200

@budgets_bp.route('', methods=['POST'])
@jwt_required()
def set_budget():
    current_user_id = get_jwt_identity()
    data = request.get_json() or {}
    limit = data.get('monthly_limit')
    
    if limit is None:
        return jsonify({"error": "Monthly limit value is required"}), 400
        
    new_budget = Budget(user_id=current_user_id, monthly_limit=limit)
    db.session.add(new_budget)
    db.session.commit()
    return jsonify({"message": "Budget limit updated successfully"}), 200


budgets_bp = Blueprint('budgets', __name__)

@budgets_bp.route('/update', methods=['PUT'])
@jwt_required()
def update_budget():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    new_limit = data.get('monthly_limit')

    if not new_limit:
        return jsonify({"message": "Limit is required"}), 400

    budget = Budget.query.filter_by(user_id=current_user_id).first()
    
    if budget:
        budget.monthly_limit = new_limit
    else:
        budget = Budget(user_id=current_user_id, monthly_limit=new_limit)
        db.session.add(budget)
    
    db.session.commit()
    return jsonify({"message": "Budget updated successfully", "newLimit": float(new_limit)}), 200