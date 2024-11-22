import streamlit as sl

sl.title("Start ESG Diagnosis - By Green Equities")
sl.write("Let's start")

with sl.form("esg_score_calculator"):
    sl.header("Company Survey")
    
    # Year of Opening Input
    year_of_opening = sl.number_input("Year of Opening", min_value=1900, max_value=2100, step=1)
    
    # Location Values
    location_values = {
        "Worli": 4.3,
        "Malabar & Cumballa Hill": 4.5,
        "Juhu": 4.4,
        "Bandra Kurla Complex": 4.2,
        "Nariman Point": 4.8,
        "Andheri": 4.4,
        "Lower Parel": 4.3,
        "Parel": 4.5,
        "Bandra": 4.9,
        "Santacruz": 4.2,
        "Ghatkopar": 4.0,
        "Thane": 4.3,
        "Goregaon": 4.3,
        "Byculla": 4.1,
        "Fort": 4.3,
        "Borivali": 5.0,
        "Jogeshwari": 4.2,
        "Khar": 4.2,
        "Malad": 4.2,
        "Vile Parle": 4.4,
        "Chembur": 4.3,
        "Dharavi": 3.4,
        "Colaba": 1.0,
        "Dadar": 4.4
    }
    
    # Multi-select for Office Locations
    selected_locations = sl.multiselect(
        "Select Office Location:",
        list(location_values.keys()),
        help="Choose one or more office locations to calculate associated values."
    )
    
    # Industry Multi-select
    industry = sl.multiselect(
        "Select Industry:",
        [
            "Financial Services", "FMCG", "Healthcare", "IT", "Media",
            "Metal", "Pharma", "Realty", "Consumer Durables", 
            "Oil and Gas", "Other"
        ]
    )
    
    # Other Company Information
    website = sl.text_input("Website")
    email_address = sl.text_input("Email address")
    telephone = sl.text_input("Telephone")
    social_media = sl.text_input("Social Media")
    mission_statement = sl.text_area("Mission statement and future goals")

    # Financial and Operational Metrics Section
    sl.subheader("Financial and Operational Metrics")
    monthly_water_bill = sl.number_input("What is the monthly Water Bill?", min_value=0.0, step=0.01)
    monthly_electricity_bill = sl.number_input("What is the monthly Electricity bill?", min_value=0.0, step=0.01)
    monthly_profit = sl.number_input("Monthly Profit", min_value=0.0, step=0.01)
    monthly_labor_costs = sl.number_input("Monthly Labor Costs", min_value=0.0, step=0.01)
    monthly_land_costs = sl.number_input("Monthly Land Costs (Rent, Storage facilities, Manufacturing facilities", min_value=0.0, step=0.01)
    monthly_raw_material_costs = sl.number_input("Monthly costs of acquiring new raw material (if applicable)", min_value=0.0, step=0.01)
    total_monthly_revenue = sl.number_input("Total Monthly Revenue", min_value=0.0, step=0.01)

    # Employee Information Section
    sl.subheader("Employee Information")
    total_employees = sl.number_input("Total number of Employees", min_value=0, step=1)
    male_employees = sl.number_input("Number of Male Employees", min_value=0, step=1)
    female_employees = sl.number_input("Number of Female employees", min_value=0, step=1)
    lgbtq_employees = sl.number_input("Number of LGBTQ+ Employees", min_value=0, step=1)
    differently_abled_workers = sl.number_input("Differently abled workers", min_value=0, step=1)
    employee_separations = sl.number_input("Number of employee separations over the past 2 years?", min_value=0, step=1)
    customer_feedback_score = sl.slider("Customer feedback score (using company feedback system or Google Business rating)", min_value=0, max_value=5, step=1)

    # Supplier Information Section
    sl.subheader("Supplier Information")
    all_time_suppliers = sl.number_input("How many all-time suppliers have you had?", min_value=0, step=1)
    remaining_suppliers = sl.number_input("What is the Number of remaining suppliers?", min_value=0, step=1)

    # Environmental and Energy Metrics Section
    sl.subheader("Environmental and Energy Metrics")
    carbon_credits_bought = sl.number_input("Carbon credits bought (Co2 emissions)", min_value=0.0, step=0.01)
    energy_sustainable_sources = sl.number_input("Energy from Sustainable sources (KwH)", min_value=0.0, step=0.01)
    total_energy_used = sl.number_input("Total Energy Used per month (KwH)", min_value=0.0, step=0.01)
    primary_waste_generator = sl.text_input("Primary Waste generator")
    company_stance_sustainability = sl.text_area("Business’ current stance on environmental sustainability (100 words or less)")
    clean_tech_initiatives = sl.text_area("Company initiatives on clean technology, energy efficiency, renewable energy, etc.")

    # Governance and Policies Section
    sl.subheader("Governance and Policies")
    anti_corruption_policy = sl.selectbox("Does the business have anti-corruption policies?", ("Yes", "No"))
    anti_corruption_policy_link = sl.text_input("Anti-corruption policy link (if available)")
    board_director_responsibility = sl.selectbox("Entity has Board/Director responsible for corporate responsibility activities", ("Yes", "No"))
    corporate_responsibility_involvement = sl.text_input("Name of person responsible for filling out this form")

    # Social and Community Engagement Section
    sl.subheader("Social and Community Engagement")
    human_rights_ngo = sl.text_area("Does the company on human rights extend to any NGOs/Others? If yes, list")
    social_impact_partnerships = sl.text_area("Has your organization partnered with Social impact organizations, NGOs, or charities?")
    compliance_certifications = sl.text_area("List any Compliance certifications received by the business")
    awards_received = sl.file_uploader("List any Awards received by the business, upload pictures", type=["jpg", "jpeg", "png", "pdf"])
    selected_sdgs = sl.multiselect("Choose 3 SDGs that relate best to your organization", [
        "No Poverty", "Zero Hunger", "Good Health and Well-Being", "Quality Education",
        "Gender Equality", "Clean Water and Sanitation", "Affordable and Clean Energy",
        "Decent Work and Economic Growth", "Industry, Innovation and Infrastructure",
        "Reduced Inequality", "Sustainable Cities and Communities",
        "Responsible Consumption and Production", "Climate Action",
        "Life Below Water", "Life on Land", "Peace, Justice, and Strong Institutions",
        "Partnerships for the Goals"
    ])

    # Management and Structure Section
    sl.subheader("Management and Structure")
    management_structure = sl.text_area("List management structure from the top down")
    number_of_executives = sl.number_input("Number of Executives/managers in the company", min_value=0, step=1)

    # Additional Information Section
    sl.subheader("Additional Information")
    current_financial_year_month = sl.text_input("Current financial year and month")
    main_business_activity = sl.text_area("Description of main business activity (product/service)")
    green_product_revenue = sl.number_input("Green Product Revenue", min_value=0.0, step=0.01)
    info_flow_time = sl.number_input("Time for information flow to reach required employees", min_value=0.0, step=0.01)

    sl.divider()
    sl.header("Employee Survey")
    work_hours_week = sl.number_input("How many hours do you work in a week on average?", min_value=0, step=1)
    company_culture_alignment = sl.slider("How strongly do you align with your company's culture and values? (1-10)", 1, 10)
    break_length = sl.number_input("How long is the break you receive per day? (in hours)", min_value=0.0, step=0.5)
    employer_satisfaction = sl.slider("How satisfied are you with your current employer? (1-10)", 1, 10)
    compensation_fairness = sl.slider("I am fairly compensated for the work I do. (1-10)", 1, 10)
    colleague_respect = sl.slider("On a scale of 1-10, how much do you feel that colleagues respect and value each other’s opinions?", 1, 10)
    mental_wellbeing = sl.slider("I have good mental wellbeing at work. (1-10)", 1, 10)
    inclusion = sl.slider("On a scale of 1-10, how included do you feel in team decision-making discussions and social interactions?", 1, 10)
    informed_by_management = sl.slider("I feel well informed by colleagues and upper management. (1-10)", 1, 10)
    work_travel_hours_year = sl.number_input("How many hours do you fly due to work yearly?", min_value=0, step=1)
    training_opportunities = sl.slider("I receive training not only related to my job but opportunities that enhance my lifestyle, such as financial literacy or wellbeing courses. (1-10)", 1, 10)
    work_hours_day = sl.number_input("How many hours do you work per day on average?", min_value=0, step=1)
    information_flow_time = sl.number_input("On average, how long does it take for information to flow from the receiver to the required employees? (in hours)", min_value=0, step=1)
    company_tenure = sl.number_input("How long have you been in the company? (in years)", min_value=0, step=1)
    workplace_rating = sl.slider("Rate your physical workplace (1-10), considering seating, lighting, cleanliness, technology, and equipment.", 1, 10)
    executive_tenure = sl.number_input("How long have you been in the company (as an Executive)? (in years)", min_value=0, step=1)
    travel_distance_private_car = sl.number_input("How many kilometers do you spend traveling via private car per day to work?", min_value=0, step=1)    # Submit Button
    if sl.form_submit_button("Submit"):
        
        sl.write("Thank you for completing the ESG Diagnosis Survey. Your responses have been recorded.")
