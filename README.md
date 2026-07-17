# 🚀 CareerFlow - AI Powered Career & Interview Preparation Platform

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?style=for-the-badge&logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?style=for-the-badge&logo=mysql)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent-green?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-LLM_Framework-success?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript)

</p>

---

# 📖 About The Project

**CareerFlow** is an AI-powered career management platform designed to help students, fresh graduates, and job seekers organize their interview journey, analyze interview performance, and improve future interview success using Artificial Intelligence.

The platform enables users to securely manage interview records while leveraging **LangGraph** and **Large Language Models (LLMs)** to generate personalized feedback, identify technical weaknesses, recommend learning resources, and build customized preparation plans.

CareerFlow acts as your **personal AI Interview Coach**, helping you prepare smarter after every interview.

---

# 🎯 Problem Statement

Most candidates attend multiple interviews but struggle to:

- Track previous interview experiences
- Remember technical questions asked
- Learn from interview mistakes
- Identify weak technical areas
- Create structured preparation plans
- Monitor interview progress over time

CareerFlow solves these challenges by combining interview management with AI-powered analysis.

---

# ✨ Features

## 🔐 Secure Authentication

- User Registration
- Secure Login
- Password Hashing using Flask-Bcrypt
- Flask-Login Authentication
- Session Management
- Logout Functionality

---

## 📋 Interview Management

Users can:

- Add Interview Details
- Edit Existing Interviews
- Delete Interview Records
- Track Interview Status
- Store Interview Feedback
- Maintain Complete Interview History

Interview Details Include:

- Company Name
- Applied Role
- Interview Date
- Number of Interview Rounds
- Interview Status
- Technical Questions
- Personal Feedback
- Additional Notes

---

## 🤖 AI Interview Analysis

CareerFlow intelligently analyzes interview experiences and generates:

- Interview Mistakes
- Technical Weak Areas
- Strong Skills
- Learning Recommendations
- Personalized Study Plan
- Future Interview Strategy
- Career Guidance

The AI recommendations are generated using **LangGraph** workflows integrated with **LLMs**.

---

## 📊 Dashboard

The interactive dashboard provides:

- Total Interviews
- Selected Interviews
- Rejected Interviews
- Pending Interviews
- AI Recommendations
- Career Progress
- Interview Analytics

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Flask |
| Programming Language | Python |
| Database | MySQL |
| Authentication | Flask-Login |
| Password Security | Flask-Bcrypt |
| Database Connector | Flask-MySQLdb |
| AI Framework | LangChain |
| Workflow Engine | LangGraph |
| LLM Provider | Groq |
| Embedding/LLM Support | Hugging Face |
| Environment Variables | Python-dotenv |
| Markdown Rendering | Python-Markdown |

---

# 🏗 System Architecture

```text
                     User
                       │
        HTML • CSS • JavaScript Frontend
                       │
                  Flask Backend
                       │
      ┌────────────────┼────────────────┐
      │                                 │
Authentication                 Interview Management
      │                                 │
 Flask Login                   MySQL Database
      │                                 │
      └────────────────┼────────────────┘
                       │
              AI Recommendation Engine
                       │
                LangGraph Workflow
                       │
             Prompt Engineering Layer
                       │
                  Groq / Hugging Face
                       │
             AI Generated Recommendations
                       │
                  Dashboard Display
```

---

# ⚙️ Application Workflow

### Step 1

User creates an account.

↓

### Step 2

Logs in securely.

↓

### Step 3

Adds interview details.

↓

### Step 4

Interview information is stored in MySQL.

↓

### Step 5

The AI Recommendation Engine retrieves interview history.

↓

### Step 6

LangGraph processes structured prompts.

↓

### Step 7

The LLM analyzes:

- Technical Skills
- Interview Performance
- Mistakes
- Strengths
- Weak Areas

↓

### Step 8

Personalized recommendations are displayed on the dashboard.

---

# 🧠 AI Workflow

```text
Interview Details
        │
        ▼
Prompt Builder
        │
        ▼
LangGraph Workflow
        │
        ▼
Large Language Model
        │
        ▼
Interview Analysis
        │
        ▼
Mistake Detection
        │
        ▼
Skill Gap Analysis
        │
        ▼
Study Plan Generation
        │
        ▼
Career Recommendations
```

---

# 📂 Project Structure

```text
CareerFlow/
│
├── main.py
├── database.py
├── interview_details.py
├── Analyze_interviews.py
├── AIRecomm.py
├── monitor_interviews.py
├── requirements.txt
├── .env
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── Hero.html
│   ├── Login.html
│   ├── Signup.html
│   ├── Dashboard.html
│   ├── Interview.html
│   ├── History.html
│   └── AI.html
│
└── README.md
```

---

# 🗄 Database Schema

## login_credits

| Column |
|---------|
| user_id |
| full_name |
| user_email |
| user_password |

---

## interview_details

| Column |
|---------|
| interview_id |
| user_id |
| company_name |
| applied_role |
| interview_date |
| interview_status |
| rounds_attended |
| interview_feedback |

---

# 🔐 Authentication Flow

```text
Signup
   │
   ▼
Password Hashing
   │
   ▼
Store Credentials
   │
   ▼
Login
   │
   ▼
Password Verification
   │
   ▼
Flask Login Session
   │
   ▼
Dashboard Access
```

---

# 🤖 AI Recommendation Engine

The AI engine executes multiple reasoning stages using LangGraph.

### Stage 1

Interview Analysis

↓

### Stage 2

Mistake Identification

↓

### Stage 3

Technical Skill Gap Detection

↓

### Stage 4

Study Plan Generation

↓

### Stage 5

Career Recommendations

---

# 📊 AI Output

For every interview, CareerFlow generates:

- ✅ Interview Mistakes
- ✅ Weak Technical Areas
- ✅ Strengths
- ✅ Topics to Focus
- ✅ Personalized Study Plan
- ✅ Career Recommendations

---

# 💻 Installation

## Clone the Repository

```bash
git clone https://github.com/Akshaykompally/CareerFlow.git
```

```bash
cd CareerFlow
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate (Windows)

```bash
venv\Scripts\activate
```

### Activate (Linux/macOS)

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=careerflow

GROQ_API_KEY=your_groq_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
```

---

## Run the Application

```bash
python main.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 📦 Main Dependencies

- Flask
- Flask-Login
- Flask-Bcrypt
- Flask-MySQLdb
- LangChain
- LangGraph
- Groq
- Hugging Face
- Python-dotenv
- Markdown

---

# 🚀 Future Enhancements

- AI Resume Builder
- ATS Resume Checker
- Resume Score Analysis
- Mock Interview Simulator
- Voice Interview Assistant
- Coding Assessment Module
- Company-wise Interview Questions
- Job Recommendation System
- Resume Improvement Suggestions
- Email Notifications
- Calendar Integration
- AI Career Roadmap
- Analytics Dashboard
- PDF Report Generation

---

# 🚀 Why CareerFlow?

- AI-Powered Interview Analysis
- Personalized Career Recommendations
- Interview History Tracking
- Secure Authentication
- Interactive Dashboard
- Full Stack Flask Application
- LangGraph Agent Workflow
- Modern AI Integration
- Recruiter-Friendly Project

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Akshay Kompally**

Computer Science Engineering Student

GitHub: https://github.com/Akshaykompally

LinkedIn: *Add your LinkedIn profile here*

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

Your support motivates further development and improvements!

**Happy Coding! 🚀**
