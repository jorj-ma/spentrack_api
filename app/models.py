from app import db
from datetime import datetime, timezone

class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash=db.Column(db.String(255), nullable=False)
    created_at=db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    expenses=db.relationship('Expense', backref='user', lazy=True, cascade="all, delete-orphan")

class Category(db.Model):
    __tablename__='categories'
    
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), unique=True, nullable=False)

    expenses=db.relationship('Expense', backref='category', lazy=True)

class Budget(db.Model):
    __tablename__ = 'budgets'
    
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    monthly_limit=db.Column(db.Numeric(10, 2), nullable=False)
    created_at=db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

class Expense(db.Model):
    __tablename__ = 'expenses'
    
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    category_id=db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='SET NULL'), nullable=True)
    amount=db.Column(db.Numeric(10, 2), nullable=False)
    description=db.Column(db.String(255), nullable=True)
    date=db.Column(db.Date, nullable=False, default=lambda: datetime.now(timezone.utc).date())
    created_at=db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))