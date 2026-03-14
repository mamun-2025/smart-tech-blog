
# Django Blog Application

A modern Blog Web Application built with Django.
Users can create blog posts, comment on posts, like posts, and manage their content.

This project is built step-by-step to learn Django Backend Development and REST API development.

---

# 🚀 Project Goal

The goal of this project is to learn and implement:

- Django Backend Development
- Blog CRUD Operations
- Authentication System
- Responsive UI
- Comment System
- Like/Reaction System
- Search + Pagination
- PostgreSQL Database Integration
- Django REST Framework APIs
- JWT Authentication
- Advanced API Features (Pagination, Search, Filter)
- Deployment


--- 

# 📌 Tech Stack 

### Backend
- Python 
- Django
- Djanog REST Framework
- JWT Authentication (SimpleJWT)

### Database
- SQLite (Development)
- PostgreSQL (Production)

### Frontend
- HTML
- TailwindCSS
- JavaScript

### Tools
- Git 
- GitHub
- Vs Code
- Postman

### Deployment
- Render

---

# 📂 Project Structure
``` text
blog-project/
│
├── core/                       # Django project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── blog/                       # Blog application
│   ├── migrations/
│   │
│   ├── templates/
│   │   └── blog/
│   │       ├── post_list.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       └── post_confirm_delete.html
│   │
│   ├── api_urls.py
│   ├── api_views.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── serializers.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
│
├── templates/                # Global templates
│   ├── base.html
│   │
│   └── registration/
│        ├── login.html
│        └── signup.html
│
├── static/
│   ├── css/
│   │   └── output.css          # Tailwind compiled CSS
│       └── input.css           # Tailwind source files        
│
├── tailwind.config.js
├── package.json
│
├── .env
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

--- 

# ⚙️ Environment Setup

- Clone Repository:
   git clone https://github.com/mamun-2025/smart-tech-blog
   cd blog_app

- Create Virtual Environment:
   python -m venv venv

- Activate Virtual Environment:
   Windows: venv\Scripts\activate

- Install Dependencies:
   pip install -r requirements.txt

- Run Migrations:
   python manage.py makemigrations
   python manage.py migrate

- Run Server:
   python manage.py runserver

---

# 🎰 Development Progress
# ✅ Step 1:  project Setup
Completed:

- Python Installed 
- Django Installed
- Django Project Created 
- Django App Created
- Development Server Running

Commands

``` bash
pip install django
django-admin startproject core
cd core 
python manage.py startapp blog 
python manage.py migrate 
python manage.py runserver

Status: ✅ Completed

# ⏳ Step 2: Blog Model Design & Admin Panel
Implemented Features:

- Post Model
- Category Model
- Tag Model
- Comment Model
- Like/Reaction Model
- Post Status(Draft/Published)
- Created & Updated Timestamp
- Superuser Creation
- Admin_Panel Setup 

Status: ✅ Completed

# ⏳ Step 3: Blog CRUD System 
Implemented Features:

- Create Post
- View Post
- Update Post
- Delete Post

Status: ✅ Completed

# ⏳ Step 4: Authentication System
Implemented Features:

- User Signup
- User Login
- User Logout

Status: ✅ Completed

# ⏳ Step 5: Responsive UI Improvement
Implemented Features:

- Tailwing CSS Integration
- Responsive Blog Layout

Status: ✅ Completed

# ⏳ Step 6: Comment System
Implemented Features:

- Add Comment
- Delete Comment
- Comment List
- User-based permission

Status: ✅ Completed

# ⏳ Step 7: Like/Reaction System
Implemented Features:

- Like Post 
- Unlike Post
- Like count

Status: ✅ Completed

# Step 8: Search + Pagination
Implemented Features:

- Blog search byt title/content
- Pagination in post list
- Filter posts by category/tag

Status: ✅ Completed

# ⏳ Step 8: Database Upgrade
Planned Features:

- PostgrSQL Integration
- Environment Variables (.env)

Status: ✅ Completed

# ⏳ Step 9: DRF API + JWT Authentication
Planned Features:

- Blog Post API
- Comment API
- Like API
- Search API
- Filter API
- JWT secure token authentication

Status: ✅ Completed
```

# ⏳ Step 10: Deployment (Render)
Planned Platform:

- GitHub repo push
- Environment variables config
- Neon PostgreSQL DB
- Render Hosting

Status: ⏳ In Progress

---

# 👨‍💻 Author
- Mamun Bepari
- Aspiring Backend Developer (Python & Django)

GitHub:
https://github.com/mamun-2025

