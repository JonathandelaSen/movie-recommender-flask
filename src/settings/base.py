from pathlib import Path
from environs import Env, load_dotenv

PROJECT_DIR = Path(__file__).parent.parent

env = Env()
load_dotenv(PROJECT_DIR / ".env")

log_level = env.log_level("LOG_LEVEL", "INFO")
environment = env.str("CONFIG_CLASS", "production").lower()


class BaseConfig:
    MONGO_URI = env.str("MONGO_URI", "")
    TMDB_APY_KEY = env.str("TMDB_APY_KEY", "")
