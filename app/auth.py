from flask import Flask , render_template,request,redirect,url_for,flash
from werkzeug.security import generate_password_hash,check_password_hash 
from .models import *
from dotenv import load_dotenv
import os
from. import crm_app

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
        
        if not username or not password: # ------
            flash("All Fields Are Required..")
            return redirect(url_for("login"))
        
        users_data=read_user()
        for user in users_data:
            if user["username"] == username:
                if check_password_hash(user["hashed_pass"], password):
                    flash("Logged in successfully..")
                    return redirect(url_for("dashboard"))
                else:
                    flash("Invalid Password")
                    return redirect(url_for("login"))
                       
        flash("Username Not Found.")
        return redirect(url_for("login"))
        
    return render_template("login.html",pagetitle = "Login Page")

# REGIISTER
@crm_app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password")
        
        if not username or not email or not password: # -----
            flash("All Fields Are Required..")
            return redirect(url_for("register"))
        
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

# Dashboard
@crm_app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html",pagetitle = "Dashboard")


