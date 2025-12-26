# app/audit.py


from models import add_audit_columns

if __name__ == "__main__":
    print("Running audit column migration...")
    add_audit_columns()
