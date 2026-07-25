# 🍽️ RecipeHub

RecipeHub is a modern recipe management web application built with **Python** and **Django**. It enables users to discover recipes, browse categories, search meals, and generate personalized recipes using **Google Gemini AI**. The application is fully responsive, deployed on **Render**, and uses **PostgreSQL** for production.

---

## 🌐 Live Demo

**Live Website:** https://recipehub-oeqm.onrender.com
📂 **GitHub Repository:** https://github.com/rakshithaagowda/RecipeHub

---

## ✨ Features

* 🍽 Browse all recipes
* ⭐ Featured recipes section
* 📂 Browse recipes by category
* 🔍 Search recipes instantly
* 📖 Detailed recipe pages
* 🤖 AI Recipe Assistant powered by Google Gemini
* 👤 User Registration & Login
* 🔐 Secure Authentication
* 👋 Personalized navigation after login
* ⚙ Django Admin Panel
* 📱 Fully Responsive UI
* 🗄 PostgreSQL Production Database
* 🚀 Deployed on Render
* 🔗 REST API Endpoints using Django REST Framework

---

## 🤖 AI Recipe Assistant

RecipeHub includes an AI-powered recipe generator using **Google Gemini 2.5 Flash**.

Simply enter the ingredients you have available, and the AI generates a complete recipe with ingredients, cooking instructions, and useful cooking tips.

Example:

**Ingredients**

* Rice
* Onion
* Tomato
* Egg

**Output**

* Recipe Name
* Ingredients
* Step-by-step Instructions
* Cooking Tips

---

## 🛠 Tech Stack

### Backend

* Python
* Django
* Django REST Framework

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Database

* PostgreSQL (Production)
* SQLite (Development)

### AI

* Google Gemini 2.5 Flash
* Google GenAI SDK

### Deployment

* Render
* Gunicorn
* WhiteNoise

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
recipehub/
│
├── accounts/
├── recipes/
├── recipehub/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/rakshithaagowda/RecipeHub.git
```

### Navigate into the project

```bash
cd RecipeHub
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply migrations

```bash
python manage.py migrate
```

### Run the server

```bash
python manage.py runserver
```

---
## 🔑 Environment Variables

Create a `.env` file in the project root and add:

```env
SECRET_KEY=your_django_secret_key
GEMINI_API_KEY=your_google_gemini_api_key
DEBUG=True
```

## 🔗 API Endpoints

| Endpoint               | Description         |
| ---------------------- | ------------------- |
| `/api/recipes/`        | List all recipes    |
| `/api/categories/`     | List all categories |
| `/api/recipes/<slug>/` | Recipe details      |

---

## 📸 Screenshots

* 🏠 Home Page
* ⭐ Featured Recipes
* 📂 Categories
* 🍽 All Recipes
* 📖 Recipe Details
* 🤖 AI Recipe Assistant
* 🔐 Login
* 📝 Register
* ⚙ Admin Dashboard

## 📸 Screenshots

### 🏠 Home Page
![Home](screenshots/home.png)

---

### ⭐ Featured Recipes
![Featured Recipes](screenshots/featured-recipes.png)

---

### 📂 Categories
![Categories](screenshots/categories.png)

---

### 🍽️ All Recipes
![All Recipes](screenshots/all-recipes.png)

---

### 📖 Recipe Details
![Recipe Detail](screenshots/recipe-detail.png)

---

### 🤖 AI Recipe Assistant
![AI Recipe Assistant](screenshots/ai-recipe.png)

---

### 🔐 Login
![Login](screenshots/login.png)

---

### 📝 Register
![Register](screenshots/register.png)

---

## 📌 Future Enhancements

- ❤️ Favorite Recipes
- ⭐ Ratings & Reviews
- 👨‍🍳 User Recipe Uploads
- 📧 Password Reset via Email
- 🥗 Nutrition Information
- 📱 Progressive Web App (PWA)
---

## 👩‍💻 Author

**Rakshitha R S**

Bachelor of Engineering (Computer Science)

GitHub:
https://github.com/rakshithaagowda

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
