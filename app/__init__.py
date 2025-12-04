import os
from flask import Flask
from dotenv import load_dotenv
from .db import init_db

load_dotenv()
#init_db()
crm_app=Flask(__name__)
crm_app.secret_key=os.getenv("APP_SECRET_KEY")

from . import auth,routes
