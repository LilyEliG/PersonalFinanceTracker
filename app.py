from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# SQLite database file
DATABASE = 'personal_finance.db'

# Function to get the database connection
def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row  # Return rows as dictionaries
    return db

# Initialize the database (create tables if they don't exist)
def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS Categories (
                category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_name TEXT NOT NULL
            )
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS Transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                transaction_date DATE NOT NULL,
                amount REAL NOT NULL,
                type TEXT NOT NULL,
                category_id INTEGER,
                description TEXT,
                FOREIGN KEY (category_id) REFERENCES Categories(category_id)
            )
        ''')
        # Insert sample categories if they don't exist
        db.execute('INSERT OR IGNORE INTO Categories (category_name) VALUES ("Salary")')
        db.execute('INSERT OR IGNORE INTO Categories (category_name) VALUES ("Bonus")')
        db.execute('INSERT OR IGNORE INTO Categories (category_name) VALUES ("Food")')
        db.execute('INSERT OR IGNORE INTO Categories (category_name) VALUES ("Utilities")')
        db.execute('INSERT OR IGNORE INTO Categories (category_name) VALUES ("Entertainment")')
        db.execute('INSERT OR IGNORE INTO Categories (category_name) VALUES ("Travel")')
        db.commit()

# Homepage - Display transactions
@app.route('/')
def index():
    db = get_db()
    transactions = db.execute('''
        SELECT Transactions.*, Categories.category_name 
        FROM Transactions 
        JOIN Categories ON Transactions.category_id = Categories.category_id
    ''').fetchall()
    return render_template('index.html', transactions=transactions)

# Add a new transaction
@app.route('/add', methods=['POST'])
def add_transaction():
    date = request.form['date']
    amount = float(request.form['amount'])
    type = request.form['type']
    category_id = int(request.form['category_id'])
    description = request.form['description']

    db = get_db()
    db.execute('''
        INSERT INTO Transactions (transaction_date, amount, type, category_id, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (date, amount, type, category_id, description))
    db.commit()
    return redirect('/')

# Run the app
if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)