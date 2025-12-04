from .db import get_connection # get_connection to work on the DB conn
from datetime import datetime

# User Table CRUD 
# CREATE
def create_user(username,email,hashed_pass):  
    conn=get_connection()
    cursor=conn.cursor()
    created_at=datetime.now()
    cursor.execute("""INSERT INTO users (username,email,hashed_pass,created_at) VALUES (?,?,?,?)""",
                                (username,email,hashed_pass,created_at))
    conn.commit()
    user_ID=cursor.lastrowid
    conn.close()
    
    return user_ID # Return User ID

# READ    
def read_user():  
    conn=get_connection()
    cursor=conn.cursor()
    Data=cursor.execute("""SELECT * FROM users""").fetchall() 
    conn.close()
    
    return Data

# READ BY ID
def read_user_byID(user_ID):
    conn=get_connection()
    cursor=conn.cursor()
    Data=cursor.execute("""SELECT * FROM users WHERE ID=?""",(user_ID)).fetchone()
    conn.close()
    
    return Data
    
# UPDATE
def update_user(user_ID,username,email):  
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""UPDATE users SET username = ?, email = ? WHERE ID = ?""",(
                                            username,email,user_ID))
    conn.commit()
    conn.close()
    
    return True
    
# DELETE    
def delete_user(user_ID):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""DELETE FROM users WHERE ID = ?""",(user_ID))
    conn.commit()
    conn.close()
    
    return True  
    
#################################################################################################################################################################################

# Company Table CRUD
# CREATE
def create_company(name,industry,address):  
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""INSERT INTO companies (name,industry,address) VALUES (?,?,?)""",
                                             (name,industry,address))
    conn.commit()
    company_ID=cursor.lastrowid
    conn.close()
    
    return company_ID
 
# READ    
def read_company():  
    conn=get_connection()
    cursor=conn.cursor()
    Data=cursor.execute("""SELECT * FROM companies""").fetchall() 
    conn.close()
    
    return Data

# READ BY ID
def read_company_byID(company_ID):
    conn=get_connection()
    cursor=conn.cursor()
    Data=cursor.execute("""SELECT * FROM companies WHERE ID=?""",(company_ID)).fetchone()
    conn.close()
    
    return Data

# UPDATE
def update_company(name,industry,address,company_ID):  
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""UPDATE companies SET name = ?, industry = ?, address = ? WHERE ID = ?""",
                                                    (name,industry,address,company_ID))
    conn.commit()
    conn.close()
    
    return True

# DELETE
def delete_company(company_ID):  
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""DELETE FROM companies WHERE ID = ?""",(company_ID))
    conn.commit()
    conn.close()
    
    return True

#################################################################################################################################################################################

# Contact Table CRUD
# CREATE
def create_contact(name,phone,email,company_id,notes):  
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""INSERT INTO contacts (name,phone,email,company_id,notes) VALUES (?,?,?,?,?)""",
                                            (name,phone,email,company_id,notes))
    conn.commit()
    contact_ID=cursor.lastrowid
    conn.close()
    
    return contact_ID

# READ
def read_contact():  
    conn=get_connection()
    cursor=conn.cursor()
    Data=cursor.execute("""SELECT * FROM contacts""").fetchall() 
    conn.close()
    
    return Data

# READ BY ID
def read_contact_byID(contact_ID):
    conn=get_connection()
    cursor=conn.cursor()
    Data=cursor.execute("""SELECT * FROM contacts WHERE ID=?""",(contact_ID)).fetchone()
    conn.close()
    
    return Data

# UPDATE
def update_contact(name,phone,email,company_id,notes,contact_ID):  
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""UPDATE contacts 
                   SET name = ?, phone = ?, email = ?, company_id = ?, notes = ? 
                   WHERE ID = ?
                   """,     (name,phone,email,company_id,notes,contact_ID))
    conn.commit()
    conn.close()
    
    return True

# DELETE
def delete_contact(contact_ID):  
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""DELETE FROM contacts WHERE ID = ?""",(contact_ID))
    conn.commit()
    conn.close()
    
    return True
#################################################################################################################################################################################

# Deal Table CRUD
# CREATE
def create_deal(title,amount,stage,expected_close_date,contact_id,user_id):    
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""INSERT INTO deals (title,amount,stage,expected_close_date,contact_id,user_id) 
                   VALUES (?,?,?,?,?,?)""",(title,amount,stage,expected_close_date,contact_id,user_id))
    conn.commit()
    deal_ID=cursor.lastrowid
    conn.close()
    
    return deal_ID 

# READ
def read_deal():  
    conn=get_connection()
    cursor=conn.cursor()
    Data=cursor.execute("""SELECT * FROM deals""").fetchall() 
    conn.close()
    
    return Data

# READ BY ID
def read_deal_byID(deal_ID):
    conn=get_connection()
    cursor=conn.cursor()
    Data=cursor.execute("""SELECT * FROM deals WHERE ID=?""",(deal_ID)).fetchone()
    conn.close()
    
    return Data

# UPDATE
def update_deal(title,amount,stage,expected_close_date,contact_id,user_id,deal_ID):  
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""UPDATE deals 
                   SET title = ?, amount = ?, stage = ?, expected_close_date = ?, 
                   contact_id = ?, user_id = ?
                   WHERE ID = ?
                   """,     (title,amount,stage,expected_close_date,contact_id,user_id,deal_ID))
    conn.commit()
    conn.close()
    
    return True

# DELETE
def delete_deal(deal_ID):  
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""DELETE FROM contacts WHERE ID = ?""",(deal_ID))
    conn.commit()
    conn.close()
    
    return True

