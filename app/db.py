import sqlite3
import os

def get_connection():
    conn=sqlite3.connect('crm.db')
    conn.row_factory=sqlite3.Row # to return the rows as a dictionary 
    
    return conn


def init_db():
    # Initialize DB using schema.sql if crm.db NOT FOUND
    if not os.path.exists('crm.db'):
        conn=get_connection()
        
        with open("config/schema.sql","r") as Schema:
            conn.executescript(Schema.read())
        
        conn.commit()
        conn.close()    
        print("Database Created Successfully")
    else:
        print("Database Already Exists")    
        


"""conn = get_connection()
cursor = conn.cursor()

audit_columns = [
        ('companies', 'created_at', 'TEXT'),
        ('companies', 'updated_at', 'TEXT'),
        ('companies', 'created_by', 'INTEGER'),
        ('companies', 'updated_by', 'INTEGER'),
        ('contacts', 'created_at', 'TEXT'),
        ('contacts', 'updated_at', 'TEXT'),
        ('contacts', 'created_by', 'INTEGER'),
        ('contacts', 'updated_by', 'INTEGER'),
        ('deals', 'created_at', 'TEXT'),
        ('deals', 'updated_at', 'TEXT'),
        ('deals', 'created_by', 'INTEGER'),
        ('deals', 'updated_by', 'INTEGER')
    ]

for table, col, col_type in audit_columns:
        try:
            cursor.execute(f"ALTER TABLE {table} ADD COLUMN {col} {col_type}")
        except Exception:
            pass

conn.commit()
conn.close()
print("Schema updated successfully without dropping tables")"""        
        
print("DONE")        
        





































'''
cursor = conn.cursor() # Cursor for implementing anything
cursor.execute() # Commands 
cursor.executemany("INSERT INTO users VALUES (?,?,?)") # ? are placeholders
conn.commit() # Commit ur commands 
conn.close() # Close Connection
cursor.fetchone() # fetch one record
cursor.fetchall() # fetch all records
cursor.fetchmany() # fetch a certain no. of records taken as a parameter
print(cursor.fetchall()) # to print the records 
'''
