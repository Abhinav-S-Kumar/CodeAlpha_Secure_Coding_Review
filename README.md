# 🔐 Secure Coding Review - Python

## 📌 Overview
This project demonstrates **secure coding practices** by comparing insecure vs secure implementations of a simple Python Flask application.

---

## 🚨 Vulnerabilities Found
1. **SQL Injection**
   - Insecure code directly concatenated user input in SQL queries.
   - Risk: Attackers can inject malicious SQL to bypass login.

2. **Debug Mode Enabled**
   - Insecure code used `app.run(debug=True)`.
   - Risk: Leaks sensitive stack traces & system info.

3. **Cross-Site Scripting (XSS)**
   - Insecure code directly returned user input.
   - Risk: Attackers could inject malicious scripts.

---

## ✅ Fixes Implemented
1. **Parameterized Queries**
   - Used `cursor.execute(query, (username, password))`.

2. **Disabled Debug Mode**
   - Used `app.run(host="0.0.0.0", port=5000)` without debug in production.

3. **Escaped User Input**
   - Used Flask’s `escape()` function to sanitize output.

---


## 📂 Files in This Repo
- `insecure_app.py` → Example of insecure code
- `secure_app.py` → Fixed & secure version
- `Secure_Coding_Review.md` → Documentation of vulnerabilities & fixes
- `README.md` → Introduction & usage
