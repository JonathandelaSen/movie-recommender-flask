import os
import multiprocessing
from pathlib import Path
from environs import Env, load_dotenv

env = Env()
load_dotenv(Path(__file__).parent / ".env")

bind = "0.0.0.0:5000"
workers = multiprocessing.cpu_count() * 2 + 1


for name, value in os.environ.items():
    _name = name.lower()
    if _name.startswith("gunicorn_"):
        globals()[_name.lstrip("gunicorn_")] = value

loglevel = env.str("LOG_LEVEL", "INFO")


# def on_starting(server):
#     import subprocess
#     subprocess.Popen(["flask", "db", "upgrade", "-d", "database/migrations"], cwd="src")
