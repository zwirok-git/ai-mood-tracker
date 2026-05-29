# 🧠 AI Mood Tracker

AI-powered journal application for tracking emotions, reflecting on daily experiences, and generating AI insights from journal entries.

This project allows users to create journal entries, monitor emotional state over time, and receive AI-generated reflections and emotion suggestions.

---

## 🌐 Live Demo 

https://ai-mood-tracker.site 

### Test Credentials

Email: test@test.com
Password: zNin4qPZiCayxC4

---

## ✨ Features

### Authentication & Users
- User registration
- Email verification
- Login / logout
- User profile
- Profile editing
- Account deletion

### Journal System
- Create journal entries
- Edit journal entries
- Delete journal entries
- Detailed journal view

### AI Features
- AI Insight generation
- Insight regeneration
- Emotion detection
- Emotion suggestions
- Multiple LLM support

---

## 🗄 Database Structure

![Database Structure](https://github.com/user-attachments/assets/9b0e95f7-68e5-408c-819b-fffc69d4e945)

---

# 📷 Application Screens

## Landing Page

![Landing 1](https://github.com/user-attachments/assets/fcf807f8-ea2f-49b8-b61b-36e6ee9869cb)

![Landing 2](https://github.com/user-attachments/assets/627ad780-e223-4af7-926b-937075c9d9e7)

---

## Authentication

### Login

![Login](https://github.com/user-attachments/assets/1d95fdb5-8b63-4ba6-ab54-9277be6f23e2)

### Registration

![Registration](https://github.com/user-attachments/assets/7044edf6-1dcd-4acf-aa2c-1290c07056b2)

### Email Confirmation

![Email](https://github.com/user-attachments/assets/7c840c43-2400-4755-a4ef-fbcc199e0459)

---

## Profile

![Profile](https://github.com/user-attachments/assets/bd78604a-5560-4efd-940e-0c937b7fecfa)

---

## Journal

![Journal](https://github.com/user-attachments/assets/ea449b12-b48a-434c-bfc6-9a5ea0137a74)

---

## Create Entry

![Create](https://github.com/user-attachments/assets/f87d7b76-e363-49c8-91af-356d38a68839)

---

## AI Reflection

![Insight](https://github.com/user-attachments/assets/8e68386e-8f6b-4c80-bca0-085fd454c993)

---

# 🚀 Getting Started

Clone repository:

```bash
git clone https://github.com/zwirok-git/ai-mood-tracker.git
cd ai-mood-tracker
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ⚙ Environment Variables

Create `.env`

```env
DJANGO_SECRET_KEY=

EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
DEFAULT_FROM_EMAIL=

LLM_API_KEY=
```

---

# 🗃 Database Setup

Apply migrations:

```bash
python manage.py migrate
```

Create superuser:

```bash
python manage.py createsuperuser
```

Run server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

# 🧪 Running Tests

Run all tests:

```bash
python manage.py test
```

---

# 🤝 Contributing

If you would like to contribute:

1. Fork repository
2. Create feature branch
3. Commit changes
4. Open Pull Request







