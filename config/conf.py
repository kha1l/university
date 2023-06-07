from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.environ.get("HOST")
BASE = os.environ.get("BASE")
USER = os.environ.get("USER")
PASS = os.environ.get("PASS")
