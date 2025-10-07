# 💰 Expense Tracker

A comprehensive full-stack web application for managing personal finances, built with Flask, Bootstrap, and SQLite. Track your monthly salary, expenses, savings, and investments with beautiful visualizations and intuitive user interface.

## ✨ Features

### 💵 Budget Management

- **Monthly Salary Tracking** with easy updates
- **Real-time Budget Calculation** with progress indicators
- **Color-coded Budget Status** (Green: Safe, Yellow: Medium, Red: Low)
- **Remaining Budget Formula**: `Salary - (Expenses + Savings + Investments)`

### 📊 Expense Tracking

- **Add Expenses** with amount, category, date, and notes
- **Predefined Categories**: Food, Transport, Shopping, Entertainment, Healthcare, Education, Utilities, Other
- **Expense History** with pagination and search
- **Edit/Delete** functionality with confirmation modals
- **Category-wise Filtering** and search in notes

### 🏦 Savings & Investments

- **Savings Tracking** with amount, date, and notes
- **Investment Management** with multiple types:
  - SIP (Mutual Fund)
  - Stocks
  - Fixed Deposit (FD)
  - PPF
  - NPS
  - Gold
  - Cryptocurrency
  - Real Estate
  - Other
- **Type-wise Filtering** for investments
- **Edit/Delete** capabilities

### 🎨 User Interface

- **Responsive Design** with Bootstrap 5
- **Modern UI/UX** with clean, intuitive interface
- **Interactive Elements** with jQuery
- **Form Validation** (client-side and server-side)
- **Toast Notifications** for user feedback
- **Loading States** and smooth animations

### 🔍 Search & Filtering

- **Category/Type Filtering**
- **Keyword Search** in notes
- **Pagination** for large datasets

## 🛠️ Tech Stack

### Frontend

- **HTML5** with semantic structure
- **Bootstrap 5** for responsive UI components
- **Custom CSS** for styling and animations
- **JavaScript & jQuery** for interactivity
- **Font Awesome** for icons

### Backend

- **Python 3.8+** as the programming language
- **Flask 2.3.3** as the web framework
- **Flask-SQLAlchemy** for database ORM

### Database

- **SQLite** for lightweight, file-based storage
- **SQLAlchemy ORM** for database operations
- **Database Models**: User, Salary, Expense, Saving, Investment

## 📁 Project Structure

```
Expense Tracker/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   ├── auth/
│   │   ├── __init__.py
│   │   └── routes.py        # Authentication routes
│   └── main/
│       ├── __init__.py
│       └── routes.py        # Main application routes
├── templates/
│   ├── base.html            # Base template
│   └── main/
│       ├── dashboard.html   # Dashboard
│       ├── salary.html      # Salary management
│       ├── expenses.html    # Expense tracking
│       ├── savings.html     # Savings management
│       └── investments.html # Investment tracking
├── static/
│   ├── css/
│   │   └── style.css        # Custom styles
│   └── js/
│       └── main.js          # JavaScript functionality
├── app.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd "Expense Tracker"
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5001`

### Step 5: Access the Application

1. Open your web browser
2. Navigate to `http://localhost:5001`

## 📱 Usage Guide

### Getting Started

1. **Set Salary**: Navigate to Salary page and enter your monthly take-home salary
2. **Add Transactions**: Start adding expenses, savings, and investments
3. **Monitor Budget**: Check the dashboard for real-time budget updates

### Dashboard Features

- **Budget Overview**: See your salary, expenses, savings, and investments
- **Progress Bar**: Visual representation of remaining budget
- **Recent Transactions**: Latest 5 transactions across all categories
- **Quick Actions**: Fast access to add new transactions

### Managing Transactions

- **Add**: Use the forms to add new expenses, savings, or investments
- **Edit**: Click the edit button to modify existing transactions
- **Delete**: Remove transactions with confirmation
- **Filter**: Use category/type filters and search functionality
- **Pagination**: Navigate through large datasets
  

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root for production settings:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///expense_tracker.db
FLASK_ENV=production
```

### Database Configuration

The application uses SQLite by default. For production, you can switch to PostgreSQL or MySQL by updating the database URI in `app/__init__.py`.


## 🚀 Deployment

### Local Development

```bash
python app.py
```

---

**Built with ❤️ using Flask, Bootstrap, and modern web technologies**

_Start tracking your expenses today and take control of your financial future!_
