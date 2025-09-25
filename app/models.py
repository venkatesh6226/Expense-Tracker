from datetime import datetime, timezone, timedelta
from flask_sqlalchemy import SQLAlchemy
from app import db

class Salary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False, default=0.0)
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone(timedelta(hours=5, minutes=30))), onupdate=lambda: datetime.now(timezone(timedelta(hours=5, minutes=30))))
    
    def __repr__(self):
        return f'<Salary {self.amount}>'

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Expense {self.amount} - {self.category}>'

class Saving(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Saving {self.amount}>'

class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    investment_type = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Investment {self.amount} - {self.investment_type}>'