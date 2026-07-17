# 🚀 CareerFlow - AI Powered Career & Interview Preparation Platform

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?style=for-the-badge&logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?style=for-the-badge&logo=mysql)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent-green?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-LLM_Framework-success?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge)
![HuggingFace](https://img.shields.io/badge/HuggingFace-LLM-yellow?style=for-the-badge)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript)

</p>

---

# 📖 About The Project

CareerFlow is an AI-powered Interview Preparation and Career Tracking Platform developed to help students monitor interview experiences, analyze performance using Large Language Models (LLMs), and receive personalized recommendations to improve future interview outcomes.

Instead of manually remembering previous interviews, CareerFlow stores interview records and uses AI to identify mistakes, weak areas, strengths, and personalized study plans.

The platform acts as a personal AI Interview Mentor.

---

# 🎯 Problem Statement

Many students attend multiple interviews but fail to:

- Track interview history
- Learn from previous mistakes
- Identify weak technical skills
- Build personalized preparation plans

CareerFlow solves this problem using AI-powered interview analysis.

---

# ✨ Features

## 🔐 Authentication System

- User Registration
- Secure Login
- Password Hashing
- Flask Login Authentication
- Session Management
- Logout

---

## 📋 Interview Management

- Add Interview Details
- Company Name
- Applied Role
- Interview Date
- Interview Status
- Number of Rounds
- Interview Feedback
- Track Complete Interview History

---

## 🤖 AI Interview Analysis

Automatically analyzes every interview and generates:

- Interview Mistakes
- Weak Areas
- Technical Gaps
- Strengths
- Career Recommendations
- Personalized Study Plan

---

## 📊 Dashboard

- Interview Records
- AI Suggestions
- Career Insights
- Progress Tracking

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Flask |
| Authentication | Flask Login |
| Password Encryption | Flask Bcrypt |
| Database | MySQL |
| ORM | Flask-MySQLdb |
| AI Framework | LangChain |
| Agent Framework | LangGraph |
| LLM | HuggingFace Llama 3.1 |
| AI APIs | HuggingFace Endpoint |
| Markdown Rendering | Python Markdown |
| Environment Variables | Python Dotenv |

---

# 🏗 Project Architecture

```
                    User
                      │
          HTML • CSS • JavaScript
                      │
                 Flask Server
                      │
       ┌──────────────┼───────────────┐
       │                              │
 Authentication                 Interview Module
       │                              │
 Flask Login                 MySQL Database
       │                              │
       └──────────────┬───────────────┘
                      │
             AI Recommendation Engine
                      │
              LangGraph Workflow
                      │
             HuggingFace LLM
                      │
             AI Generated Report
                      │
                Dashboard
```

---

# ⚙️ Workflow

## Step 1

User creates an account.

↓

## Step 2

User logs in securely.

↓

## Step 3

Adds interview details.

↓

## Step 4

Interview data stored in MySQL.

↓

## Step 5

AI Recommendation Engine retrieves interview history.

↓

## Step 6

LangGraph sends structured prompts to LLM.

↓

## Step 7

AI analyzes

- mistakes
- weak skills
- interview performance

↓

## Step 8

Dashboard displays personalized recommendations.

---

# 🧠 AI Workflow

```
Interview Details
        │
        ▼
Prompt Builder
        │
        ▼
LangGraph State
        │
        ▼
LLM
        │
        ▼
Mistakes Analysis
        │
        ▼
Need to Focus
        │
        ▼
Study Plan
        │
        ▼
Career Recommendations
```

---

# 📂 Project Structure

```
CareerFlow/

│
├── main.py
├── database.py
├── interview_details.py
├── AIRecomm.py
├── Analyze_interviews.py
├── monitor_interviews.py
│
├── static/
│      ├── css/
│      ├── js/
│      └── images/
│
├── templates/
│      ├── Hero.html
│      ├── Login.html
│      ├── Signup.html
│      ├── Dashboard.html
│      └── ...
│
├── requirements.txt
│
├── .env
│
└── README.md
```

---

# 🗄 Database Design

## Table : login_credits

| Column |
|----------|
| user_id |
| full_name |
| user_email |
| user_password |

---

## Table : interview_details

| Column |
|-----------|
| interview_id |
| user_id |
| company_name |
| applied_role |
| interview_date |
| interview_status |
| rounds_attended |
| feedback |

---

# 🔐 Authentication Flow

```
Signup
   │
Password Hash
   │
Store in Database
   │
Login
   │
Verify Password
   │
Flask Login
   │
Session Created
   │
Dashboard
```

---

# 🤖 AI Recommendation Engine

The AI engine uses LangGraph to execute multiple reasoning stages.

### Stage 1

Interview Analysis

↓

### Stage 2

Mistake Identification

↓

### Stage 3

Weak Skill Detection

↓

### Stage 4

Study Plan Generation

↓

### Stage 5

Career Recommendation

---

# 📊 AI Output

For every interview the system generates:

✅ Mistakes

✅ Weak Areas

✅ Strengths

✅ Need to Focus

✅ Study Plan

✅ Career Recommendations

---

# 💻 Installation

Clone Repository

```bash
git clone https://github.com/yourusername/CareerFlow.git
```

Go inside project

```bash
cd CareerFlow
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

# ⚙ Environment Variables

Create

```
.env
```

Add

```env
MYSQL_HOST=

MYSQL_USER=

MYSQL_PASSWORD=

MYSQL_DB=

HuggingFaceHub_API_Token=

GROQ_API_KEY=
```

---

# 📈 Future Enhancements

- Resume ATS Analyzer
- AI Resume Builder
- AI Mock Interview
- Voice Interview Assistant
- Coding Assessment
- Resume Score
- Job Recommendation
- Company Wise Questions
- Email Notifications
- Analytics Dashboard
- Resume Improvement Suggestions
- AI Career Roadmap
- Interview Calendar
- AI Chat Assistant

---

# 🚀 Why CareerFlow?

- Personalized Interview Analysis
- AI Powered Suggestions
- Career Tracking
- Interview History
- Secure Authentication
- Modern Web Application
- Easy to Extend
- Recruiter Friendly Project
- Demonstrates Full Stack + AI Integration

---

# 👨‍💻 Author

**Akshay Kompally**

Computer Science Engineering Student

GitHub: https://github.com/Akshaykompally

---

# ⭐ If you like this project

Give it a ⭐ on GitHub and support the project!
