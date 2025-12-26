import requests
from bs4 import BeautifulSoup
import sys

BASE = "http://127.0.0.1:5000"

USERNAME = "Zeyad"
PASSWORD = "Gowaily@1378"

SQLI_PAYLOADS = [
    "' OR 1=1 --",
    "'; DROP TABLE users; --",
    '" OR "1"="1',
    "' UNION SELECT NULL,NULL,NULL --",
]

def fail(msg):
    print(f"[FAIL] {msg}")
    sys.exit(1)

def ok(msg):
    print(f"[OK] {msg}")

session = requests.Session()


# 1. Access protected route WITHOUT login
r = session.get(f"{BASE}/dashboard", allow_redirects=False)
if r.status_code not in (302, 401):
    fail("Protected route accessible without login")
ok("Protected route blocked for unauthenticated users")


# 2. GET login page and extract CSRF
r = session.get(f"{BASE}/login")
if r.status_code != 200:
    fail("Login page not accessible")

soup = BeautifulSoup(r.text, "html.parser")
csrf_input = soup.find("input", {"name": "csrf_token"})
if not csrf_input:
    fail("CSRF token missing on login form")

csrf = csrf_input["value"]
ok("CSRF token found on login form")


# 3. Login WITHOUT CSRF (should fail)
r = session.post(
    f"{BASE}/login",
    data={"username": USERNAME, "password": PASSWORD},
    allow_redirects=False
)

if r.status_code == 200:
    fail("Login succeeded without CSRF")
ok("Login blocked without CSRF")


# 4. Login WITH CSRF
r = session.post(
    f"{BASE}/login",
    data={
        "username": USERNAME,
        "password": PASSWORD,
        "csrf_token": csrf
    },
    allow_redirects=False
)

if r.status_code not in (302, 303):
    fail("Login failed with valid CSRF")
ok("Login successful with CSRF")


# 5. Access protected route AFTER login
r = session.get(f"{BASE}/dashboard")
if r.status_code != 200:
    fail("Protected route blocked after login")
ok("Protected route accessible after login")


# 6. CSRF enforcement on POST action
r = session.post(
    f"{BASE}/dashboard/deals/delete",
    data={"deal_id": "1"},
    allow_redirects=False
)

if r.status_code != 400:
    fail("POST succeeded without CSRF")
ok("CSRF blocks forged POST request")


# 7. SQL Injection tests (authenticated + CSRF)
r = session.get(f"{BASE}/dashboard/deals")
soup = BeautifulSoup(r.text, "html.parser")
csrf = soup.find("input", {"name": "csrf_token"})["value"]

for payload in SQLI_PAYLOADS:
    r = session.post(
        f"{BASE}/dashboard/deals",
        data={
            "title": payload,
            "amount": "100",
            "stage": "open",
            "expected_close_date": "2025-01-01",
            "contact_id": "1",
            "csrf_token": csrf
        }
    )

    if r.status_code == 500:
        fail(f"500 error on SQL payload: {payload}")

    if "sqlite" in r.text.lower() or "syntax error" in r.text.lower():
        fail(f"SQL error leaked for payload: {payload}")

ok("SQL injection payloads handled safely")


# 8. Method enforcement
r = session.get(f"{BASE}/dashboard/deals/delete")
if r.status_code != 405:
    fail("GET allowed on POST-only route")
ok("HTTP method restrictions enforced")

print("\nALL SYSTEM TESTS PASSED")
