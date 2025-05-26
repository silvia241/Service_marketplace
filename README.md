# 🛎️ Django Service Marketplace

A full-featured freelance-style service marketplace built using Django and Bootstrap.

Users can register, log in, post services, and request services from others. Each user has a personalized dashboard to manage their posted and requested services.

---

## 🌐 Features

- 🔐 User Registration, Login & Logout
- 🛠️ Post services with title, description, category
- 📥 Request services from other users
- 🧍 Self-request prevention logic
- 🧭 User Dashboard (Posted Services, Requested Services)
- 🗂️ Service detail page with request option
- 🧼 Clean & modern Bootstrap UI
- 🛡️ Admin panel with custom list display

---

## 🔧 Technologies Used

- Python 3
- Django 4.x
- Bootstrap 5
- SQLite (default for development)
- HTML5, CSS3

---
## 🚀 Setup Instructions (Local Development)

```bash
git clone https://github.com/silvia241/service-marketplace.git
cd service-marketplace

python -m venv venv
venv\Scripts\activate     # On Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```
Then visit: http://127.0.0.1:8000

Folder Structure
service-marketplace/
│
-├── config/           # Project settings
-├── services/         # Main app for services and requests
-├── templates/        # HTML templates (Bootstrap-based)
-├── static/           # Static files (CSS, JS)
-├── db.sqlite3        # Default DB (can be removed)
-└── manage.py         # Django management script

