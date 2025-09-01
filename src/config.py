import os
from dotenv import load_dotenv

# Load environment variables from .env if exists
load_dotenv()

# Environment configs
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
ALGORITHM = "HS256"
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
SESSION_EXP_MINUTES = int(os.getenv("SESSION_EXP_MINUTES", "30"))
