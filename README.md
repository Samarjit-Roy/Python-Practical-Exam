# Simple User Registration System 

A lightweight, full-stack web application built with Python and Flask. This project was developed to demonstrate fundamental web architecture, routing, and backend database connectivity.

## 🚀 Features

This application performs core CRUD (Create, Read, Update, Delete) database operations:
* **Create:** Register new users via secure `POST` requests.
* **Read:** Fetch and display all registered users dynamically from the database.
* **Delete:** Remove specific users from the database using dynamic URL routing.
* **Modern UI:** A clean, centered, and responsive user interface styled with custom CSS.

## 🛠️ Technologies Used

* **Backend:** Python, Flask (Microframework)
* **Database:** SQLite (via Python's built-in `sqlite3` library)
* **Frontend:** HTML5, CSS3, Jinja2 Templating

## 📁 Project Structure

```text
├── app.py                  # Main Python server, routing, and database logic
├── templates/
│   └── index.html          # Frontend UI and Jinja data loops
└── database.db             # SQLite database file (auto-generates on first run)
