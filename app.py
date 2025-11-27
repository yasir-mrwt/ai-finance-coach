from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os
from datetime import datetime
from dotenv import load_dotenv 

load_dotenv()

app = Flask(__name__)
app.secret_key = 'finance-coach321'

# Admin credentials
ADMIN_USERNAME = 'yasirgotnoChill'
ADMIN_PASSWORD = 'admin123'

# Data file path
DATA_FILE = 'data.json'

# Lazy load Groq client
_groq_client = None

def get_groq_client():
    """Lazy load Groq client to avoid initialization errors"""
    global _groq_client
    if _groq_client is None:
        try:
            from groq import Groq
            _groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        except Exception as e:
            print(f"Warning: Could not initialize Groq client: {e}")
            _groq_client = False
    return _groq_client if _groq_client is not False else None

def load_data():
    """Load data from JSON file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                content = f.read().strip()
                if not content:  # File is empty
                    return []
                return json.loads(content)
        except json.JSONDecodeError:
            # If JSON is invalid, backup old file and return empty list
            if os.path.exists(DATA_FILE):
                os.rename(DATA_FILE, f'{DATA_FILE}.backup')
            return []
        except Exception as e:
            print(f"Error loading data: {e}")
            return []
    return []

def save_data(data):
    """Save data to JSON file"""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving data: {e}")

def get_ai_analysis(salary, expenses, savings_goal, notes):
    """Get AI-powered financial analysis using Groq"""
    total_expenses = sum(expenses.values())
    remaining = salary - total_expenses
    
    prompt = f"""You are a professional financial advisor. Analyze this financial situation:

Monthly Salary: ${salary}
Expenses:
{chr(10).join([f'- {k}: ${v}' for k, v in expenses.items()])}
Total Expenses: ${total_expenses}
Remaining: ${remaining}
Savings Goal: ${savings_goal}
Additional Notes: {notes}

Provide a comprehensive financial analysis with:
1. A financial stability score (0-100)
2. Personalized savings advice
3. Monthly budget recommendations
4. Expense warnings if any
5. Smart tips to reach the savings goal
6. Spending breakdown analysis

Be specific, encouraging, and actionable. Format your response clearly."""

    groq_client = get_groq_client()
    
    if groq_client is None:
        return f"""Basic Financial Analysis:

Your remaining balance is ${remaining:.2f}. 
To reach your savings goal of ${savings_goal:.2f}, you need to save ${max(0, savings_goal - remaining):.2f} more per month.

Monthly Income: ${salary:.2f}
Total Expenses: ${total_expenses:.2f}
Remaining: ${remaining:.2f}

Recommendations:
1. Review your largest expense categories
2. Consider reducing non-essential spending
3. Set up automatic transfers to savings account
4. Track daily expenses to identify saving opportunities

Note: AI analysis is temporarily unavailable. Please check your Groq API configuration."""

    try:
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert financial advisor who provides clear, actionable advice."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=1500
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"""Basic Financial Analysis:

Your remaining balance is ${remaining:.2f}. 
To reach your savings goal of ${savings_goal:.2f}, you need to save ${max(0, savings_goal - remaining):.2f} more per month.

Error: {str(e)}

Monthly Income: ${salary:.2f}
Total Expenses: ${total_expenses:.2f}
Remaining: ${remaining:.2f}

Basic Recommendations:
1. Review your expense breakdown carefully
2. Identify areas where you can reduce spending
3. Set realistic savings targets
4. Consider the 50/30/20 budgeting rule (50% needs, 30% wants, 20% savings)"""

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/finance-form')
def finance_form():
    return render_template('finance_form.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Get form data
        salary = float(request.form.get('salary', 0))
        expenses = {
            'rent': float(request.form.get('rent', 0)),
            'food': float(request.form.get('food', 0)),
            'transportation': float(request.form.get('transportation', 0)),
            'utilities': float(request.form.get('utilities', 0)),
            'entertainment': float(request.form.get('entertainment', 0)),
            'other': float(request.form.get('other', 0))
        }
        savings_goal = float(request.form.get('savings_goal', 0))
        notes = request.form.get('notes', '')
        
        # Calculate totals
        total_expenses = sum(expenses.values())
        remaining = salary - total_expenses
        
        # Get AI analysis
        ai_analysis = get_ai_analysis(salary, expenses, savings_goal, notes)
        
        # Save to data.json
        data = load_data()
        entry = {
            'id': len(data) + 1,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'salary': salary,
            'expenses': expenses,
            'total_expenses': total_expenses,
            'remaining': remaining,
            'savings_goal': savings_goal,
            'notes': notes,
            'ai_analysis': ai_analysis
        }
        data.append(entry)
        save_data(data)
        
        return render_template('result.html', 
                             salary=salary,
                             expenses=expenses,
                             total_expenses=total_expenses,
                             remaining=remaining,
                             savings_goal=savings_goal,
                             ai_analysis=ai_analysis)
    except Exception as e:
        print(f"Error in analyze route: {e}")
        return f"An error occurred: {str(e)}", 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error='Invalid credentials')
    
    return render_template('login.html')

@app.route('/admin')
def admin():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    
    data = load_data()
    return render_template('admin.html', entries=data)

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('home'))

@app.route('/delete-entry/<int:entry_id>')
def delete_entry(entry_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    
    data = load_data()
    data = [entry for entry in data if entry['id'] != entry_id]
    save_data(data)
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)