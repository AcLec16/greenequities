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
        help ="Choose one or more office locations to calculate associated values."
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
    form_filler = website = sl.text_input("Name of person responsible for filling out this form") 
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
    # Role-to-score mapping
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

    # Dropdown menus for roles
    roles = sl.multiselect(
        "Please list the management structure of your company from the top down by selecting positions from the dropdowns below:",
        [
            "Chairman", "CEO", "COO", "CFO", "General Manager", "Department Head", "Employee"
        ]
    )
    

    # Additional Information Section
    sl.subheader("Additional Information")
    current_financial_year_month = sl.text_input("Current financial year and month")
    main_business_activity = sl.text_area("Description of main business activity (product/service)")
    green_product_revenue = sl.number_input("Green Product Revenue", min_value=0.0, step=0.01)
    info_flow_time = sl.number_input("Time for information flow to reach required employees", min_value=0.0, step=0.01)
    sl.write("Rate your current business performance:")
    rating = sl.radio("Select your rating:", options=[1, 2, 3, 4, 5], format_func=lambda x: "⭐" * x)
    

    sl.divider()
    sl.header("Employee Survey")
    employee_form_name = sl.text_input("Name of employee responsible for filling out this form")
    work_hours_week = sl.number_input("How many hours do you work in a week on average?", min_value=0, step=1)
    company_culture_alignment = sl.slider("How strongly do you align with your company's culture and values? (1-10)", 1, 10)
    employer_satisfaction = sl.slider("How satisfied are you with your current employer? (1-10)", 1, 10)
    compensation_fairness = sl.slider("I am fairly compensated for the work I do. (1-10)", 1, 10)
    colleague_respect = sl.slider("On a scale of 1-10, how much do you feel that colleagues respect and value each other’s opinions?", 1, 10)
    mental_wellbeing = sl.slider("I have good mental wellbeing at work. (1-10)", 1, 10)
    inclusion = sl.slider("On a scale of 1-10, how included do you feel in team decision-making discussions and social interactions?", 1, 10)
    informed_by_management = sl.slider("I feel well informed by colleagues and upper management. (1-10)", 1, 10)
    work_travel_hours_year = sl.number_input("How many hours do you fly due to work yearly?", min_value=0, step=1)
    training_opportunities = sl.slider("Rate the training you receive not only related to your job but opportunities that enhance your lifestyle, such as financial literacy or wellbeing courses. (1-10)", 1, 10)
    work_hours_day = sl.number_input("How many hours do you work per day on average?", min_value=0, step=1)
    information_flow_time = sl.number_input("On average, how long does it take for information to flow from the receiver to the required employees? (in hours)", min_value=0, step=1)
    company_tenure = sl.number_input("How long have you been in the company? (in years)", min_value=0, step=1)
    workplace_rating = sl.slider("Rate your physical workplace (1-10), considering seating, lighting, cleanliness, technology, and equipment.", 1, 10)
    executive_tenure = sl.number_input("How long have you been in the company (as an Executive)? (in years)", min_value=0, step=1)
    travel_distance_private_car = sl.number_input("How many kilometers do you spend traveling via private car per day to work?", min_value=0, step=1)   

    
    if sl.form_submit_button("Submit"):
         #Enviroment 
# Revenue Efficiency
        revenue_efficiency = (total_monthly_revenue - (energy_cost + general_utilities) - intermediate_inputs) / (
            (energy_cost + general_utilities) - intermediate_inputs
        )
        
        # Carbon Credit Score
        carbon_credit_score = (carbon_credit / total_carbon) * 10
        
        # Green Product Revenue Percentage
        green_product_revenue_percentage = green_product_revenue / revenue
        
        # Waste Generator Score
        waste_generator_score = (1 / primary_waste_generator) * 10
        
        # Green Energy Score
        green_energy_score = (green_energy / total_energy) * 10
        
        # Average Energy-Related Costs
        average_energy_costs = (electricity + air_travel + employee_commute) / 3
        
        # Annual Electricity Emissions
        annual_electricity_emissions = electricity_kwh_monthly * 0.85 * 12
        phone_charges = (electricity_kwh * 1000) * 5
        
        # Emissions Rating
        emissions_rating = 10 - ((annual_electricity_emissions - 871.25 * num_employees) / (403.75 * num_employees)) * 9
        
        # Water Usage Rating
        water_usage_rating = 10 - ((water_cost / 0.05 - 62.85 * num_employees) / (25.7 * num_employees)) * 9
        bath_tubs_full = (water_cost / 0.05) / 302
        
        # Flight Emissions Rating
        flight_emissions = num_employees * flight_time_per_employee * 48 * 3.1
        flight_emissions_rating = 10 - ((flight_emissions - 119398.2466 * num_employees) / (255136.7094 * num_employees)) * 9
        distance_to_the_moon = (num_employees * flight_time_per_employee * 835) / 384400  # Distance to the moon in km
        
        # Travel Distance Emissions
        travel_emissions = (((num_employees * average_travel_distance * 255) / 100) * fuel_efficiency) * 2.474
        travel_emissions_rating = 10 - ((travel_emissions - 971.5 * num_employees) / (403.7 * num_employees)) * 9
        times_around_earth = (num_employees * avg_travel_distance_per_employee * 255) / 40075  # Earth circumference in km
        
                #Social
        # Average of Employee Answers for "Company Culture" + EMP Satisfaction / 2
        average_culture_satisfaction = (sum(employee_answers_culture) / len(employee_answers_culture) + emp_satisfaction) / 2
        
        # EMP Opinion + EMP Social / 2
        average_opinion_social = (emp_opinion + emp_social) / 2
        
        # Diversity Index
        diversity_index = ((male_employees / total_employees) * 100 + 
                           (female_employees / total_employees) * 100 + 
                           (lgbtq_employees / total_employees) * 100 + 
                           (differently_abled_employees / total_employees) * 100) / 4
        
        # Adjusted Score
        adjusted_score = max(1, min(10, math.ceil((diversity_index / 100) * 9 + 1)))
        
        # Revenue Efficiency
        revenue_efficiency = company_revenue / (wL * labor_input + wC * capital_input + wM * material_input)
        
        # Average Employee Salary Rating
        average_salary_rating = sum(employee_answers_culture) / len(employee_answers_culture)
        
        # Work Hours Rating
        if weekly_work_hours >= 60:
            work_hours_rating = 1
        elif 54 <= weekly_work_hours < 60:
            work_hours_rating = 2
        elif 51 <= weekly_work_hours < 54:
            work_hours_rating = 3
        elif 48 <= weekly_work_hours < 51:
            work_hours_rating = 4
        else:
            work_hours_rating = 5
        
        # Tenure-Based Promotion Index
        tenure_promotion_index = ((average_tenure_employees / average_tenure_executives) * 
                                  (total_employees / internal_promotions)) * 10
        
        # Health and Satisfaction Index
        health_satisfaction_index = (health_confidence + emp_satisfaction) / 2
        
        # Employee Separation Rate
        separation_rate = (employee_separations / total_employees) * 100
        
        # Average of Training Opportunities
        average_training_opportunities = sum(training_opportunities) / len(training_opportunities)
        
        # Mental Wellbeing and Non-Job-Related Training
        wellbeing_training_index = (mental_wellbeing + non_job_training) / 2
        
        #Governance
        # 1. Hiring Cost Formula
        hiring_cost = (num_employees * turnover_rate * average_departure_cost) + (
            hiring_manager_cost + average_hours_required + (percentage_salary_spent_on_development * hiring_manager_cost)
        )
        
        # 2. Supplier Retention Score
        supplier_retention_score = (remaining_suppliers / all_time_suppliers) * 10
        
        # 3. Tanh-Based Rating
        tanh_rating = 5 + 5 * math.tanh((RPR - 1) / 0.5)
        
        # 4. Workplace Average
        workplace_average = (location_rating + physical_workplace_rating) / 2
        
        # 5. Organizational Structure
        total_score = sum(role_scores[role] for role in selection)
        if 25 <= total_score <= 28:
            sl.write("Hierarchical (Traditional) Structure")
        elif 13 <= total_score <= 24:
            sl.write("Flat (Horizontal) Structure")
        elif 15 <= total_score <= 21 and ai1 == "Department Head":
            sl.write("Matrix Structure Score")
        elif 14 <= total_score <= 24 and ai1 in ["General", "Department Head"]:
            sl.write("Divisional Structure Score")
        else:
            sl.write("Undefined Structure")
        
        sl.write("Thank you for completing the ESG Diagnosis Survey. Your responses have been recorded.")
