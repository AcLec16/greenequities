import streamlit as st
from firebase_config import store_employee_data, check_company_code

def run():
    st.header("Employee Survey Form")
    
    company_code = st.text_input("Enter Company Code")
    
    if company_code != '' and check_company_code(company_code):
        st.write(f"Filling form for company: {company_code}")
        employee_answers = {}
        
        employee_answers["employee_form_name"] = st.text_input("Name of employee responsible for filling out this form")
        employee_answers["work_hours_week"] = st.number_input("How many hours do you work in a week on average?", min_value=0, step=1)
        employee_answers["company_culture_alignment"] = st.slider("How strongly do you align with your company's culture and values? (1-10)", 1, 10)
        employee_answers["employer_satisfaction"] = st.slider("How satisfied are you with your current employer? (1-10)", 1, 10)
        employee_answers["compensation_fairness"] = st.slider("I am fairly compensated for the work I do. (1-10)", 1, 10)
        employee_answers["colleague_respect"] = st.slider("On a scale of 1-10, how much do you feel that colleagues respect and value each other’s opinions?", 1, 10)            
        employee_answers["health_wellbeing"] = st.slider("Do you feel your workplace supports your physical and mental health effectively (1-10)?", 1, 10)
        employee_answers["inclusion"] = st.slider("On a scale of 1-10, how included do you feel in team decision-making discussions and social interactions?", 1, 10)
        employee_answers["informed_by_management"] = st.slider("I feel well informed by colleagues and upper management. (1-10)", 1, 10)
        employee_answers["work_travel_hours_year"] = st.number_input("How many hours do you fly due to work yearly?", min_value=0, step=1)
        employee_answers["training_opportunities"] = st.slider("Rate the training you receive not only related to your job but opportunities that enhance your lifestyle, such as financial literacy or wellbeing courses. (1-10)", 1, 10)
        employee_answers["information_flow_time"] = st.number_input("On average, how long does it take for information to flow from the receiver to the required employees? (hours, ie. 0.5, 1...)", min_value=0, step=1)
        employee_answers["company_tenure"] = st.number_input("How long have you been in the company? (in years)", min_value=0, step=1)
        employee_answers["workplace_rating"] = st.slider("Rate your physical workplace (1-10), considering seating, lighting, cleanliness, technology, and equipment.", 1, 10)
        employee_answers["executive_tenure"] = st.number_input("How long have you been in the company (as an Executive)? (in years)", min_value=0, step=1)
        employee_answers["travel_distance_private_car"] = st.number_input("How many kilometers do you spend traveling via private car per day to work?", min_value=0, step=1)
        employee_answers["Job_related_training"] = st.slider("Now rate the job-related training you’ve received in aspects such as, compliance, technical skills, leadership, and career growth")
        if st.button("Submit"):
            store_employee_data(company_code, employee_answers)
            st.success("Employee survey submitted!")

    elif company_code != '':
        st.error("Incorrect Company Code")
