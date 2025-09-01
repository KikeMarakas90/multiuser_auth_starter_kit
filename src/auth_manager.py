import jwt
import datetime
from src import config

class AuthManager:
    def __init__(self):
        self.secret_key = config.SECRET_KEY
        self.algorithm = config.ALGORITHM
        self.session_exp_minutes = config.SESSION_EXP_MINUTES

    def create_session(self, user_id: str, role: str) -> str:
        """
        Creates a JWT token with user_id and role.
        """
        expiration = datetime.datetime.utcnow() + datetime.timedelta(
            minutes=self.session_exp_minutes
        )
        payload = {
            "user_id": user_id,
            "role": role,
            "exp": expiration,
        }
        token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        return token

    def validate_session(self, token: str) -> dict:
        """
        Validates the JWT token and returns the decoded payload.
        """
        try:
            decoded = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return decoded
        except jwt.ExpiredSignatureError:
            raise ValueError("Session expired")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token")

    def has_role(self, token: str, required_role: str) -> bool:
        """
        Checks if the user has the required role.
        """
        decoded = self.validate_session(token)
        return decoded.get("role") == required_role
