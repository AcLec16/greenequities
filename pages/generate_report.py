import streamlit as st
from firebase_config import get_company_data, get_employee_data, check_company_code, get_employee_count
from esg_algorithm import calculate_esg_score

def run():
    st.header("Generate ESG Report")
    
    company_code = st.text_input("Enter Company Code")

    if company_code != '' and check_company_code(company_code):
        num_emp = get_employee_count(company_code)
        if num_emp > 1:
            if st.button("Generate Report"):
                company_data = get_company_data(company_code)
                employee_data = get_employee_data(company_code)
                
                report = calculate_esg_score(company_data, employee_data)
                st.write("**ESG Report**")
                st.json(report)

        else:
            st.error(f"Not enough employees filled the survey! Number of Employees Filled: {num_emp}")
    
    elif company_code != '':
        st.error("Incorrect Company Code")
