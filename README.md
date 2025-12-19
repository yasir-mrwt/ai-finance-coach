📦 Flask Fullstack Project Structure (Starter Template)

This repository provides a clean and scalable Flask fullstack folder structure designed for small to medium web applications.
It includes routes, modules, templates, static files, and an app factory setup — perfect for beginners to understand how real Flask applications are organized.

🚀 Features

Modular backend with routes + blueprints

Organized templates with Jinja inheritance

Static assets folder (CSS, JS, Images)

Example modules for business logic separation

Ready-to-extend structure for any Flask project

Clean and industry-standard layout

📁 Project Structure
flask-fullstack-structure/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── app/
│ ├── **init**.py
│ ├── routes/
│ │ ├── **init**.py
│ │ ├── home_routes.py
│ │ ├── auth_routes.py
│ │ └── api_routes.py
│ │
│ ├── modules/
│ │ ├── **init**.py
│ │ ├── finance.py
│ │ ├── utils.py
│ │ └── ai_engine.py
│ │
│ ├── templates/
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── dashboard.html
│ │ ├── finance.html
│ │ └── components/
│ │ ├── navbar.html
│ │ └── cards.html
│ │
│ ├── static/
│ ├── css/
│ │ └── style.css
│ ├── js/
│ │ └── app.js
│ └── img/
│ └── placeholder.png
│
└── instance/
└── config.py

⚙️ Setup Instructions
1️⃣ Create & Activate Virtual Environment
python -m venv venv
.\venv\Scripts\Activate.ps1

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the App
python app.py

🛠 Tech Stack

Python

Flask

Jinja2

HTML / CSS / JavaScript

🎯 Purpose of This Repository

This template is intended for:

Students learning Flask

Developers wanting a clean structure

Beginners confused about templates, static, routes, and modules

Anyone building a small fullstack website with Python

⭐ Contributions

Feel free to fork, improve structure, or create issues.
