import streamlit as st
from firebase_config import store_employee_data, check_company_code

def run():
    st.header("Employee Survey Form")
    
    company_code = st.text_input("Enter Company Code")
    
    if company_code != '' and check_company_code(company_code):
        st.write(f"Filling form for company: {company_code}")
        employee_answers = {}
        
        employee_answers["employee_form_name"] = st.text_input("Name of the employee responsible for filling out this form")
        employee_answers["work_hours_week"] = st.number_input("How many hours do you work on average per week?", min_value=0, step=1)
        employee_answers["company_culture_alignment"] = st.slider("How strongly do you align with your company's culture and values? (Rate from 1 to 10)", 1, 10)
        employee_answers["employer_satisfaction"] = st.slider("How satisfied are you with your current employer? (Rate from 1 to 10)", 1, 10)
        employee_answers["compensation_fairness"] = st.slider("Do you feel you are fairly compensated for the work you do? (Rate from 1 to 10)", 1, 10)
        employee_answers["colleague_respect"] = st.slider("On a scale of 1 to 10, how much do you feel that colleagues respect and value each other’s opinions?", 1, 10)
        employee_answers["health_wellbeing"] = st.slider("How effectively does your workplace support your physical and mental health? (Rate from 1 to 10)", 1, 10)
        employee_answers["inclusion"] = st.slider("On a scale of 1 to 10, how included do you feel in team decision-making discussions and social interactions?", 1, 10)
        employee_answers["informed_by_management"] = st.slider("Do you feel well-informed by colleagues and upper management? (Rate from 1 to 10)", 1, 10)
        employee_answers["work_travel_hours_year"] = st.number_input("How many hours do you travel by air for work annually?", min_value=0, step=1)
        employee_answers["training_opportunities"] = st.slider("Rate the training you receive not only related to your job but also opportunities that enhance your lifestyle, such as financial literacy or well-being courses. (Rate from 1 to 10)", 1, 10)
        employee_answers["information_flow_time"] = st.number_input("On average, how long does it take for information to flow from the receiver to the required employees? (in hours, e.g., 0.5, 1...)", min_value=0, step=1)
        employee_answers["company_tenure"] = st.number_input("How long have you been with the company? (in years)", min_value=0, step=1)
        employee_answers["workplace_rating"] = st.slider("Rate your physical workplace (Rate from 1 to 10), considering seating, lighting, cleanliness, technology, and equipment.", 1, 10)
        employee_answers["executive_tenure"] = st.number_input("How long have you been with the company as an Executive? (in years)", min_value=0, step=1)
        employee_answers["travel_distance_private_car"] = st.number_input("How many kilometers do you travel daily to work using a private car?", min_value=0, step=1)
        employee_answers["Job_related_training"] = st.slider("Rate the job-related training you have received in aspects such as compliance, technical skills, leadership, and career growth. (Rate from 1 to 10)", 1, 10)
        employee_answers["leadership_confidence"] = st.slider("How confident are you in the leadership of the organization? (Rate from 1 to 10)", 1, 10)

    if st.button("Submit"):
            form_valid = True  # Assume everything is filled correctly

            if employee_answers["work_hours_week"] == 0:
                st.error("Please enter the average work hours per week.")
                form_valid = False
            if employee_answers["work_travel_hours_year"] == 0:
                st.error("Please enter your annual work-related air travel hours.")
                form_valid = False
            if employee_answers["information_flow_time"] == 0:
                st.error("Please enter the average time for internal information flow.")
                form_valid = False
            if employee_answers["company_tenure"] == 0:
                st.error("Please enter your total years with the company.")
                form_valid = False
            if employee_answers["executive_tenure"] == 0:
                st.error("Please enter your executive-level tenure (if applicable).")
                form_valid = False
            if employee_answers["travel_distance_private_car"] == 0:
                st.error("Please enter your daily commute distance using a private car.")
                form_valid = False

            # Submit only if all required fields are valid
            if form_valid:
                st.success("All required fields are filled. Submitting employee survey...")
                store_employee_data(company_code, employee_answers)
                st.success("Employee survey submitted!")
            elif company_code != '':
                st.error("Incorrect Company Code")
