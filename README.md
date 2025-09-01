# 🔐 Multiuser Auth Starter Kit

A lightweight **Python starter kit** for multiuser authentication with JWT.  
Optimized for **local development** (Alpine/iSH) and **CI/CD pipelines** (GitHub Actions).

---

## 📦 Features

- **Session Management**: Secure JWT-based authentication.
- **Role-Based Access Control**: Supports roles like `admin`, `user`, etc.
- **Environment Configuration**: Easily configurable via `.env` files.
- **Automated Testing**: Integrated with Pytest for seamless testing.
- **CI/CD Integration**: Example GitHub Actions workflow for automation.

---

## 🚀 Installation

\`\`\`bash
# 1️⃣ Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2️⃣ Install dependencies
pip install -r requirements.txt
\`\`\`

---

## ▶️ Usage

\`\`\`bash
# Run the main application
python main.py

# Run automated tests
pytest
\`\`\`

---

## ⚙️ Configuration

Set the following environment variables (e.g., in `.env`):

\`\`\`env
SECRET_KEY=super_secret_key
ENVIRONMENT=development
SESSION_EXP_MINUTES=30
\`\`\`

---

## ✅ CI/CD with GitHub Actions

The project includes a workflow example to:

- Install dependencies
- Run automated tests
- Prepare for deployment

---

## 🧪 Testing

To run tests:

\`\`\`bash
pytest
\`\`\`

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please fork this repository, create a new branch, and submit a pull request with your proposed changes.

---

## 📬 Contact

For inquiries or support, please reach out to [enr1qu3rdza9021@outlook.com](mailto:enr1qu3rdza9021@outlook.com).

---

## 🔗 Links

- [GitHub Repository](https://github.com/KikeMarakas90/multiuser_auth_starter_kit)
- [Documentation](https://github.com/KikeMarakas90/multiuser_auth_starter_kit/wiki)
