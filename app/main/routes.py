from flask import render_template
from app.main import bp

@bp.route('/')
@bp.route('/dashboard')
def dashboard():
    return render_template('main/dashboard.html',
                         salary_amount=0,
                         total_expenses=0,
                         total_savings=0,
                         total_investments=0,
                         remaining_budget=0,
                         budget_percentage=0,
                         recent_expenses=[],
                         recent_savings=[],
                         recent_investments=[])