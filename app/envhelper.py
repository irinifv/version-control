import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(var_name, default_value=None):
    """Returns the environment variable or a default value if not set."""
    return os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

#API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")