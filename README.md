# Secure Backend API

A secure backend REST API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Pydantic**, **JWT authentication**, and **password hashing**.

The project demonstrates user registration, secure password storage, login authentication, JWT-based authorization, protected routes, and role-based access control.

## Features

* User registration
* Secure password hashing using Argon2
* User login
* JWT access-token authentication
* Protected user profile endpoint
* Role-based authorization
* Admin-only endpoint
* PostgreSQL database integration
* SQLAlchemy ORM
* Pydantic request and response validation
* Automatic Swagger API documentation
* Environment-variable configuration
* `.env` protection using `.gitignore`

## Technologies Used

* Python
* FastAPI
* Uvicorn
* PostgreSQL
* SQLAlchemy
* Psycopg
* Pydantic
* Pydantic Email Validator
* PyJWT
* pwdlib
* Argon2
* python-dotenv

## Project Structure

```text
secure-backend/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   │
│   ├── dependencies/
│   │   ├── __init__.py
│   │   └── auth.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── users.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── security.py
│
├── venv/
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Database

The project uses PostgreSQL.

Database name:

```text
secure_backend
```

Main table:

```text
users
```

The `users` table contains:

* `id`
* `username`
* `email`
* `password`
* `role`
* `is_active`

Passwords are not stored as plain text. They are stored as secure password hashes.

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/secure_backend

SECRET_KEY=your-long-secret-key-at-least-32-characters-long
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Do not commit the real `.env` file to GitHub.

Use `.env.example` as a template instead.

## Installation

Clone the project and open the project directory:

```bash
cd secure-backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The application runs at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger to:

1. Register a user
2. Login
3. Receive an access token
4. Authorize the API
5. Access protected endpoints
6. Test admin authorization

## Authentication Flow

The authentication flow is:

```text
User Registration
       ↓
Password Hashing
       ↓
PostgreSQL
       ↓
User Login
       ↓
Password Verification
       ↓
JWT Access Token
       ↓
Authorization Header
       ↓
Protected Endpoint
```

The authorization header uses the Bearer token format:

```text
Authorization: Bearer <access_token>
```

## User Registration

Endpoint:

```text
POST /auth/register
```

Example request:

```json
{
  "username": "testuser",
  "email": "testuser@example.com",
  "password": "Test@123"
}
```

The password is hashed before it is stored in PostgreSQL.

## User Login

Endpoint:

```text
POST /auth/login
```

Example:

```text
username=testuser
password=Test@123
```

A successful login returns an access token.

Example response:

```json
{
  "access_token": "eyJ...",
  "token_type": "bearer"
}
```

## Protected User Endpoint

Endpoint:

```text
GET /users/me
```

This endpoint requires a valid JWT access token.

Example response:

```json
{
  "id": 1,
  "username": "testuser",
  "email": "testuser@example.com",
  "role": "user"
}
```

## Admin Authorization

Endpoint:

```text
GET /users/admin
```

This endpoint requires the authenticated user's role to be:

```text
admin
```

A normal user receives:

```text
403 Forbidden
```

with:

```json
{
  "detail": "Admin access required"
}
```

An administrator can access the endpoint successfully.

## Security

This project demonstrates several security practices:

* Passwords are hashed instead of stored as plain text.
* JWT tokens are used for authentication.
* Protected endpoints require authentication.
* Admin endpoints require the correct user role.
* Database credentials are stored in `.env`.
* `.env` is excluded from Git.
* A strong secret key should be used for JWT signing.

## Testing the Authentication Flow

Recommended testing order:

```text
1. Register a user
       ↓
2. Verify the user in PostgreSQL
       ↓
3. Login
       ↓
4. Copy the access token
       ↓
5. Authorize Swagger
       ↓
6. Test GET /users/me
       ↓
7. Test GET /users/admin
```

For an administrator test:

```text
1. Change the user's role to admin
       ↓
2. Login again
       ↓
3. Get a new JWT
       ↓
4. Authorize Swagger with the new token
       ↓
5. Test GET /users/admin
```

## Requirements

The project's Python dependencies are listed in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

## Important

Never upload these files or folders to GitHub:

```text
.env
venv/
__pycache__/
```

The `.gitignore` file should contain:

```text
venv/
.env
__pycache__/
*.pyc
```

## Project Goal

The purpose of this project is to demonstrate how to build a secure backend API using FastAPI and PostgreSQL with:

* Authentication
* Authorization
* Password hashing
* JWT tokens
* Role-based access control
* Database integration
* API validation
* Protected routes
