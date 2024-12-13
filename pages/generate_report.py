import streamlit as st
# from firebase_config import get_company_data, get_employee_data
from esg_algorithm import calculate_esg_score

def run():
    st.header("Generate ESG Report")
    
    company_code = st.text_input("Enter Company Code")
    
    if st.button("Generate Report"):
        # company_data = get_company_data(company_code)
        # employee_data = get_employee_data(company_code)
        
        if not company_data or not employee_data:
            st.error("Invalid company code or no data found!")
        else:
            report = calculate_esg_score(company_data["answers"], employee_data)
            st.write("**ESG Report**")
            st.json(report)
