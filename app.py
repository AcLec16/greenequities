import streamlit as st

st.set_page_config(page_title="ESG Score Application", layout="wide")

# Main app with navigation
st.title("ESG Diagnosis by Green Equities")
st.sidebar.title("Navigation")

# Navigation to pages
menu = st.sidebar.radio("Go to", ["Company Survey", "Employee Survey", "Generate Report"])

if menu == "Company Survey":
    from pages import company_survey
    company_survey.run()
elif menu == "Employee Survey":
    from pages import employee_survey
    employee_survey.run()
elif menu == "Generate Report":
    from pages import generate_report
    generate_report.run()
