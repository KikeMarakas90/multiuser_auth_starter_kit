# 🔐 Multiuser Auth Starter Kit

A lightweight **Python starter kit** for multiuser authentication with JWT.  
Designed for local development (Alpine/iSH) and CI/CD pipelines (GitHub Actions).

---

## 📦 Features
- Session management with JWT
- Role-based access control (admin, user, etc.)
- Environment variables support (`.env`)
- Automated tests with Pytest

---

## 🚀 Installation

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

##▶️ Run Example

python main.py

##🧪 Run Tests

pytest

##⚙️ Environment Variables

SECRET_KEY=super_secret_key
ENVIRONMENT=development
SESSION_EXP_MINUTES=30

##✅ GitHub Actions CI/CD

This project includes a workflow example to:
•Install dependencies
•Run automated tests

