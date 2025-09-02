from src.secure_auth_manager import SecureAuthManager
from src.secure_config import ALGORITHM
from src.secure_logger import logger

def main():
    logger.info(f"🔐 Testing Multiuser Auth (Algorithm: {ALGORITHM})")

    auth = SecureAuthManager()
    token = auth.create_session("user123", "admin")
    logger.info(f"Token created: {token}")

    is_admin = auth.has_role(token, "admin")
    logger.info(f"Is admin: {is_admin}")

if __name__ == "__main__":
    main()
