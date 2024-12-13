import streamlit as st
# from firebase_config import store_employee_data

def run():
    st.header("Employee Survey Form")
    
    company_code = st.text_input("Enter Company Code")
    
    if company_code:
        st.write(f"Filling form for company: {company_code}")
        employee_answers = {}
        
        for i in range(1, 6):
            employee_answers[f"q{i}"] = st.slider(f"Question {i}", 0, 10, 5)

        if st.button("Submit"):
            # store_employee_data(company_code, employee_answers)
            st.success("Employee survey submitted!")
