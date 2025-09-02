import jwt
from datetime import datetime, timedelta
from src.secure_config import SECRET_KEY, ALGORITHM, TOKEN_EXPIRE_MINUTES
from src.secure_logger import logger

class SecureAuthManager:
    def create_session(self, user_id: str, role: str) -> str:
        try:
            payload = {
                "sub": user_id,
                "role": role,
                "exp": datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
            logger.info(f"✅ Session created for user {user_id}")
            return token
        except Exception as e:
            logger.error(f"❌ Error creating session: {e}")
            raise

    def has_role(self, token: str, required_role: str) -> bool:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            has_role = payload.get("role") == required_role
            logger.info(f"Checked role for token: {has_role}")
            return has_role
        except jwt.ExpiredSignatureError:
            logger.warning("⚠️ Token expired")
            return False
        except jwt.InvalidTokenError as e:
            logger.error(f"❌ Invalid token: {e}")
            return False
