# Cyber Security Internship Project

**User Management System Security Analysis**

## Overview

This project is based on a User Management Web Application that was analyzed for common security vulnerabilities. Basic security measures were implemented to improve the overall protection of the system.

---

## Features

* User Signup
* User Login
* User Profile Page
* Input Validation
* Password Hashing
* JWT-based Authentication
* Security Headers using Helmet
* Logging using Winston

---

## Technologies Used

* Node.js
* React
* MySQL

---

## Security Testing Performed

### Cross Site Scripting (XSS)

Tested using script injection in input fields.

### SQL Injection

Tested using common payload:
`admin' OR '1'='1`

### Password Security

Checked how passwords were stored and handled.

---

## Security Improvements Implemented

* User input sanitization
* Email and password validation
* Password hashing using bcrypt
* Token-based authentication using JWT
* Secure HTTP headers using Helmet
* Basic logging using Winston

---

## Tools Used

* Express.js
* Validator
* Bcrypt
* JSON Web Token
* Helmet
* Winston
* OWASP ZAP
* Nmap

---

## Project Structure

* backend
* frontend
* security-analysis.md
* CyberSecurity_Report.pdf

---

## Installation

```bash
npm install
node server.js
```

---

## Run the Application

Open in browser:
http://localhost:3000

---

## Report

The detailed report is included in this repository:
**CyberSecurity_Report.pdf**

---

## Author

Saghir Ahmed
