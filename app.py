from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'

@app.route('/')
def index():
    return "Expense Tracker - Coming Soon!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)