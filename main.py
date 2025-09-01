from src.auth_manager import AuthManager
from src import config

def main():
    print(f"🔐 Multiuser Auth Starter Kit (Environment: {config.ENVIRONMENT})")

    auth = AuthManager()

    # Demo session
    token = auth.create_session("user123", "admin")
    print(f"✅ Session created: {token}")

    # Validate role
    is_admin = auth.has_role(token, "admin")
    print(f"👤 Is admin? {is_admin}")

if __name__ == "__main__":
    main()
