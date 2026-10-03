# TaskFlow

A modern Task Management REST API built with **Django** and **Django REST Framework (DRF)**, featuring secure **JWT authentication** (with token blacklisting) and user-specific task management.

---

## 🚀 Features

- **User Authentication**: Secure user registration, login, and logout powered by `rest_framework_simplejwt`.
- **JWT Authentication & Token Blacklisting**: Access and refresh token generation with blacklist support on logout.
- **Task Management**: Structured task tracking (title, description, completion status, timestamps) associated with registered users.
- **RESTful Architecture**: Clean, modular API design adhering to REST conventions.

---

## 🛠️ Tech Stack

- **Backend Framework**: [Django](https://www.djangoproject.com/)
- **API Framework**: [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
- **Authentication**: [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
- **Database**: SQLite (default development database)

---

## 📁 Project Structure

```text
task-management/
├── tasks/               # Main project configuration (settings, URLs, WSGI)
├── users/               # Authentication & user management app
│   ├── serializers.py   # Register & Login serializers
│   ├── views.py         # RegisterView, LoginView, LogoutView
│   └── urls.py          # Auth route definitions
├── tasksmeng/           # Task management app
│   ├── models.py        # Task model definition
│   └── views.py         # Task views & logic
├── manage.py            # Django CLI management script
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

---

## ⚡ Getting Started

### Prerequisites

- Python 3.10+ installed on your system
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/FarazSafder/TaskFlow.git
cd TaskFlow
```

### 2. Set Up a Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

*(Optional) Freeze installed packages:*
```bash
pip freeze > requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## 📡 API Endpoints

### 🔐 Authentication

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/api/auth/register/` | Register a new user account | No |
| `POST` | `/api/auth/login/` | Log in and receive JWT access & refresh tokens | No |
| `POST` | `/api/auth/logout/` | Blacklist the refresh token and log out | Yes (`Bearer <token>`) |

#### Sample Requests

##### **1. Register User**
`POST /api/auth/register/`
```json
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "secretpassword123"
}
```

##### **2. Login**
`POST /api/auth/login/`
```json
{
  "username": "johndoe",
  "password": "secretpassword123"
}
```
**Response:**
```json
{
  "message": "Login successful",
  "Token": "<access_token>",
  "refresh": "<refresh_token>"
}
```

##### **3. Logout**
`POST /api/auth/logout/`  
**Headers:** `Authorization: Bearer <access_token>`
```json
{
  "refresh": "<refresh_token>"
}
```

---

## 📝 License

This project is licensed under the MIT License - feel free to use and customize it for your needs.
