# Restful-Blog-API

---

# 🌟 RESTful Blog API 🚀

A **RESTful API** for a blog application that allows users to create, read, update, and delete posts, manage comments, likes, follows, and receive notifications.

---

## 🎯 Features

* **🔐 User Authentication**: Register & login with JWT tokens
* **📝 Blog Posts**: Create, Read, Update, Delete (CRUD) posts
* **💬 Comments**: Add, update, delete, and view comments on posts
* **❤️ Likes**: Like or unlike posts and comments
* **👥 Follow System**: Follow/unfollow other users
* **🔔 Notifications**: Receive alerts for activity (likes, comments, follows)
* **📚 API Documentation**: Swagger integration for easy testing
* **🧪 Testing**: Unit & integration tests using Pytest

---

## 🛠 Tech Stack

| Layer    | Technology                        |
| -------- | ----------------------------------|
| Backend  | Flask (Python)                    |
| Database | SQLite / PostgreSQL / MySQL(used) |
| Auth     | JWT (JSON Web Tokens)             |
| API Docs | Swagger (Flasgger)                |
| Testing  | Pytest                            |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Pallavi-23K/Restful-BLog-API.git
cd Restful-BLog-API
```

### 2️⃣ Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file and set your JWT secret and database URI:

```
SECRET_KEY=your_jwt_secret
DATABASE_URI=sqlite:///blog.db   # or PostgreSQL/MySQL URI
```

### 5️⃣ Initialize Database

```bash
flask db init
flask db migrate
flask db upgrade
```

### 6️⃣ Run the API

```bash
flask run
```

Your API will be available at `http://127.0.0.1:5000/`

### 7️⃣ Access Swagger Documentation

Visit `http://127.0.0.1:5000/apidocs` to explore endpoints interactively.

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📂 Project Structure

```
blog_api/
├─ models.py         # Database models (User, Post, Comment, etc.)
├─ routes.py         # API endpoints
├─ config.py         # Configuration & environment settings
├─ main.py            # Flask app initialization
└─ tests/            # Unit & integration tests
--requirements.txt  # Dependencies
```

---

## 💡 Notes

* Use JWT tokens in headers for authenticated requests.
* Swagger docs provide example requests/responses.
* Make sure your database is correctly configured before running the API.

---

## 📌 GitHub Repository

[Restful Blog API Repository](https://github.com/Pallavi-23K/Restful-BLog-API)

---


