# insecure_app.py
# Example of insecure Python code for demonstration

import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Insecure database connection and query
@app.route("/login", methods=["GET"])
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ Vulnerability: SQL Injection
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    user = cursor.fetchone()
    conn.close()

    if user:
        return f"✅ Welcome {username}!"
    else:
        return "❌ Invalid credentials"

if __name__ == "__main__":
    app.run(debug=True)  # ❌ Debug mode enabled (security risk)
