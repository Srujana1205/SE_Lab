from flask import Flask, render_template, request, redirect, url_for
from database import db_session, init_db
from models import User, Transaction

app = Flask(__name__)

# Initialize the database
init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        # Validate user credentials
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup form submission
        # Create new user account
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/transaction', methods=['GET', 'POST'])
def transaction():
    if request.method == 'POST':
        # Handle transaction form submission
        # Process the transaction
        return redirect(url_for('transaction_history'))
    return render_template('transaction.html')

@app.route('/transaction_history')
def transaction_history():
    # Retrieve transaction history for the current user
    return render_template('transaction_history.html')

if __name__ == '__main__':
    app.run(debug=True)
