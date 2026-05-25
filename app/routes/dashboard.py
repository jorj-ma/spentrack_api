from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Expense, Budget, Category
from sqlalchemy import func

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/summary", methods=["GET"])
@jwt_required()
def get_dashboard_summary():
    current_user_id = get_jwt_identity()

    budget = Budget.query.filter_by(user_id=current_user_id).first()
    if not budget:
        budget = Budget(user_id=current_user_id, monthly_limit=1000.00)
        db.session.add(budget)
        db.session.commit()
    limit = float(budget.monthly_limit)

    total_spent = (
        db.session.query(func.sum(Expense.amount))
        .filter(Expense.user_id == current_user_id)
        .scalar()
        or 0.0
    )

    recent_expenses = (
        Expense.query.filter_by(user_id=current_user_id)
        .order_by(Expense.date.desc())
        .limit(5)
        .all()
    )

    expense_list = [
        {
            "id": e.id,
            "date": e.date.isoformat(),
            "category_name": e.category.name,
            "description": e.description,
            "amount": float(e.amount),
        }
        for e in recent_expenses
    ]

    category_data = (
        db.session.query(Category.name, func.sum(Expense.amount))
        .join(Expense)
        .filter(Expense.user_id == current_user_id)
        .group_by(Category.name)
        .all()
    )

    return (
        jsonify(
            {
                "totalSpent": float(total_spent),
                "remainingBudget": max(0.0, limit - float(total_spent)),
                "pieChartData": [
                    {"category": name, "value": float(amt)}
                    for name, amt in category_data
                ],
                "recentExpenses": expense_list,
            }
        ),
        200,
    )
