from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# --- DATABASE SETUP ---
def create_table():
    # Connects to the database and creates it if it doesn't exist
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT,
                        email TEXT,
                        age INTEGER,
                        password TEXT
                    )''')
    conn.commit()
    conn.close()

# --- HOME ROUTE (CREATE & READ) ---
@app.route('/', methods=['GET', 'POST'])
def home():
    # 1. If the user submits the form to CREATE data
    if request.method == 'POST':
        user = request.form['username']
        email = request.form['email']
        age = request.form['age']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, age, password) VALUES (?, ?, ?, ?)", 
                       (user, email, age, password))
        conn.commit()
        conn.close()
        
        return redirect('/')

    # 2. If the user is just loading the page, READ the data
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()
    conn.close()

    return render_template('index.html', users=all_users)

# --- DELETE ROUTE ---
@app.route('/delete/<int:id>')
def delete_user(id):
    # Connects to the database and deletes the specific user by ID
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    
    return redirect('/')

# --- RUN THE APP ---
if __name__ == '__main__':
    create_table()
    app.run(debug=True)