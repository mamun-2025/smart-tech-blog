
# 🚀 Smart-Tech-Blog

A feature-rich, modern blogging platform specifically designed for tech enthusiasts. Built with Django, it offers a seamless reading experience with professional formatting and real-time interaction.

---

## ✨ Features

- **📖 Professional Content Management:** Integrated Markdown support for clean and professional tech articles.
- **⏱️ Dynamic Reading Time:** Automatically calculates and displays the estimated 'Read Time' for each post.
- **🔍 Advanced Search & Filtering:** Quick search functionality to find posts by keywords or categories.
- **💬 Interactive Comments:** Full-featured comment section allowing users to engage and share thoughts.
- **📱 One-Click Social Share:** Integrated buttons to share blogs directly to Facebook, Twitter (X), and LinkedIn.
- **🔒 Secure Authentication:** Robust User sign-up, login, and profile management system.
- **📂 Category Management:** Subject-based post organization for easy navigation.
- **📄 Pagination:** User-friendly navigation through page-based content display.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django 6.0
- **Database:** PostgreSQL (Transitioning from SQLite for scalability)
- **Frontend:** HTML5, CSS3, Bootstrap 5.3
- **Libraries:**
  - `django-markdownify` (Markdown Rendering)
  - `Pillow` (Media Handling)
  - `FontAwesome` (UI Icons)

---

## 📂 Project Structure

SMART_TECH_BLOG/
├── accounts/          # Authentication & User Profiles
├── blog/              # Core Logic (Posts, Comments, Tags)
├── MainSettings/      # Django Configuration (settings.py, urls.py)
├── media/             # User Uploads (Thumbnails, Profile Pics)
├── templates/         # HTML Templates
├── manage.py          # Django CLI
└── requirements.txt   # Project Dependencies


## ⚙️ Installation & Setup
1. Clone the repository:
Bash
git clone [https://github.com/mamun-2025/smart-tech-blog]
cd smart-tech-blog

2. Create and activate a virtual environment:
python -m venv venv
# Windows:
venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Apply migrations:
python manage.py makemigrations
python manage.py migrate

5. Run the server:
python manage.py runserver