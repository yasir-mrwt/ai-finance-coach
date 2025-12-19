# 💰 AI-Powered Personal Finance Coach

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![AI](https://img.shields.io/badge/Groq-AI-7C3AED?style=for-the-badge&logo=ai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An intelligent web application that provides personalized financial advice, budget planning, and expense analysis powered by AI.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack)

---

</div>

## 🎯 About

AI Finance Coach helps users make better financial decisions through AI-powered analysis. Input your income and expenses to receive personalized advice, budget recommendations, and visual insights into spending patterns.

### Key Highlights

- 🤖 Real AI integration using Groq's LLaMA 3.3 70B
- 📊 Interactive charts with Chart.js
- 💾 No database required - uses JSON storage
- 🔐 Secure admin dashboard
- 📱 Fully responsive design

## ✨ Features

- **Financial Analysis Form** - Track salary, 6 expense categories, and savings goals
- **AI-Powered Insights** - Get stability scores, savings advice, and budget recommendations
- **Visual Reports** - Interactive pie and bar charts
- **Admin Dashboard** - View all submissions, detailed analytics, and manage entries
- **Modern UI** - Gradient design with smooth animations

## 🛠️ Tech Stack

- **Backend:** Python, Flask 3.0
- **AI:** Groq API (LLaMA 3.3 70B)
- **Frontend:** HTML5, CSS3, JavaScript
- **Templating:** Jinja2
- **Charts:** Chart.js
- **Storage:** JSON

## 📁 Project Structure

```
ai-finance-coach/
├── app.py                 # Main Flask application
├── requirements.txt       # Dependencies
├── data.json             # Data storage (auto-generated)
├── static/
│   └── styles.css        # All styling
└── templates/
    ├── base.html         # Base template
    ├── home.html         # Landing page
    ├── finance_form.html # Input form
    ├── result.html       # Analysis results
    ├── login.html        # Admin login
    └── admin.html        # Admin dashboard
```

## 🚀 Installation

### Prerequisites

- Python 3.8+
- pip
- Groq API key ([Get it free](https://console.groq.com/))

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/yasir-mrwt/ai-finance-coach.git
cd ai-finance-coach

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variable
export GROQ_API_KEY='your-groq-api-key'  # Windows: set GROQ_API_KEY=your-key

# 5. Run the application
python app.py
```

Visit `http://127.0.0.1:5000`

### Environment Configuration

Create a `.env` file (optional):

```env
GROQ_API_KEY=your-groq-api-key-here
SECRET_KEY=your-secret-key-here
```

## 💻 Usage

### For Users

1. Go to `http://127.0.0.1:5000`
2. Click "Start Your Analysis"
3. Fill in salary, expenses, and savings goal
4. Submit to get AI-powered financial advice
5. View charts and recommendations

### For Admins

1. Navigate to `/login`
2. Login with: `admin` / `admin123`
3. View all submissions and analytics
4. Delete entries if needed

**⚠️ Change default admin credentials in production!**

## 🔑 API Configuration

### Getting Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up for free
3. Generate API key
4. Add to environment variables

### Available Models

Default: `llama-3.3-70b-versatile`

Change in `app.py`:
```python
model="llama-3.3-70b-versatile"  # Modify here
```

## 🚢 Deployment

### Heroku

```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
heroku create your-app-name
heroku config:set GROQ_API_KEY=your-key
git push heroku main
```

### Render / Railway

1. Connect GitHub repository
2. Set environment variables
3. Auto-deploy

## 🤝 Contributing

Contributions are welcome! 

1. Fork the project
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Contact

**Yasir** 

- GitHub: [@yasir-mrwt](https://github.com/yasir-mrwt)
- Email: yasirmarwat09@gmail.com
- LinkedIn: [Yasir Marwat](https://linkedin.com/in/yasir-marwat)

**Project Link:** [https://github.com/yasir-mrwt/ai-finance-coach](https://github.com/yasir-mrwt/ai-finance-coach)

## 🙏 Acknowledgments

- [Groq](https://groq.com/) - Free AI API access
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Chart.js](https://www.chartjs.org/) - Data visualizations
- Python community for continuous support

---

<div align="center">

**⭐ If you found this helpful, please star the repository!**

Made with ❤️ by [Yasir](https://github.com/yasir-mrwt)

</div>
