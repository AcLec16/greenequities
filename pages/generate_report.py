import streamlit as st
from firebase_config import get_company_data, get_employee_data, check_company_code, get_employee_count
from esg_algorithm import calculate_esg_score
from pdf_test import generate_pdf
from AIpowered_ESG import get_esg_ai_recommendations
import json

# Streamlit App
def run():
    st.header("Generate ESG Report")
    
    company_code = st.text_input("Enter Company Code")

    if company_code != '' and check_company_code(company_code):
        num_emp = get_employee_count(company_code)
        if num_emp > 1:
            if st.button("Generate Report"):
                with st.spinner("Getting Data"):
                    company_data = get_company_data(company_code)
                    employee_data = get_employee_data(company_code)
                with st.spinner("Generating PDF"):
                    report = calculate_esg_score(company_data, employee_data)
                suggestion = get_esg_ai_recommendations(report)
                # st.subheader("ESG AI Report")
                st.write(suggestion)
                suggestion = json.loads(suggestion)
                # Generate and display PDF
                with st.spinner("Generating Report"):
                    pdf_file = generate_pdf(report,suggestion)
                with open(pdf_file, "rb") as pdf:
                    st.download_button(
                        label="Download ESG Report as PDF",
                        data=pdf,
                        file_name=pdf_file,
                        mime="application/pdf"
                    )
        else:
            st.error(f"Not enough employees filled the survey! Number of Employees Filled: {num_emp}")
    elif company_code != '':
        st.error("Incorrect Company Code")

# Run the app
if __name__ == "__main__":
    run()
