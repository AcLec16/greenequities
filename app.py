import streamlit as sl
import math

sl.title("Start ESG Diagnosis - By Green Equities")
sl.write("Let's start")

with sl.form("esg_score_calculator"):
    sl.header("Company Survey")
    
    # Year of Opening Input
    company_name = sl.text_input("Company name")
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
    csr_person = sl.radio("Does the entity have a specified Committee of the Board/Director responsible for corporate responsibility-related activities?", ("Yes", "No"))
    form_filler = sl.text_input("Name of person responsible for filling out this form") 
    website = sl.text_input("Website")
    email_address = sl.text_input("Email address")
    telephone = sl.text_input("Telephone")
    social_media = sl.text_input("Social Media")
    mission_statement = sl.text_area("Mission statement")

    # Financial and Operational Metrics Section
    sl.subheader("Financial and Operational Metrics")
    monthly_water_bill = sl.number_input("What is the monthly Water Bill?", min_value=0.0, step=0.01)
    monthly_electricity_bill = sl.number_input("What is the monthly Electricity bill?", min_value=0.0, step=0.01)
    monthly_profit = sl.number_input("Monthly Profit", min_value=0.0, step=0.01)
    monthly_labor_costs = sl.number_input("Monthly Labor Costs", min_value=0.0, step=0.01)
    monthly_land_costs = sl.number_input("Monthly Land Costs (Rent, Storage facilities, Manufacturing facilities)", min_value=0.0, step=0.01)
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
    green_product_revenue = sl.number_input("Green Product Revenue", min_value=0.0, step=0.01)
    green_energy = sl.number_input("Energy from Sustainable sources (KwH)", min_value=0.0, step=0.01)
    total_energy = sl.number_input("Total Energy Used per month (KwH)", min_value=0.0, step=0.01)
    waste_values = {
        "Plastic": 7,
        "Food Waste": 6, 
        "Electronic Waste (e-waste)": 5, 
        "Fabric Scraps": 4,
        "Damaged or Expired Goods": 3,
        "Scrap Metals": 2,
        "Paper Waste": 1,
    }

    # Streamlit multiselect for selecting primary waste generators
    primary_waste_generator = sl.multiselect(
        "What is your company's primary waste generator:",
        list(waste_values.keys()),
    )
    company_stance_sustainability = sl.text_area("Business’ current stance on environmental sustainability (100 words or less)")
    clean_tech_initiatives = sl.text_area("Company initiatives on clean technology, energy efficiency, renewable energy, etc.")

    # Governance and Policies Section
    sl.subheader("Governance and Policies")
    anti_corruption_policy = sl.selectbox("Does the business have anti-corruption policies?", ("Yes", "No"))
    anti_corruption_policy_link = sl.text_input("Anti-corruption policy link (if available)")
    board_director_responsibility = sl.selectbox("Entity has Board/Director responsible for corporate responsibility activities", ("Yes", "No"))

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
    
    sl.subheader("Management and Structure")
    role_scores = {
        "Chairman": 7,
        "CEO": 6,
        "COO": 5,
        "CFO": 4,
        "General Manager": 3,
        "Department Head": 2,
        "Employee": 1,
        "": 0  # For empty selections
    }

    roles = sl.multiselect(
        "Please list the management structure of your company from the top down by selecting positions from the dropdowns below:",
        [
            "Chairman", "CEO", "COO", "CFO", "General Manager", "Department Head", "Employee"
        ]
    )
    
    sl.subheader("Additional Information")
    current_financial_year_month = sl.text_input("Current financial year and month")
    main_business_activity = sl.text_area("Description of main business activity (product/service)")
    info_flow_time = sl.number_input("Time for information flow to reach required employees (mins)", min_value=0.0, step=0.01)
    sl.write("Rate your current business performance:")
    rating = sl.radio("Select your rating:", options=[1, 2, 3, 4, 5], format_func=lambda x: "⭐" * x)

    if sl.form_submit_button("Submit"):
        # Environmental Calculations
        green_product_revenue_percentage = green_product_revenue / total_monthly_revenue if total_monthly_revenue else 0
        waste_rating = sum([1 / waste_values[waste] * 10 for waste in primary_waste_generator])
        green_energy_score = (green_energy / total_energy) * 10 if total_energy else 0
        annual_electricity_emissions = total_energy * 0.85 * 12
        emissions_rating = 10 - ((annual_electricity_emissions - 871.25 * total_employees) / (403.75 * total_employees)) * 9 if total_employees else 0

        # Social Calculations
        average_culture_satisfaction = (sum(employee_answers_culture) / len(employee_answers_culture) + emp_satisfaction) / 2 if employee_answers_culture else 0
        average_opinion_social = (emp_opinion + emp_social) / 2 if emp_opinion and emp_social else 0
        diversity_index = ((male_employees / total_employees) * 100 + 
                           (female_employees / total_employees) * 100 + 
                           (lgbtq_employees / total_employees) * 100 + 
                           (differently_abled_employees / total_employees) * 100) / 4 if total_employees else 0
        adjusted_score = max(1, min(10, math.ceil((diversity_index / 100) * 9 + 1)))

        # Governance Calculations
        total_score = sum(role_scores[role] for role in roles)
        if 25 <= total_score <= 28:
            sl.write("Hierarchical (Traditional) Structure")
        elif 13 <= total_score <= 24:
            sl.write("Flat (Horizontal) Structure")
        elif 15 <= total_score <= 21 and "Department Head" in roles:
            sl.write("Matrix Structure Score")
        elif 14 <= total_score <= 24 and any(role in roles for role in ["General", "Department Head"]):
            sl.write("Divisional Structure Score")
        else:
            sl.write("Undefined Structure")
        
        sl.write("Thank you for completing the ESG Diagnosis Survey. Your responses have been recorded.")
