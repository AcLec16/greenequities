import streamlit as st
from firebase_config import get_company_data, get_employee_data, check_company_code, get_employee_count
from esg_algorithm import calculate_esg_score
from fpdf import FPDF
import os

# # Custom PDF class for generating reports
# class PDF(FPDF):
#     def header(self):
#         self.set_font('Arial', 'B', 16)
#         self.set_text_color(0, 102, 204)
#         self.cell(0, 10, 'ESG Report', 0, 1, 'C')
#         self.ln(10)

#     def footer(self):
#         self.set_y(-15)
#         self.set_font('Arial', 'I', 8)
#         self.set_text_color(128)
#         self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

#     def add_section_title(self, title):
#         self.set_font('Arial', 'B', 14)
#         self.set_text_color(0, 0, 0)
#         self.cell(0, 10, title, 0, 1, 'L')
#         self.ln(5)

#     def add_text(self, label, value):
#         self.set_font('Arial', '', 12)
#         self.cell(50, 10, f'{label}:', 0, 0, 'L')
#         self.set_text_color(0, 102, 204)
#         self.cell(0, 10, f'{value}', 0, 1, 'L')
#         self.set_text_color(0, 0, 0)
#         self.ln(3)

#     def add_box(self, title, value):
#         self.set_font('Arial', '', 12)
#         self.set_fill_color(240, 240, 240)
#         self.cell(0, 10, f'{title}: {value}', 0, 1, 'L', fill=True)
#         self.ln(5)

# # Function to generate the PDF report
# def generate_pdf(report):
#     pdf = PDF()
#     pdf.add_page()

#     # Company Details
#     pdf.add_section_title("Company Details")
#     pdf.add_text("Company Name", report["company_name"])
#     pdf.add_text("Financial Year (Month)", report["current_financial_year_month"])
#     pdf.add_text("Main Business Activity", report["main_business_activity"])
#     pdf.add_text("Website", report["website"])
#     pdf.add_text("Email Address", report["email_address"])
#     pdf.add_text("Telephone", report["telephone"])
#     pdf.add_text("Social Media", report["social_media"])
#     pdf.add_text("Mission Statement", report["mission_statement"])
#     pdf.add_text("Year of Opening", report["year_of_opening"])
#     pdf.add_text("Selected Locations", ", ".join(report["selected_locations"]))

#     # Add additional sections for other report details
#     pdf.add_section_title("ESG Analysis")
#     for key, value in report.items():
#         if key not in [
#             "company_name",
#             "current_financial_year_month",
#             "main_business_activity",
#             "website",
#             "email_address",
#             "telephone",
#             "social_media",
#             "mission_statement",
#             "year_of_opening",
#             "selected_locations",
#         ]:
#             pdf.add_box(key.replace("_", " ").capitalize(), value)

#     # Save the PDF
#     pdf_file = "ESG_Report.pdf"
#     pdf.output(pdf_file)
#     return pdf_file

# Streamlit App
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
                st.write("**ESG Report Data**")
                st.json(report)

                # Generate and display PDF
                pdf_file = generate_pdf(report)
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