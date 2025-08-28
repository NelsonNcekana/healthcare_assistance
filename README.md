# 🏥 Healthcare Assistant

AI-powered chatbot platform to support healthcare queries and patient triage.

---

##  Overview

This project is designed to assist users with common healthcare inquiries,
provide initial triage recommendations, and serve as a learning tool for health-focused AI applications.

---

##  Features

- AI-based question understanding and response generation
- Patient symptom guidance and triage suggestions
- Future support for natural language input and direct chat interface

---

##  Tech Stack

| Component        | Tool / Framework       |
|------------------|------------------------|
| Backend          | Python, (Flask or Django) |
| AI / NLP         | OpenAI API, spaCy, scikit-learn |
| Data Storage     | SQLite / PostgreSQL    |
| Deployment       | Docker, Gunicorn, nginx (optional) |

---

##  Setup & Usage

```bash
git clone https://github.com/SenzoN95/healthcare_assistance.git
cd healthcare_assistance
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt

# Run (Flask example)
export FLASK_APP=app.py
flask run  # Or `python app.py`
