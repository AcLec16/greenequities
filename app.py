import streamlit as sl

sl.title("Start ESG Diagnosis - By Green Equities")
sl.write(
    "Let's start"
)
with sl.form("esg score calculator"):
    sl.subheader("Company survey")
    year_of_opening = sl.number_input("Year of Opening", min_value=1900, max_value=2100, step=1)
    office_address = sl.text_area("Office Address")
    industry = sl.text_input("Industry")
    website = sl.text_input("Website")
    email_address = sl.text_input("Email address")
    telephone = sl.text_input("Telephone")
    social_media = sl.text_input("Social Media")
    mission_statement = sl.text_area("Mission statement and future goals")

    # Financial and Operational Metrics Section
    sl.header("Financial and Operational Metrics")
    monthly_water_bill = sl.number_input("What is the monthly Water Bill?", min_value=0.0, step=0.01)
    monthly_electricity_bill = sl.number_input("What is the monthly Electricity bill?", min_value=0.0, step=0.01)
    monthly_profit = sl.number_input("Monthly Profit", min_value=0.0, step=0.01)
    monthly_labor_costs = sl.number_input("Monthly Labor Costs", min_value=0.0, step=0.01)
    monthly_raw_material_costs = sl.number_input("Monthly costs of acquiring new raw material (if applicable)", min_value=0.0, step=0.01)
    total_monthly_revenue = sl.number_input("Total Monthly Revenue", min_value=0.0, step=0.01)

    # Employee Information Section
    sl.header("Employee Information")
    total_employees = sl.number_input("Total number of Employees", min_value=0, step=1)
    male_employees = sl.number_input("Number of Male Employees", min_value=0, step=1)
    female_employees = sl.number_input("Number of Female employees", min_value=0, step=1)
    lgbtq_employees = sl.number_input("Number of LGBTQ+ Employees", min_value=0, step=1)
    differently_abled_workers = sl.number_input("Differently abled workers", min_value=0, step=1)
    employee_separations = sl.number_input("Number of employee separations over the past 2 years?", min_value=0, step=1)
    customer_feedback_score = sl.slider("Customer feedback score (using company feedback system or Google Business rating)", min_value=0, max_value=5, step=1)

    # Supplier Information Section
    sl.header("Supplier Information")
    all_time_suppliers = sl.number_input("How many all-time suppliers have you had?", min_value=0, step=1)
    remaining_suppliers = sl.number_input("What is the Number of remaining suppliers?", min_value=0, step=1)

    # Environmental and Energy Metrics Section
    sl.header("Environmental and Energy Metrics")
    carbon_credits_bought = sl.number_input("Carbon credits bought (Co2 emissions)", min_value=0.0, step=0.01)
    energy_sustainable_sources = sl.number_input("Energy from Sustainable sources (KwH)", min_value=0.0, step=0.01)
    total_energy_used = sl.number_input("Total Energy Used per month (KwH)", min_value=0.0, step=0.01)
    primary_waste_generator = sl.text_input("Primary Waste generator")
    company_stance_sustainability = sl.text_area("Business’ current stance on environmental sustainability (100 words or less)")
    clean_tech_initiatives = sl.text_area("Company initiatives on clean technology, energy efficiency, renewable energy, etc.")

    # Governance and Policies Section
    sl.header("Governance and Policies")
    anti_corruption_policy = sl.selectbox("Does the business have anti-corruption policies?", ("Yes", "No"))
    anti_corruption_policy_link = sl.text_input("Anti-corruption policy link (if available)")
    board_director_responsibility = sl.selectbox("Entity has Board/Director responsible for corporate responsibility activities", ("Yes", "No"))
    corporate_responsibility_involvement = sl.text_input("Name of person responsible for filling out this form")

    # Social and Community Engagement Section
    sl.header("Social and Community Engagement")
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
    sl.header("Management and Structure")
    management_structure = sl.text_area("List management structure from the top down")
    number_of_executives = sl.number_input("Number of Executives/managers in the company", min_value=0, step=1)

    # Additional Information Section
    sl.header("Additional Information")
    current_financial_year_month = sl.text_input("Current financial year and month")
    main_business_activity = sl.text_area("Description of main business activity (product/service)")
    green_product_revenue = sl.number_input("Green Product Revenue", min_value=0.0, step=0.01)
    info_flow_time = sl.number_input("Time for information flow to reach required employees", min_value=0.0, step=0.01)

    # Submit Button
    if sl.form_submit_button("Submit"):
        
        sl.write("Thank you for completing the ESG Diagnosis Survey. Your responses have been recorded.")
