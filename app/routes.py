from flask import Flask , render_template,request,redirect,url_for,flash
from .models import *
from app.auth import crm_app

@crm_app.route("/dashboard/users")
def users():
    return "<h1>Users List</h1>"
    #return render_template("users.html",pagetitle="Users Page")
    
@crm_app.route("/dashboard/contacts")
def contacts():
    return "<h1>Contacts List</h1>"
    #return render_template("contacts.html",pagetitle="Contacts Page")

@crm_app.route("/dashboard/companies")
def comapnies():
     return "<h1>Comapnies List</h1>"
    #return render_template("companies.html",pagetitle="Companies Page")

@crm_app.route("/dashboard/deals")
def deals():
    return "<h1>Deals List</h1>"
    #return render_template("deals.html",pagetitle="Deals Page")