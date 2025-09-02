from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# App configuration
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
TOKEN_EXPIRE_MINUTES = int(os.getenv("TOKEN_EXPIRE_MINUTES", 60))

# Validate critical variables
if not SECRET_KEY or SECRET_KEY == "YOUR_SECRET_KEY_HERE":
    raise ValueError("b SECRET_KEY is not set properly in the environment variables")
