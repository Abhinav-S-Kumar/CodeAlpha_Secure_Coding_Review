# secure_app.py
# Secure version of the above code

import sqlite3
from flask import Flask, request, escape

app = Flask(__name__)

# Secure database connection and query
@app.route("/login", methods=["GET"])
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    if not username or not password:
        return "❌ Missing username or password"

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ✅ Fix: Use parameterized queries (prevents SQL Injection)
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))

    user = cursor.fetchone()
    conn.close()

    if user:
        return f"✅ Welcome {escape(username)}!"  # ✅ Escape output to prevent XSS
    else:
        return "❌ Invalid credentials"

if __name__ == "__main__":
    # ✅ Do not enable debug in production
    app.run(host="0.0.0.0", port=5000)
