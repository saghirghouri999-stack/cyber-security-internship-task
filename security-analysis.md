# Security Analysis

## Vulnerabilities Tested

### 1. Cross Site Scripting (XSS)
Tested using:
<script>alert('XSS')</script>

Result:
Application was vulnerable / partially vulnerable.

---

### 2. SQL Injection
Tested using:
admin' OR '1'='1

Result:
Login bypass possible / not possible.

---

### 3. Password Security
Observation:
Passwords stored in plain text / secured.

---

## Improvements Suggested
- Input validation required
- Password hashing recommended
- Secure authentication needed
