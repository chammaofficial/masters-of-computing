# Django Events App

A Django-based web application for creating, categorizing, and listing events with an admin approval workflow. The project features Bootstrap-styled forms, validation, and alerts.

---

## 🛠 Features

- List upcoming events  
- Categorize events  
- Create new events via form submission  
- Admin approval workflow for events  
- Custom validation for datetime fields
- Success and error messages displayed with dismissible Bootstrap alerts  
- Bootstrap 4 styling for forms, buttons, and alerts  

---

## ⚙️ Project Setup

### 1. Create a Virtual Environment
- python3 -m venv venv
- source venv/bin/activate      # Linux / macOS
- venv\Scripts\activate         # Windows

### 2. Install Dependencies
- pip install -r requirements.txt

### 3. Apply Migrations
- python3 manage.py makemigrations
- python3 manage.py migrate

### 4. Create Superuser
- python3 manage.py createsuperuser

### 5. Run Development Server
- python3 manage.py runserver

