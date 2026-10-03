# TaskFlow

A modern Task Management REST API built with **Django** and **Django REST Framework (DRF)**, featuring secure **JWT authentication** (with token blacklisting) and user-specific task management.

---

## 🚀 Features

- **User Authentication**: Secure user registration, login, and logout powered by `rest_framework_simplejwt`.
- **JWT Authentication & Token Blacklisting**: Access and refresh token generation with blacklist support on logout.
- **Task Management CRUD**: Full CRUD operations for user tasks (list, create, retrieve, update, delete) handled via DRF `ModelViewSet` and routers.
- **Automatic User Scoping**: Authenticated users can only view and manage their own tasks.
- **Auto Timestamping**: Tracks creation time and automatically records completion timestamps (`completed_at`).
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
├── tasks/               # Main project configuration (settings, root URLs, WSGI)
├── users/               # Authentication & user management app
│   ├── serializers.py   # Register & Login serializers
│   ├── views.py         # RegisterView, LoginView, LogoutView
│   └── urls.py          # Auth routes (/api/auth/...)
├── tasksmeng/           # Task management app
│   ├── models.py        # Task model definition
│   ├── serializers.py   # TaskSerializers
│   ├── views.py         # TaskView (ModelViewSet)
│   └── urls.py          # DefaultRouter routes (/api/tasks/...)
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

All authenticated requests must include the JWT token in the Authorization header:
```http
Authorization: Bearer <access_token>
```

---

### 🔐 Authentication (`/api/auth/`)

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/api/auth/register/` | Register a new user account | No |
| `POST` | `/api/auth/login/` | Log in and receive JWT access & refresh tokens | No |
| `POST` | `/api/auth/logout/` | Blacklist the refresh token and log out | Yes |

#### Authentication Samples

##### **1. Register User**
`POST /api/auth/register/`
```json
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "secretpassword123"
}
```

**Response (201 Created):**
```json
{
  "message": "User Created",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "johndoe@example.com"
  }
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

**Response (200 OK):**
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

**Response (200 OK):**
```json
{
  "message": "Logout successful"
}
```

---

### 📋 Task Management (`/api/tasks/`)

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `GET` | `/api/tasks/` | List all tasks for current user (ordered newest first) | Yes |
| `POST` | `/api/tasks/` | Create a new task (auto-assigned to current user) | Yes |
| `GET` | `/api/tasks/<id>/` | Retrieve details of a specific task | Yes |
| `PUT` | `/api/tasks/<id>/` | Update all fields of a specific task | Yes |
| `PATCH` | `/api/tasks/<id>/` | Partially update a task (e.g., mark as completed) | Yes |
| `DELETE` | `/api/tasks/<id>/` | Delete a specific task | Yes |

#### Task Management Samples

##### **1. Create Task**
`POST /api/tasks/`  
**Headers:** `Authorization: Bearer <access_token>`
```json
{
  "title": "Complete Django documentation",
  "description": "Write API docs and update README",
  "completed": false
}
```

##### **2. List Tasks**
`GET /api/tasks/`  
**Headers:** `Authorization: Bearer <access_token>`

**Response (200 OK):**
```json
[
  {
    "title": "Complete Django documentation",
    "description": "Write API docs and update README",
    "completed": false
  }
]
```

##### **3. Update / Complete Task**
`PATCH /api/tasks/<id>/`  
**Headers:** `Authorization: Bearer <access_token>`
```json
{
  "completed": true
}
```

> **Note**: When `completed` is marked `true`, the `completed_at` timestamp is automatically set in UTC.

##### **4. Delete Task**
`DELETE /api/tasks/<id>/`  
**Headers:** `Authorization: Bearer <access_token>`

**Response (204 No Content)**

---

## 📝 License

This project is licensed under the MIT License - feel free to use and customize it for your needs.
