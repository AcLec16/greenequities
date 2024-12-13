import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("path/to/your/firebase/credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Functions to interact with Firebase
def store_company_data(company_code, company_data):
    db.collection("companies").document(company_code).set(company_data)

def store_employee_data(company_code, employee_data):
    db.collection("companies").document(company_code).collection("employees").add(employee_data)

def get_company_data(company_code):
    return db.collection("companies").document(company_code).get().to_dict()

def get_employee_data(company_code):
    employees = db.collection("companies").document(company_code).collection("employees").stream()
    return [emp.to_dict() for emp in employees]
