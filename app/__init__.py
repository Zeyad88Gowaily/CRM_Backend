import os
from flask import Flask
from dotenv import load_dotenv
from .db import init_db
from flask_login import LoginManager
from .models import User
from flask_wtf.csrf import CSRFProtect


load_dotenv()
#init_db()

crm_app=Flask(__name__)
crm_app.secret_key=os.getenv("APP_SECRET_KEY")

# Login Manager for handling user sessions
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(crm_app)

# CSRF Protection
csrf = CSRFProtect(crm_app)

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)


from . import auth,routes
