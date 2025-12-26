from flask import Flask, abort, render_template, request,redirect ,url_for ,flash
from .models import *
from app.auth import crm_app
from email_validator import validate_email, EmailNotValidError
from flask_login import login_required, current_user


''' #################################### CRUD Operations ######################################### '''
# contacts Table
@crm_app.route("/dashboard/contacts", methods=["POST"]) 
@login_required
def create_contact_route():
        name=request.form.get("name")
        phone=request.form.get("phone")
        email=request.form.get("email")
        company_id=request.form.get("company_id")
        notes=request.form.get("notes")
        
        # Required fields
        if not name or not phone or not email or not company_id:
            flash("Name, Phone and Email are required.")
            return redirect(url_for("contacts"))
    
        try:
            validate_email(email)
            company_id = int(company_id)
        except (EmailNotValidError, ValueError):
            flash("Invalid Email Address or Company ID.")
            return redirect(url_for("contacts"))
        
        company=read_company_byID(company_id)
        if not company:
            flash(f"No company found with ID {company_id}")
            return redirect(url_for("contacts"))
        
        create_contact(name,phone,email,company_id,notes) # models.py function
        
        flash("Contact Created Successfully.")
        return redirect(url_for("contacts"))
 
 
 # UPDATE BY ID
@crm_app.route("/dashboard/contacts/update", methods=["POST"])
@login_required
def update_contact_route():
    contact_id = request.form.get("contact_id")
    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    company_id = request.form.get("company_id")
    notes = request.form.get("notes")

    # Required fields
    if not contact_id or not name or not phone or not email:
        flash("Contact ID, Name, Phone, and Email are required.")
        return redirect(url_for("contacts"))
    
    try:
        validate_email(email)
        contact_id = int(contact_id)
    except (EmailNotValidError, ValueError):
        flash("Invalid Email Address or Contact ID.")
        return redirect(url_for("contacts"))

    contact = read_contact_byID(contact_id)
    if not contact:
        flash(f"No contact found with ID {contact_id}")
        return redirect(url_for("contacts"))

    update_contact(name, phone, email, company_id, notes, contact_id)
    flash("Contact Updated Successfully.")
    return redirect(url_for("contacts"))

    
# DELETE BY ID    
@crm_app.route("/dashboard/contacts/delete", methods=["POST"])    
@login_required
def delete_contact_route():
    contact_id = request.form.get("contact_id")
    
    if not contact_id:
        flash("Contact ID is required.")
        return redirect(url_for("contacts"))
    
    try:
        contact_id = int(contact_id)
    except ValueError:
        flash("Contact ID must be a number.")
        return redirect(url_for("contacts"))
    
    contact = read_contact_byID(contact_id)
    if not contact:
        flash(f"No contact found with ID {contact_id}")
        return redirect(url_for("contacts"))
    
    delete_contact(contact_id)
    flash("Contact Deleted Successfully.")
    return redirect(url_for("contacts"))



########################################## COMPANIES ##############################################

@crm_app.route("/dashboard/companies", methods=["POST"])       
@login_required
def create_company_route():
        name=request.form.get("name")
        industry=request.form.get("industry")
        address=request.form.get("address")
        
        if not name or not industry or not address:
            flash("All Fields Are Required..")
            return redirect(url_for("companies"))
        
        create_company(name,industry,address)
        
        flash("Company Created Successfully.")
        return redirect(url_for("companies"))
    
    
# UPDATE BY ID    
@crm_app.route("/dashboard/companies/update", methods=["POST"])
@login_required
def update_company_route():
    # try except here for company_id conversion
    company_id = request.form.get("company_id")
    name = request.form.get("name")
    industry = request.form.get("industry")
    address = request.form.get("address")
    
    if not company_id or not name or not industry or not address:
        flash("All Fields Are Required..")
        return redirect(url_for("companies"))
    
    try:
        company_id = int(company_id)
    except ValueError:
        flash("Company ID must be a number.")
        return redirect(url_for("companies"))
    
    company = read_company_byID(company_id)
    if not company:
        flash(f"No company found with ID {company_id}")
        return redirect(url_for("companies"))
    
    update_company(name, industry, address, company_id)
    flash("Company Updated Successfully.")
    return redirect(url_for("companies"))


# DELETE BY ID
@crm_app.route("/dashboard/companies/delete", methods=["POST"])
@login_required
def delete_company_route():
    company_id = request.form.get("company_id")
    
    if not company_id:
        flash("Company ID is required.")
        return redirect(url_for("companies"))
    
    try:
        company_id = int(company_id)
    except ValueError:
        flash("Company ID must be a number.")
        return redirect(url_for("companies"))
    
    company = read_company_byID(company_id)
    if not company:
        flash(f"No company found with ID {company_id}")
        return redirect(url_for("companies"))
    
    delete_company(company_id)
    flash("Company Deleted Successfully.")
    return redirect(url_for("companies"))
                
############################################## DEALS ##############################################

@crm_app.route("/dashboard/deals/create", methods=["POST"])
@login_required
def create_deal_route():
        title=request.form.get("title")
        amount=request.form.get("amount")
        stage=request.form.get("stage")
        close_date=request.form.get("expected_close_date")
        contactID=request.form.get("contact_id")
        userID=current_user.id # Use current_user.id for userID
        #userID=request.form.get("user_id")
        
        
        if not title or not amount or not stage or not close_date or not contactID: #or not userID:
            flash("All Fields Are Required..")
            return redirect(url_for("deals"))
        
        try:
            amount = float(amount)
            contactID = int(contactID)
            #userID = int(userID)
        except ValueError:
            flash("Amount must be a number. Contact ID must be an integer.") 
            return redirect(url_for("deals"))
        
        # Validate Foreign Keys
        contact=read_contact_byID(contactID)
        #user=read_user_byID(userID)
        
        if not contact: # or not user:
            flash("Invalid Contact ID.")
            return redirect(url_for("deals"))
        
        create_deal(title,amount,stage,close_date,contactID,userID) # Ensure to use current_user.id for userID
        
        flash("Deal Created Successfully.")
        return redirect(url_for("deals"))
    
@crm_app.route("/dashboard/deals/update", methods=["POST"])
@login_required
def update_deal_route():
    deal_id =request.form.get("deal_id")
    title =request.form.get("title")
    amount =request.form.get("amount")
    stage =request.form.get("stage")
    close_date =request.form.get("expected_close_date")
    contactID =request.form.get("contact_id")
    userID = current_user.id # Use current_user.id for userID
    
    if not deal_id or not title or not amount or not stage or not close_date or not contactID: #or not userID:
        flash("All Fields Are Required..")
        return redirect(url_for("deals"))
    
    try:
        deal_id = int(deal_id)
        amount = float(amount)
        contactID = int(contactID)
        #userID = int(userID)
    except ValueError:
        flash("Deal ID and Contact ID must be integers. Amount must be a number.")
        return redirect(url_for("deals"))
    
     # Validate Foreign Keys
    
    deal = read_deal_byID(deal_id)
    if deal['user_id'] != current_user.id: #UPDATED FOR AUTHORIZATION
        abort(403)  # Forbidden Access
    
    update_deal(title, amount, stage, close_date, contactID, userID, deal_id)
    flash("Deal Updated Successfully.")
    return redirect(url_for("deals"))

@crm_app.route("/dashboard/deals/delete", methods=["POST"])
@login_required
def delete_deal_route():
    deal_id = request.form.get("deal_id")
    
    if not deal_id:
        flash("Deal ID is required.")
        return redirect(url_for("deals"))
    
    try:
        deal_id = int(deal_id)
    except ValueError:
        flash("Deal ID must be a number.")
        return redirect(url_for("deals"))
    
    check_deal=read_deal_byID(deal_id)
    if not check_deal:
        abort(404)  # Deal Not Found
    
    deal = read_deal_userID(deal_id)
    if deal['user_id'] != current_user.id:
        abort(403)  # Forbidden Access
    
    delete_deal(deal_id)
    flash("Deal Deleted Successfully.")
    return redirect(url_for("deals"))    

#################################### Listing (SEARCH) #########################################
# Users
@crm_app.route("/dashboard/users")
@login_required
def users():
    q = request.args.get("q") # search query
    page = int(request.args.get("page", 1)) # pagination default page 1 
    per_page = 5 # records per page
    
    if q:
        Data = general_search("users",q) #general_search(table,query)
    else:
        Data = read_user()
        
    total_pages=(len(Data)+per_page-1)//per_page # TOTAL PAGES
    start=(page-1)*per_page
    end=start+per_page
    Data=Data[start:end]    
           
      
    return render_template("users.html",pagetitle="Users List" ,users = Data, page=page,total_pages=total_pages)     

# Contacts
@crm_app.route("/dashboard/contacts")
@login_required
def contacts():
    q = request.args.get("q")
    page = int(request.args.get("page", 1)) # pagination default page 1 
    per_page = 5 # records per page
    
    if q:
        Data = general_search("contacts",q)
    else:
        Data = read_contact()
    
    total_pages=(len(Data)+per_page-1)//per_page # TOTAL PAGES
    start=(page-1)*per_page
    end=start+per_page
    Data=Data[start:end]
    
    
    return render_template("contacts.html",pagetitle="Contacts List" ,contacts = Data,page=page,total_pages=total_pages)

# Companies
@crm_app.route("/dashboard/companies")
@login_required
def companies():
    q = request.args.get("q")
    page = int(request.args.get("page", 1)) # pagination default page 1 
    per_page = 5 # records per page
    
    if q:
        Data = general_search("companies",q)
    else:
        Data = read_company()
        
    
    total_pages=(len(Data)+per_page-1)//per_page # TOTAL PAGES
    start=(page-1)*per_page
    end=start+per_page
    Data=Data[start:end]
    
    return render_template("companies.html",pagetitle="Comapnies List" ,companies = Data, page=page,total_pages=total_pages)

# deals
@crm_app.route("/dashboard/deals")
@login_required
def deals():
    q = request.args.get("q")
    page = int(request.args.get("page", 1)) # pagination default page 1 
    per_page = 5 # records per page
    
    if q:
        Data = general_search("deals",q)
    else:
        Data = read_deal_userID(current_user.id)
        
    total_pages=(len(Data)+per_page-1)//per_page # TOTAL PAGES
    start=(page-1)*per_page
    end=start+per_page
    Data=Data[start:end]    
    
    return render_template("deals.html",pagetitle="Deals List" ,deals = Data,page=page,total_pages=total_pages)