from google.cloud import firestore
from google.oauth2 import service_account
import streamlit as st
import json

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="green-equities")

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

def check_company_code(company_code):
    if not company_code or company_code.strip() == "":
        raise ValueError("Company code cannot be empty.")
    
    doc_ref = db.collection("companies").document(company_code)
    return doc_ref.get().exists