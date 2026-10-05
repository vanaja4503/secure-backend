# Secure Backend API

A secure REST API built with **FastAPI, PostgreSQL, SQLAlchemy, JWT authentication, Argon2 password hashing, and role-based access control (RBAC)**.

This project demonstrates how to build a secure backend application with authentication, authorization, protected routes, database integration, validation, and file uploads.

## Features

* User registration
* Secure password hashing using Argon2
* User login
* JWT access-token authentication
* Protected user profile endpoint
* Role-Based Access Control (RBAC)
* Admin-only endpoint
* PostgreSQL database integration
* SQLAlchemy ORM
* Pydantic request and response validation
* Authentication service layer
* Protected file upload endpoint
* File type validation
* Environment-variable configuration
* Automatic Swagger/OpenAPI documentation
* Secure `.env` handling with `.gitignore`

## Technologies

* Python
* FastAPI
* Uvicorn
* PostgreSQL
* SQLAlchemy
* Psycopg
* Pydantic
* PyJWT
* pwdlib
* Argon2
* python-dotenv
* python-multipart
* pytest
* httpx

## Architecture

The application follows a layered backend structure:

```text
Client
  ↓
FastAPI Router
  ↓
Dependencies / Authentication
  ↓
Service Layer
  ↓
SQLAlchemy ORM
  ↓
PostgreSQL
```

The service layer keeps business logic separate from API routing logic, making the application easier to maintain and extend.

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
│   │   ├── users.py
│   │   └── uploads.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── auth_service.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── security.py
│       └── logger.py
│
├── uploads/
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Database

The application uses PostgreSQL.

Database:

```text
secure_backend
```

Main table:

```text
users
```

User fields:

```text
id
username
email
password
role
is_active
```

Passwords are never stored as plain text. They are stored using secure password hashing.

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/secure_backend
SECRET_KEY=your-long-secret-key-at-least-32-characters-long
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Never commit the real `.env` file.

Use `.env.example` as the configuration template.

## Installation

Clone the repository:

```bash
git clone https://github.com/vanaja4503/secure-backend.git
```

Move into the project:

```bash
cd secure-backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` from `.env.example` and enter your local PostgreSQL credentials.

## Run the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Authentication

| Method | Endpoint         | Description           |
| ------ | ---------------- | --------------------- |
| POST   | `/auth/register` | Register a new user   |
| POST   | `/auth/login`    | Login and receive JWT |

### User

| Method | Endpoint       | Description                      |
| ------ | -------------- | -------------------------------- |
| GET    | `/users/me`    | Get authenticated user's profile |
| GET    | `/users/admin` | Admin-only endpoint              |

### Uploads

| Method | Endpoint   | Description             |
| ------ | ---------- | ----------------------- |
| POST   | `/uploads` | Upload a protected file |

## Authentication Flow

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

The API uses the Bearer token format:

```text
Authorization: Bearer <access_token>
```

## Role-Based Access Control

The application supports:

```text
user
admin
```

Normal users can access:

```text
GET /users/me
```

Administrators can access:

```text
GET /users/admin
```

A normal user attempting to access the admin endpoint receives:

```text
403 Forbidden
```

After changing a user's database role from `user` to `admin`, the user must log in again to receive a new JWT containing the updated role.

## File Uploads

The application provides a protected upload endpoint.

Example:

```text
POST /uploads
```

Uploaded files are stored locally in:

```text
uploads/
```

The upload directory is excluded from Git using `.gitignore`.

File validation should be used to restrict unsupported or unsafe file types.

## Security Practices

This project demonstrates:

* Password hashing with Argon2
* JWT-based authentication
* Protected API endpoints
* Role-based authorization
* PostgreSQL integration
* Environment-variable configuration
* Secret protection using `.gitignore`
* Input validation using Pydantic
* File upload validation
* Separation of routing and business logic
* Authentication dependency injection

Never commit:

```text
.env
venv/
__pycache__/
uploads/
```

## Testing

Recommended authentication test flow:

```text
1. Register a user
        ↓
2. Verify the user in PostgreSQL
        ↓
3. Login
        ↓
4. Copy the JWT access token
        ↓
5. Authorize Swagger
        ↓
6. Test GET /users/me
        ↓
7. Test GET /users/admin
        ↓
8. Change role to admin
        ↓
9. Login again
        ↓
10. Test GET /users/admin
```

Recommended upload test flow:

```text
1. Login
        ↓
2. Authorize Swagger
        ↓
3. POST /uploads
        ↓
4. Select a test file
        ↓
5. Execute
        ↓
6. Verify the file inside uploads/
```

## Example Registration

```json
{
  "username": "testuser",
  "email": "testuser@example.com",
  "password": "Test@123"
}
```

## Example Successful Profile Response

```json
{
  "id": 1,
  "username": "testuser",
  "email": "testuser@example.com",
  "role": "user"
}
```

## Example Admin Response

```json
{
  "message": "Welcome Admin",
  "username": "adminuser",
  "role": "admin"
}
```

## Project Goal

The goal of this project is to demonstrate practical backend development using:

* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT authentication
* Password hashing
* RBAC
* Dependency injection
* Service-layer architecture
* API validation
* Protected routes
* File upload handling
* Environment-based configuration

## Future Improvements

Possible future enhancements include:

* Automated test coverage
* Database migrations with Alembic
* Refresh tokens
* Password reset functionality
* Email verification
* Rate limiting
* Docker deployment
* CI/CD using GitHub Actions
* Production deployment
