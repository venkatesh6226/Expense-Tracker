# 💰 Expense Tracker

A comprehensive full-stack web application for managing personal finances, built with Flask, Bootstrap, and SQLite. Track your monthly salary, expenses, savings, and investments with beautiful visualizations and intuitive user interface.

![Expense Tracker](https://img.shields.io/badge/Flask-2.3.3-green) ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple) ![SQLite](https://img.shields.io/badge/SQLite-3-blue) ![Python](https://img.shields.io/badge/Python-3.8+-yellow)

## ✨ Features

### 🔐 Authentication & Security

- **User Registration & Login** with secure password hashing
- **Session Management** with Flask-Login
- **Password Security** using bcrypt encryption
- **User-specific Data** isolation

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

### 📈 Visualization & Reports

- **Pie Chart** for expense categories (current month)
- **Bar Chart** for monthly comparison (last 6 months)
- **Financial Summary** with key metrics
- **Category Breakdown Table** with percentages
- **Savings Rate Calculation**

### 🎨 User Interface

- **Responsive Design** with Bootstrap 5
- **Modern UI/UX** with clean, intuitive interface
- **Interactive Elements** with jQuery
- **Form Validation** (client-side and server-side)
- **Toast Notifications** for user feedback
- **Loading States** and smooth animations

### 🔍 Search & Filtering

- **Date Range Filtering** (future enhancement)
- **Category/Type Filtering**
- **Keyword Search** in notes
- **Pagination** for large datasets

## 🛠️ Tech Stack

### Frontend

- **HTML5** with semantic structure
- **Bootstrap 5** for responsive UI components
- **Custom CSS** for styling and animations
- **JavaScript & jQuery** for interactivity
- **Chart.js** for data visualization
- **Font Awesome** for icons

### Backend

- **Python 3.8+** as the programming language
- **Flask 2.3.3** as the web framework
- **Flask-SQLAlchemy** for database ORM
- **Flask-Login** for authentication
- **Werkzeug** for password hashing
- **Passlib** with bcrypt for secure password storage

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
│   ├── auth/
│   │   ├── login.html       # Login page
│   │   └── signup.html      # Registration page
│   └── main/
│       ├── dashboard.html   # Dashboard
│       ├── salary.html      # Salary management
│       ├── expenses.html    # Expense tracking
│       ├── savings.html     # Savings management
│       ├── investments.html # Investment tracking
│       └── reports.html     # Reports and analytics
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
3. Create a new account or use the default admin credentials:
   - **Email**: admin@example.com
   - **Password**: admin123

## 📱 Usage Guide

### Getting Started

1. **Sign Up**: Create a new account with your email and password
2. **Set Salary**: Navigate to Salary page and enter your monthly take-home salary
3. **Add Transactions**: Start adding expenses, savings, and investments
4. **Monitor Budget**: Check the dashboard for real-time budget updates
5. **View Reports**: Analyze your spending patterns with charts and reports

### Dashboard Features

- **Budget Overview**: See your salary, expenses, savings, and investments
- **Progress Bar**: Visual representation of remaining budget
- **Recent Transactions**: Latest 5 transactions across all categories
- **Quick Actions**: Fast access to add new transactions
- **Category Chart**: Pie chart showing expense distribution

### Managing Transactions

- **Add**: Use the forms to add new expenses, savings, or investments
- **Edit**: Click the edit button to modify existing transactions
- **Delete**: Remove transactions with confirmation
- **Filter**: Use category/type filters and search functionality
- **Pagination**: Navigate through large datasets

### Reports & Analytics

- **Category Breakdown**: See how much you spend in each category
- **Monthly Comparison**: Compare expenses, savings, and investments over time
- **Financial Summary**: Key metrics including savings rate
- **Visual Charts**: Interactive pie and bar charts

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

## 🧪 Testing

### Manual Testing

1. **Authentication**: Test signup, login, and logout functionality
2. **CRUD Operations**: Test adding, editing, and deleting transactions
3. **Validation**: Test form validation and error handling
4. **Responsive Design**: Test on different screen sizes
5. **Charts**: Verify chart rendering and data accuracy

### Test Data

The application creates a default admin user for testing:

- Email: admin@example.com
- Password: admin123

## 🚀 Deployment

### Local Development

```bash
python app.py
```

### Production Deployment

1. Set `FLASK_ENV=production`
2. Use a production WSGI server like Gunicorn
3. Configure a reverse proxy with Nginx
4. Set up SSL certificates
5. Use a production database (PostgreSQL/MySQL)

### Docker Deployment (Future Enhancement)

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 Future Enhancements

### Planned Features

- [ ] **Date Range Filtering** for expenses and reports
- [ ] **Export Functionality** (PDF, Excel, CSV)
- [ ] **Budget Goals** and alerts
- [ ] **Recurring Transactions** (monthly bills, subscriptions)
- [ ] **Multi-currency Support**
- [ ] **Dark Theme** toggle
- [ ] **Mobile App** (React Native/Flutter)
- [ ] **API Endpoints** for third-party integrations
- [ ] **Advanced Analytics** and insights
- [ ] **Bill Reminders** and notifications
- [ ] **Investment Tracking** with current values
- [ ] **Family/Shared Accounts** support
- [ ] **Backup and Restore** functionality

### Technical Improvements

- [ ] **Unit Tests** with pytest
- [ ] **API Documentation** with Swagger
- [ ] **Docker Containerization**
- [ ] **CI/CD Pipeline** with GitHub Actions
- [ ] **Performance Optimization**
- [ ] **Security Enhancements**
- [ ] **Database Migrations** with Flask-Migrate

## 🐛 Known Issues

- Date picker may not work in older browsers
- Charts may not render properly in very small screens
- Large datasets may cause performance issues (pagination implemented)

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/expense-tracker/issues) page
2. Create a new issue with detailed description
3. Include error messages and steps to reproduce

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Bootstrap** for the responsive UI framework
- **Chart.js** for beautiful data visualizations
- **Font Awesome** for the icon library
- **Flask** community for the excellent web framework
- **SQLAlchemy** for the powerful ORM

## 📊 Project Statistics

- **Lines of Code**: ~2,000+
- **Files**: 20+
- **Features**: 15+
- **Technologies**: 10+
- **Development Time**: 2-3 days

---

**Built with ❤️ using Flask, Bootstrap, and modern web technologies**

_Start tracking your expenses today and take control of your financial future!_
