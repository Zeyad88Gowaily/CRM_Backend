CREATE TABLE users(
    id INTEGER PRIMARY KEY ,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    hashed_pass TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE companies(
    id INTEGER PRIMARY KEY,
    [name] TEXT NOT NULL,
    industry TEXT ,
    [address] TEXT
);

CREATE TABLE contacts(
    id INTEGER PRIMARY KEY,
    [name] TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    company_id INTEGER,
    notes TEXT,

    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE deals(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    amount REAL,
    stage TEXT,
    expected_close_date TEXT,
    contact_id INTEGER,
    user_id INTEGER,

    FOREIGN KEY (contact_id) REFERENCES contacts(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
    
);


"""ALTER TABLE deals ADD COLUMN created_at TEXT;
ALTER TABLE deals ADD COLUMN updated_at TEXT;
ALTER TABLE deals ADD COLUMN created_by INTEGER;
ALTER TABLE deals ADD COLUMN updated_by INTEGER;

ALTER TABLE contacts ADD COLUMN created_at TEXT;
ALTER TABLE contacts ADD COLUMN updated_at TEXT;
ALTER TABLE contacts ADD COLUMN created_by INTEGER;
ALTER TABLE contacts ADD COLUMN updated_by INTEGER;

ALTER TABLE companies ADD COLUMN created_at TEXT;
ALTER TABLE companies ADD COLUMN updated_at TEXT;
ALTER TABLE companies ADD COLUMN created_by INTEGER;
ALTER TABLE companies ADD COLUMN updated_by INTEGER;"""