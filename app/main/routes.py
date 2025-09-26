from flask import render_template, redirect, url_for, flash, request, make_response
from datetime import datetime, timezone, timedelta
from sqlalchemy import func, extract
from app import db
from app.models import Salary, Expense, Saving, Investment
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

@bp.route('/salary', methods=['GET', 'POST'])
def salary():
    if request.method == 'POST':
        amount = float(request.form.get('amount', 0))
        
        if amount < 0:
            flash('Salary amount cannot be negative.', 'error')
            return redirect(url_for('main.salary'))
        
        salary = Salary.query.first()
        if salary:
            salary.amount = amount
            ist_timezone = timezone(timedelta(hours=5, minutes=30))
            salary.updated_at = datetime.now(ist_timezone)
        else:
            ist_timezone = timezone(timedelta(hours=5, minutes=30))
            salary = Salary(amount=amount, updated_at=datetime.now(ist_timezone))
            db.session.add(salary)
        
        db.session.commit()
        flash('Salary updated successfully!', 'success')
        return redirect(url_for('main.salary'))
    
    salary = Salary.query.first()
    current_salary = salary.amount if salary else 0
    
    response = make_response(render_template('main/salary.html', salary=salary))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@bp.route('/expenses')
def expenses():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    
    total_expenses = sum(expense.amount for expense in expenses)
    
    return render_template('main/expenses.html', 
                         expenses=expenses, 
                         total_expenses=total_expenses)

@bp.route('/add_expense', methods=['POST'])
def add_expense():
    amount = float(request.form.get('amount', 0))
    category = request.form.get('category', '').strip()
    date_str = request.form.get('date', '')
    notes = request.form.get('notes', '').strip()
    
    if amount <= 0:
        flash('Amount must be greater than 0.', 'error')
        return redirect(url_for('main.expenses'))
    
    if not category:
        flash('Category is required.', 'error')
        return redirect(url_for('main.expenses'))
    
    if not date_str:
        flash('Date is required.', 'error')
        return redirect(url_for('main.expenses'))
    
    try:
        expense_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        flash('Invalid date format.', 'error')
        return redirect(url_for('main.expenses'))
    
    salary = Salary.query.first()
    if not salary or salary.amount <= 0:
        flash('Please set your monthly salary first before adding expenses.', 'error')
        return redirect(url_for('main.expenses'))
    
    current_month = datetime.now().month
    current_year = datetime.now().year
    
    total_expenses = db.session.query(func.sum(Expense.amount)).filter(
        extract('month', Expense.date) == current_month,
        extract('year', Expense.date) == current_year
    ).scalar() or 0
    
    total_savings = db.session.query(func.sum(Saving.amount)).filter(
        extract('month', Saving.date) == current_month,
        extract('year', Saving.date) == current_year
    ).scalar() or 0
    
    total_investments = db.session.query(func.sum(Investment.amount)).filter(
        extract('month', Investment.date) == current_month,
        extract('year', Investment.date) == current_year
    ).scalar() or 0
    
    total_spent = total_expenses + total_savings + total_investments
    remaining_budget = salary.amount - total_spent
    
    if amount > remaining_budget:
        flash(f'Insufficient budget! You can only spend ₹{remaining_budget:.2f} more this month.', 'error')
        return redirect(url_for('main.expenses'))
    
    expense = Expense(
        amount=amount,
        category=category,
        date=expense_date,
        notes=notes
    )
    
    db.session.add(expense)
    db.session.commit()
    
    flash('Expense added successfully!', 'success')
    return redirect(url_for('main.expenses'))

@bp.route('/edit_expense/<int:expense_id>', methods=['POST'])
def edit_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    
    amount = float(request.form.get('amount', 0))
    category = request.form.get('category', '').strip()
    date_str = request.form.get('date', '')
    notes = request.form.get('notes', '').strip()
    
    if amount <= 0:
        flash('Amount must be greater than 0.', 'error')
        return redirect(url_for('main.expenses'))
    
    if not category:
        flash('Category is required.', 'error')
        return redirect(url_for('main.expenses'))
    
    if not date_str:
        flash('Date is required.', 'error')
        return redirect(url_for('main.expenses'))
    
    try:
        expense_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        flash('Invalid date format.', 'error')
        return redirect(url_for('main.expenses'))
    
    expense.amount = amount
    expense.category = category
    expense.date = expense_date
    expense.notes = notes
    
    db.session.commit()
    
    flash('Expense updated successfully!', 'success')
    return redirect(url_for('main.expenses'))

@bp.route('/delete_expense/<int:expense_id>')
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    
    db.session.delete(expense)
    db.session.commit()
    
    flash('Expense deleted successfully!', 'success')
    return redirect(url_for('main.expenses'))

@bp.route('/savings')
def savings():
    savings = Saving.query.order_by(Saving.date.desc()).all()
    
    total_savings = sum(saving.amount for saving in savings)
    
    return render_template('main/savings.html', savings=savings, total_savings=total_savings)

@bp.route('/add_saving', methods=['POST'])
def add_saving():
    amount = float(request.form.get('amount', 0))
    date_str = request.form.get('date', '')
    notes = request.form.get('notes', '').strip()
    
    if amount <= 0:
        flash('Amount must be greater than 0.', 'error')
        return redirect(url_for('main.savings'))
    
    if not date_str:
        flash('Date is required.', 'error')
        return redirect(url_for('main.savings'))
    
    try:
        saving_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        flash('Invalid date format.', 'error')
        return redirect(url_for('main.savings'))
    
    saving = Saving(
        amount=amount,
        date=saving_date,
        notes=notes
    )
    
    db.session.add(saving)
    db.session.commit()
    
    flash('Saving added successfully!', 'success')
    return redirect(url_for('main.savings'))

@bp.route('/edit_saving/<int:saving_id>', methods=['POST'])
def edit_saving(saving_id):
    saving = Saving.query.get_or_404(saving_id)
    
    amount = float(request.form.get('amount', 0))
    date_str = request.form.get('date', '')
    notes = request.form.get('notes', '').strip()
    
    if amount <= 0:
        flash('Amount must be greater than 0.', 'error')
        return redirect(url_for('main.savings'))
    
    if not date_str:
        flash('Date is required.', 'error')
        return redirect(url_for('main.savings'))
    
    try:
        saving_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        flash('Invalid date format.', 'error')
        return redirect(url_for('main.savings'))
    
    saving.amount = amount
    saving.date = saving_date
    saving.notes = notes
    
    db.session.commit()
    
    flash('Saving updated successfully!', 'success')
    return redirect(url_for('main.savings'))

@bp.route('/delete_saving/<int:saving_id>')
def delete_saving(saving_id):
    saving = Saving.query.get_or_404(saving_id)
    
    db.session.delete(saving)
    db.session.commit()
    
    flash('Saving deleted successfully!', 'success')
    return redirect(url_for('main.savings'))

@bp.route('/investments')
def investments():
    investments = Investment.query.order_by(Investment.date.desc()).all()
    
    total_investments = sum(investment.amount for investment in investments)
    
    return render_template('main/investments.html', investments=investments, total_investments=total_investments)

@bp.route('/add_investment', methods=['POST'])
def add_investment():
    amount = float(request.form.get('amount', 0))
    investment_type = request.form.get('investment_type', '').strip()
    date_str = request.form.get('date', '')
    notes = request.form.get('notes', '').strip()
    
    if amount <= 0:
        flash('Amount must be greater than 0.', 'error')
        return redirect(url_for('main.investments'))
    
    if not investment_type:
        flash('Investment type is required.', 'error')
        return redirect(url_for('main.investments'))
    
    if not date_str:
        flash('Date is required.', 'error')
        return redirect(url_for('main.investments'))
    
    try:
        investment_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        flash('Invalid date format.', 'error')
        return redirect(url_for('main.investments'))
    
    investment = Investment(
        amount=amount,
        investment_type=investment_type,
        date=investment_date,
        notes=notes
    )
    
    db.session.add(investment)
    db.session.commit()
    
    flash('Investment added successfully!', 'success')
    return redirect(url_for('main.investments'))

@bp.route('/edit_investment/<int:investment_id>', methods=['POST'])
def edit_investment(investment_id):
    investment = Investment.query.get_or_404(investment_id)
    
    amount = float(request.form.get('amount', 0))
    investment_type = request.form.get('investment_type', '').strip()
    date_str = request.form.get('date', '')
    notes = request.form.get('notes', '').strip()
    
    if amount <= 0:
        flash('Amount must be greater than 0.', 'error')
        return redirect(url_for('main.investments'))
    
    if not investment_type:
        flash('Investment type is required.', 'error')
        return redirect(url_for('main.investments'))
    
    if not date_str:
        flash('Date is required.', 'error')
        return redirect(url_for('main.investments'))
    
    try:
        investment_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        flash('Invalid date format.', 'error')
        return redirect(url_for('main.investments'))
    
    investment.amount = amount
    investment.investment_type = investment_type
    investment.date = investment_date
    investment.notes = notes
    
    db.session.commit()
    
    flash('Investment updated successfully!', 'success')
    return redirect(url_for('main.investments'))

@bp.route('/delete_investment/<int:investment_id>')
def delete_investment(investment_id):
    investment = Investment.query.get_or_404(investment_id)
    
    db.session.delete(investment)
    db.session.commit()
    
    flash('Investment deleted successfully!', 'success')
    return redirect(url_for('main.investments'))