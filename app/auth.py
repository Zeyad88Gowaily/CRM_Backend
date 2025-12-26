from flask import Flask , render_template,request,redirect, session,url_for,flash
from werkzeug.security import generate_password_hash,check_password_hash 
from .models import *
from dotenv import load_dotenv
import os
from. import crm_app
from flask_login import login_user,logout_user,login_required,current_user

load_dotenv()

crm_app.secret_key=os.getenv("APP_SECRET_KEY")

# Welcome Page
@crm_app.route("/")
def Welcome():
    return render_template("welcome.html",pagetitle="Robocop")

# LOGIN
@crm_app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        
        if not username or not password: 
            flash("All Fields Are Required..")
            return redirect(url_for("login"))
        
        # NEW LOGIC (CLEAN + MORE SECURE (Not Exposing All Data) + EFFICIENT)
        user_data=read_user_byUsername(username) # Added to models.py Phase 3
        if not user_data:
            flash("Username Not Found.")
            return redirect(url_for("login"))
        
        if not check_password_hash(user_data["hashed_pass"],password):
            flash("Incorrect Password.")
            return redirect(url_for("login"))
        
        user_obj=User(*user_data) # Same as commented line below *(is used to unpack the dictionary into arguments)
        """user_obj=User(
            user_data["ID"],
            user_data["username"],
            user_data["email"],
            user_data["hashed_pass"],
            user_data["created_at"]
            )"""
        login_user(user_obj)
        flash("Logged in Successfully.")
        return redirect(url_for("dashboard"))
                   
    return render_template("login.html",pagetitle = "Login Page")

# REGIISTER
@crm_app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password")
        
        if not username or not email or not password: 
            flash("All Fields Are Required..")
            return redirect(url_for("register"))
        
        # Not the best logic "MUST be changed Later"
        users_data=read_user()
        for user in users_data:
            if user["username"] == username or user["email"] == email:
                flash("Username or Email Already Registered.")
                return redirect(url_for("register"))
        
        #hashing the password
        hash_pass=generate_password_hash(password)
        create_user(username,email,hash_pass)
        flash("Account Created Successfully.. Login Now")
        return redirect(url_for("login"))               
        
    return render_template("register.html",pagetitle ="Register Page")


@crm_app.route("/logout", methods=["GET","POST"])
@login_required
def logout():
    logout_user()
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for("login"))

# Dashboard
@crm_app.route("/dashboard")
@login_required
def dashboard():
    #print(current_user.id)
    #print(current_user.username)
    #print(current_user.email)
    #print(current_user.is_authenticated)
    
    return render_template("dashboard.html",pagetitle = "Dashboard")


