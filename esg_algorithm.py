
import math

def calculate_esg_score(company_data, employee_data):
    report = {}
    
    report["company_name"] =  company_data["company_name"]
    report["form_filler"] = company_data["form_filler"]
    report["CEO_message"] = company_data["CEO_message"]
    report["current_financial_year_month"] = company_data["current_financial_year_month"]
    report["main_business_activity"] = company_data["main_business_activity"]
    report["website"] =  company_data["website"]
    report["email_address"] = company_data["email_address"]
    report["telephone"] =  company_data["telephone"]
    report["social_media"] =  company_data["social_media"]
    report["mission_statement"] =  company_data["mission_statement"]
    report["year_of_opening"] = company_data["year_of_opening"]
    report["selected_locations"] = company_data["selected_locations"]
    report["csr_person"] = company_data["csr_person"]
    report["materiality_assessment"] = company_data["materiality_assessment"]

    kwh_electricity = company_data["monthly_electricity_bill"] / 8
    #Enviroment 
    # Value Based Revenue Efficiency
    VRE_denominator = company_data["monthly_electricity_bill"] + company_data["monthly_water_bill"] + company_data["monthly_salary_costs"] + company_data["monthly_land_costs"] + company_data["monthly_raw_material_costs"]
    vbre = company_data["total_yearly_revenue"] /  VRE_denominator
    report["value_based_resource_efficiency_s"] = f"Value-Based Resource Efficiency (value_based_resource_efficiency) for every ₹1 of stressed resources: {vbre:.2f}"
    vbre_rating = 0
    if vbre <= 0.5:
        vbre_rating =  1
    elif 0.51 <= vbre <= 0.75:
        vbre_rating =  2
    elif 0.76 <= vbre <= 1.0:
        vbre_rating =  3
    elif 1.01 <= vbre <= 1.5:
        vbre_rating =  4
    elif 1.51 <= vbre <= 1.75:
        vbre_rating =  5
    elif 1.76 <= vbre <= 2.0:
        vbre_rating =  6
    elif 2.01 <= vbre <= 3.0:
        vbre_rating =  7
    elif 3.01 <= vbre <= 5.0:
        vbre_rating =  8
    elif 5.01 <= vbre <= 10.0:
        vbre_rating =  9
    else:
        vbre_rating =  10
    
    #Enviro_laws 
    selected_enviro = len(company_data["compliant_laws"])
    enviro_comp = selected_enviro
    report["Enviroment_Laws_Compliance"] = enviro_comp
    report["Enviroment_Laws_Compliance_list"] = company_data["compliant_laws"]
    #sustainability_statement
    report["sustainability_stance"] = company_data["company_stance_sustainability"]
        
    # Green Product Revenue Percentage
    green_product_revenue_percentage = (company_data["green_product_revenue"] / company_data["total_yearly_revenue"])* 100
    score_product = round((green_product_revenue_percentage / 10), 1)
    score_product = max(1, min(10, score_product))
    report["green_product_revenue_percentage"] = score_product


    # Green Energy Score
    green_energy_score = round((company_data["green_energy"] / company_data["total_energy"]) * 10, 2) 
    report["green_energy_score"] = green_energy_score
                
    # Annual Electricity Emissions
    annual_electricity_emissions = kwh_electricity * 0.85 * 12
    phone_charges = (kwh_electricity * 1000) * 5
    report["phone_charges"] = f"You could charge your phone {phone_charges:.2f} times! Based on the electricity usage of {kwh_electricity:.2f} kWh."
    base_rating = ((annual_electricity_emissions / company_data["total_employees"]) - 871.25) / 403.75
    emissions_rating = ((base_rating + 0.89) * 9) + 1
    emissions_rating = max(1, min(10, emissions_rating))
    report["emissions_rating"] = emissions_rating
    
    # Water Usage Rating
    monthly_water_bill = company_data["monthly_water_bill"]
    base_value = ((((monthly_water_bill / 0.05)/company_data["total_employees"]) - 968) / 677.6) 
    water_usage_rating = ((base_value + 0.46) * 9) + 1
    rounded_water_usage_rating = round(water_usage_rating, 2)
    bath_tubs_full= (monthly_water_bill / 0.05) / 302
    bath_tubs_full_rounded = round(bath_tubs_full)
    report["bath_tubs_full"] = f"The monthly water bill equates to approximately {bath_tubs_full_rounded} bath tubs full of water."
    report["water_usage_rating"] = rounded_water_usage_rating
    
    # Flight Emissions Rating
    total_flight_time = 0
    for emp in employee_data:
        total_flight_time += emp["work_travel_hours_year"]
    flight_time_per_employee = total_flight_time / len(employee_data)
    flight_emissions = company_data["total_employees"] * flight_time_per_employee * 48 * 3.1
    base_emissions_rating =  (((flight_emissions/company_data["total_employees"]) - 119398.2466) / 255136.7094)
    flight_emissions_rating = ((base_emissions_rating + 0.34) * 9) + 1
    flight_emissions_rating = max(1, min(10, flight_emissions_rating))
    report["flight_emissions_rating"] = flight_emissions_rating
    distance_to_the_moon = ((company_data["total_employees"] * flight_time_per_employee * 835) / 384400)*100
    report["distance_to_the_moon"] = f"The total flight time for all employees would cover approximately {distance_to_the_moon:.2f}% of the distance from Earth to the Moon."

    # Travel Distance Emissions
    total_car_dist = 0
    for emp in employee_data:
        total_car_dist += emp["travel_distance_private_car"]
    average_travel_distance = total_car_dist / len(employee_data)
    fuel_efficiency = 8.9  # Average fuel efficiency in km/l
    travel_emissions = (((company_data["total_employees"] * average_travel_distance * 255) / 100) * fuel_efficiency) * 2.474
    travel_emissions_rating = 10 - (((travel_emissions/company_data["total_employees"]) - 971.5) / 403.7) * 9
    travel_emissions_rating_rounded = round(travel_emissions_rating , 2)
    report["travel_emissions_rating"] = travel_emissions_rating_rounded
    times_around_earth = round(company_data["total_employees"] * average_travel_distance * 255) / 40075  # Earth circumference in km
    report["times_around_earth"] = f"The total travel distance for all employees, with an average travel distance of {average_travel_distance} km per employee, would cover approximately {times_around_earth} times around the Earth."
    
    total_carbon = round(annual_electricity_emissions + flight_emissions + travel_emissions, 2)
    report["total_carbon"] = total_carbon

    # Carbon Credit Score
    carbon_credit_score = company_data["carbon_credits_bought"] / total_carbon

    # Assign a rating based on the ratio
    if carbon_credit_score >= 0.9:
        carbon_credit_rating = 10
    elif 0.8 <= carbon_credit_score < 0.9:
        carbon_credit_rating = 9
    elif 0.7 <= carbon_credit_score < 0.8:
        carbon_credit_rating = 8
    elif 0.6 <= carbon_credit_score < 0.7:
        carbon_credit_rating = 7
    elif 0.5 <= carbon_credit_score < 0.6:
        carbon_credit_rating = 6
    elif 0.4 <= carbon_credit_score < 0.5:
        carbon_credit_rating = 5
    elif 0.3 <= carbon_credit_score < 0.4:
        carbon_credit_rating = 4
    elif 0.2 <= carbon_credit_score < 0.3:
        carbon_credit_rating = 3
    elif 0.1 <= carbon_credit_score < 0.2:
        carbon_credit_rating = 2
    else:
        carbon_credit_rating = 1

    # Add the carbon credit score and rating to the report
    report["carbon_credit_rating"] = carbon_credit_rating
    report["average_energy_score"] = round((travel_emissions_rating + emissions_rating + flight_emissions_rating) / 3, 2)

    #Primary Waste generator 
    
    def get_waste_value(primary_waste_generator):
        waste_values = {
            "Plastic Waste": 3,
            "Food Waste": 4,
            "Electronic Waste (e-waste)": 2,
            "Fabric Scraps": 5,
            "Scrap Metals": 9,
            "Paper Waste": 7,
            "Glass Waste": 8,
            "Hazardous Chemicals or Substances": 1,
            "Construction and Demolition Debris": 6,
            "Packaging Waste": 10,
        }
        return waste_values[primary_waste_generator]
    
    waste_value = get_waste_value(company_data["primary_waste_generator"])
    report["waste_value"] = waste_value
    #SDGs
    #Ensure company_data["selected_sdgs"] is valid
    report["selected_sdgs"] = company_data.get("selected_sdgs", [])

    # SDG image paths dictionary
    sdg_image_paths = {
        "No Poverty": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/Poverty.png",
        "Zero Hunger": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/Zero Hunger.png",
        "Good Health and Well-Being": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/Good health.png",
        "Quality Education": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/education.png",
        "Gender Equality": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/Gender Equality.png",
        "Clean Water and Sanitation": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/Clean water.png",
        "Affordable and Clean Energy": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/energy.png",
        "Decent Work and Economic Growth": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/decent work.png",
        "Industry, Innovation and Infrastructure": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/industry, innovation.png",
        "Reduced Inequality": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/inequalities.png",
        "Sustainable Cities and Communities": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/sustainable cities.png",
        "Responsible Consumption and Production": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/Responsible consumption.png",
        "Climate Action": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/climate action.png",
        "Life Below Water": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/life below water.png",
        "Life on Land": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/life on land.png",
        "Peace, Justice, and Strong Institutions": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/peace justice.png",
        "Partnerships for the Goals": "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/partnerships for the goals.png",
}

    # Helper function for mapping SDGs to image paths
    def map_sdgs_to_paths(selected_sdgs, sdg_image_map):
        missing_sdgs = [sdg for sdg in selected_sdgs if sdg not in sdg_image_map]
        if missing_sdgs:
            print(f"Warning: The following SDGs are missing image paths: {missing_sdgs}")
        return [sdg_image_map[sdg] for sdg in selected_sdgs if sdg in sdg_image_map]

    # Map SDGs to their image paths
    sdg_image_paths = map_sdgs_to_paths(report["selected_sdgs"], sdg_image_paths)


    #######Social##########Social##########Social##########Social##########Social##########Social##########Social#######
    #Leadership_Rating
    total_leader = 0 
    for emp in employee_data:
        total_leader +=  emp["leadership_confidence"]
    leader_confidence = total_leader / len(employee_data)
    report["leader_confidence"] = leader_confidence      
    # Average of Employee Answers for "Company Culture" + EMP Satisfaction / 2
    total_emp_culture = 0 
    for emp in employee_data:
        total_emp_culture += emp["company_culture_alignment"]
    employee_answers_culture = total_emp_culture / len(employee_data)
    total_emp_satisfaction = 0 
    for emp in employee_data:
        total_emp_satisfaction += emp["employer_satisfaction"]
    emp_satisfaction = total_emp_satisfaction / len(employee_data)
    average_culture_satisfaction = (employee_answers_culture + emp_satisfaction) / 2
    report["average_culture_satisfaction"] = average_culture_satisfaction
        
    # Inclusion at the workplace
    total_respect_rating = 0
    for emp in employee_data:
        total_respect_rating += emp["colleague_respect"]
    emp_opinion = total_respect_rating / len(employee_data)
    total_inclusion_rating = 0
    for emp in employee_data:
        total_inclusion_rating += emp["inclusion"]
    emp_social = total_inclusion_rating / len(employee_data)
    employee_inclusion = (emp_opinion + emp_social) / 2
    report["employee_inclusion"] = employee_inclusion
        
    # Diversity Index
    diversity_index_score = ((company_data["male_employees"] / company_data["total_employees"]) * 100 + 
                       (company_data["female_employees"] / company_data["total_employees"]) * 100 + 
                       (company_data["lgbtq_employees"] / company_data["total_employees"]) * 100 + 
                       (company_data["differently_abled_workers"] / company_data["total_employees"]) * 100) / 4
    diversity_index = max(1, min(10, math.ceil((diversity_index_score / 100) * 9 + 1)))
    report["diversity_index"] = diversity_index
    
        
    # Average Employee Salary Rating
    total_salary_rating = 0
    for emp in employee_data:
        total_salary_rating += emp["compensation_fairness"]
    average_salary_rating = total_salary_rating / len(employee_data)
    report["employee_compensation_fairness"] = average_salary_rating
        
    # Work Hours Rating
    total_work_hours = 0
    for emp in employee_data:
        total_work_hours += emp["work_hours_week"]
    weekly_work_hours =  total_work_hours / len(employee_data)
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
    report["work_hours"] =  work_hours_rating
        
    # Tenure-Based Promotion Index
    total_emp_tenure = 0
    for emp in employee_data:
        total_emp_tenure += emp["company_tenure"]   
    average_tenure_employees = total_emp_tenure / len(employee_data)
    total_exec_tenure = 0
    num_executives = 0
    for emp in employee_data:
        if emp["executive_tenure"] > 0:
            total_exec_tenure += emp["executive_tenure"]
            num_executives+=1
    average_tenure_executives =  total_exec_tenure / num_executives
    tenure_promotion_index = ((average_tenure_employees / average_tenure_executives) * (company_data["total_employees"] / company_data["internal_promotions"])) * 10
    normalized_promotion_index = min((tenure_promotion_index / 100) * 10, 10)
    report["tenure_promotion_index"] = normalized_promotion_index

      
    # Health and Satisfaction Index
    health_confidence = len(company_data["health_practices"])
    total_employee_health = 0
    for emp in employee_data:
        total_employee_health += emp["health_wellbeing"]
    employee_health = total_employee_health / len(employee_data)
    health_satisfaction_index = (health_confidence + employee_health) / 2
    report["health_satisfaction_index"] = health_satisfaction_index
        
    # Employee Separation Rate
    def calculate_turnover_rating(turnover_rate):
        if turnover_rate == 0:
            return 10  # No turnover, excellent retention
        elif turnover_rate <= 10:
            return 9  # Low turnover, very good retention
        elif turnover_rate <= 20:
            return 8  # Slightly above average turnover
        elif turnover_rate <= 30:
            return 7  # Moderate turnover, acceptable retention
        elif turnover_rate <= 40:
            return 6  # High turnover, needs improvement
        elif turnover_rate <= 50:
            return 5  # Very high turnover, significant concern
        elif turnover_rate <= 60:
            return 4  # Alarmingly high turnover
        elif turnover_rate <= 70:
            return 3  # Critical turnover level
        elif turnover_rate <= 80:
            return 2  # Severe turnover crisis
        else:
            return 1  # Extremely high turnover, urgent intervention required
    
    # Example usage
    turnover_rate = (company_data["employee_separations"] / company_data["total_employees"]) * 100
    turnover_rating = calculate_turnover_rating(turnover_rate)
    report["turnover_rating"] = turnover_rating
        
    # Mental Wellbeing and Non-Job-Related Training
    total_employee_training = 0 
    for emp in employee_data:
        total_employee_training += emp["training_opportunities"]
    employee_training_opportunities = total_employee_training / len(employee_data)
    wellbeing_training_index = (employee_health + employee_training_opportunities) / 2
    report["wellbeing_training_index"] = wellbeing_training_index

    #Job related compliance training 
    total_emp_training = 0 
    for emp in employee_data:
         total_emp_training += emp["Job_related_training"]
    employee_job_related_training = total_emp_training/ len(employee_data)
    report["employee_job_related_training"] =  employee_job_related_training
 
    
    ##########################################################################################################################################
    ##########################################################################################################################################
    #Governance
    
    selected_data_laws = len(company_data["data_comp"])
    report["data_law_compliance"] = selected_data_laws
    report["data_law_compliance_list"] = company_data["data_comp"]

    #Stakeholder_engagment
    Customer_feedbacks = company_data["customer_feedback_score"] * 2
    report["Customer_feedbacks"] = company_data["customer_feedback_score"]
    report["customer_statement"] = company_data["customer_feedback"]
    
    #NGOs 
    report["NGO_statement"] = company_data["NGO_statement"]
    report["social_impact_partnerships"] = company_data["social_impact_partnerships"]
    
     # 2. Supply chain ESG
    supplier_retention_score = (company_data["remaining_suppliers"] / company_data["all_time_suppliers"]) * 10
    supplier_retention_score_round = round(supplier_retention_score)
    report["supplier_retention_score"] = supplier_retention_score_round
    report["supply_statement"] = company_data["supply_statement"]
    
    #Investor/Shareholder Feedback
    report["Investor/Shareholder_statement"] = company_data["Investor/Shareholder_statement"]
    
    # 3. Sector Growth Rating
    
    def get_sector_value(industry): 
        sector_ratings = {
        "MICROCAP 250": 9.82,
        "Auto": 9.89,
        "Financial Services": 6.96,
        "FMCG": 8.90,
        "Healthcare": 9.67,
        "IT": 6.91,
        "Media": 0.40,
        "Metal": 4.10,
        "Pharma": 9.76,
        "Realty": 6.59,
        "Consumer Durables": 9.95,
        "Oil and Gas": 5.45
    }
        # If industry is "Other", use "NIFTY MICROCAP 250"
        if industry == "Other":
            return sector_ratings["MICROCAP 250"]
        # If industry exists in the sector_ratings dictionary, return its value
        elif industry in sector_ratings:
            return sector_ratings[industry]
    report["Sector_growth_Rating"] = get_sector_value(company_data["industry"])
    
    # 4. Workplace Average
    total_health_wellbeing = 0 
    for emp in employee_data:
        total_health_wellbeing += emp["workplace_rating"]
    physical_workplace_rating = total_health_wellbeing / len(employee_data)
   
       
    #Business Awards and Recognition
    report["awards_received"] = company_data["awards_received"]
        
    #Compliance certifications
    report["compliance_certifications"] = company_data["compliance_certifications"]

    #Anti Corruption
    selected_anti = len(company_data["Anti_Corruption"])
    report["Anti_Corruption_score"] = selected_anti 
    report["Anti_Corruption_score_list"] = company_data["Anti_Corruption"]

    #Volatility 
    
    def get_volatility_value(industry):
        sector_ratings_volatility = {
        "MICROCAP 250": 3.29,
        "Auto": 4.74,
        "Financial Services": 4.83,
        "FMCG": 4.46,
        "Healthcare": 3.82,
        "IT": 1,
        "Media": 1,
        "Metal": 2.74,
        "Pharma": 3.73,
        "Realty": 2.25,
        "Consumer Durables": 5.12,
        "Oil and Gas": 4.54
    }
        # If industry is "Other", use "NIFTY MICROCAP 250"
        if industry == "Other":
            return sector_ratings_volatility["MICROCAP 250"]
        # If industry exists in the sector_ratings dictionary, return its value
        elif industry in sector_ratings_volatility:
            return sector_ratings_volatility[industry]
        report["sector_volatility"] = sector_ratings_volatility
    
    #Information Asymmetry
    total_informed = 0 
    for emp in employee_data:
        total_informed += emp["informed_by_management"]
    informed_rating = total_informed / len(employee_data)
    total_time = 0
    for emp in employee_data:
        total_time += emp["information_flow_time"]
    average_time = total_time / len(employee_data)
            
    if average_time <= 0.5:
        time_score = 10
    elif 0.5 < average_time <= 1:
        time_score = 9
    elif 1 < average_time <= 2:
        time_score = 8
    elif 2 < average_time <= 3:
        time_score = 7
    elif 3 < average_time <= 5:
        time_score = 6
    elif 5 < average_time <= 7:  # 1-2 days
        time_score = 5
    elif 7 < average_time <= 10:  # 2-3 days
        time_score = 4
    elif 10 < average_time <= 15:  # 3-5 days
        time_score = 3
    elif 15 < average_time <= 20:  # 5-7 days
        time_score = 2
    else: 
        time_score = 1
    infomation_flow_efficency = (informed_rating + time_score) / 2
    report["infomation_flow_efficency"] = infomation_flow_efficency
    
    #GeoPoli Risk 
    report["Geopolitical_Risk_Index"] = 6.6 
    report["India_News_sentiment"] = 5.09
    report["India_Internet_sentiment"] = 6.08
    report["Market_Uncertainty"] = 5.78
    
    # 5. Organizational Structure
    role_scores = {
        "Chairman": 10,
        "CEO": 9,
        "COO": 8,
        "CFO": 7,
        "General Manager": 6,
        "Department Head": 5,
        "Employee": 1
    }
    
    # Get the selected roles from the multiselect
    selection = company_data["roles"]
    total_score = 0
    for role in selection:
        total_score += role_scores[role]
    
    # Calculate total score based on the selected roles
    structure_type = ""
    structure_rating = 0

    if 25 <= total_score <= 28:  # More hierarchical, with high-level roles selected
        structure_type = "Hierarchical (Traditional) Structure"
        structure_rating = 3
    elif 13 <= total_score <= 24:  # Moderate selection, with both senior and mid-level roles
        structure_type = "Flat (Horizontal) Structure"
        structure_rating = 5
    elif 15 <= total_score <= 21 and "Department Head" in selection:  # Departmental heads indicate matrix structure
        structure_type = "Matrix Structure"
        structure_rating = 4
    elif 14 <= total_score <= 24 and any(role in selection for role in ["General Manager", "Department Head"]):  # Divisional structure
        structure_type = "Divisional Structure"
        structure_rating = 2
    else:
        structure_type = "Non-Standard Structure" 
        structure_rating = 3
    report["cooperate_stucture"] = structure_type
    
    #profit to revenue ratio 
    profit_to_revenue_ratio = (company_data["monthly_profit"] / company_data["total_yearly_revenue"]) * 100
    if profit_to_revenue_ratio >= 20:
        profit_rating = 10
    elif profit_to_revenue_ratio >= 15:
         profit_rating = 9
    elif profit_to_revenue_ratio >= 12:
         profit_rating = 8
    elif profit_to_revenue_ratio >= 10:
         profit_rating = 7
    elif profit_to_revenue_ratio >= 8:
         profit_rating = 6
    elif profit_to_revenue_ratio >= 6:
         profit_rating = 5
    elif profit_to_revenue_ratio >= 4:
         profit_rating = 4
    elif profit_to_revenue_ratio >= 2:
         profit_rating = 3
    elif profit_to_revenue_ratio >= 1:
         profit_rating = 2
    else:
         profit_rating = 1
    report["profit_to_revenue_ratio"] = profit_rating

    #Location_Rating 

    def get_location_value(selected_locations):
        location_ratings = {
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
            "Dadar": 4.4,
            "Bengaluru": 4.3,
            "Delhi": 4.3,
            "Hyderabad": 4.3
        }

        if selected_locations == "Other":
            return location_ratings["Khar"]
            # If industry exists in the sector_ratings dictionary, return its value
        elif selected_locations in location_ratings:
                return location_ratings[selected_locations]
    location_rating = get_location_value(company_data["selected_locations"])
    report["buissnes_location_rating"] = location_rating
    if company_data["selected_locations"] == "Other":
        report["selected_locations"] = company_data["custom_locations"]
    else:
        report["selected_locations"] = company_data["selected_locations"]
        report["workplace_average"] = (location_rating + physical_workplace_rating) / 2

    #Strategic Risk
    strategic_risk =  ((get_sector_value(company_data["industry"]) - 1 / 9)) +  ((Customer_feedbacks - 1 / 9)) + ((vbre - 1) / 9) + ((leader_confidence - 1) / 9) + ((informed_rating - 1) / 9)
    if strategic_risk >= 70:
        risk_level_strat = "high probability"
    elif strategic_risk >= 40:
        risk_level_strat = "medium probability"
    else:
        risk_level_strat = "low probability"
    
    report["strategic_risk"] = (f"Strategic Risk stands at {strategic_risk:.2f}% putting you at a {risk_level_strat} of risk in this area.")

    #Compliance and Regulatory Risk
    Compliance_and_Regulatory_Risk = ((health_confidence - 1) / 9) + ((enviro_comp - 1) / 9) + ((employee_job_related_training - 1) / 9) + ((employee_health - 1) / 9) + ((emp_satisfaction - 1) / 9) 
    + ((average_salary_rating - 1) / 9) + ((selected_data_laws - 1) / 9) * 100 
    if Compliance_and_Regulatory_Risk >= 70:
        risk_level = "high probability"
    elif Compliance_and_Regulatory_Risk >= 40:
        risk_level = "medium probability"
    else:
        risk_level = "low probability"
    
    report["Compliance_and_Regulatory_Risk"] = (f"Compliance and Regulatory Risk stands at {Compliance_and_Regulatory_Risk:.2f}% putting you at a {risk_level} of risk in this area.")
        
    #Financial Risk
    Financial_risk = ((get_volatility_value(company_data["industry"]) - 1) / 9) + ((get_sector_value(company_data["industry"]) - 1) / 9) +  ((profit_rating - 1) / 9) / 3 
    if  Financial_risk >= 70:
        risk_level_fin = "high probability"
    elif Financial_risk >= 40:
        risk_level_fin = "medium probability"
    else:
        risk_level_fin = "low probability"
    
    report["Financial_Risk"] = (f"Financial Risk stands at {Financial_risk:.2f}% putting you at a {risk_level_fin} of risk in this area.")

    #Operational Risk 
    Operational_Risk = ((infomation_flow_efficency - 1) / 9) + ((supplier_retention_score - 1) / 9) + (0.61) + ((location_rating - 1) / 9) + ((selected_anti - 1) / 9)
    if Operational_Risk >= 70:
        risk_level_opp = "high probability"
    elif Operational_Risk >= 40:
        risk_level_opp = "medium probability"
    else:
        risk_level_opp = "low probability"
    
    report["Operational_Risk"] = (f"Compliance and Regulatory Risk stands at {Operational_Risk:.2f}% putting you at a {risk_level_opp} of risk in this area.")

    #Total Environment
    total_environment = round(((0.1*vbre_rating + 0.15*enviro_comp + 0.1*waste_value + 0.15*green_energy_score + 0.15*emissions_rating + 0.1*water_usage_rating + 0.05*flight_emissions_rating + 0.05*travel_emissions_rating) / 8)*10, 2)

    #Total social
    total_social = ((leader_confidence + employee_inclusion + average_salary_rating + diversity_index + work_hours_rating + tenure_promotion_index + health_satisfaction_index + wellbeing_training_index + employee_job_related_training + turnover_rating + average_culture_satisfaction) / 10)*10
   
    #Total Governance
    total_governance = round(((0.1 *location_rating + 0.1 *supplier_retention_score + 0.05*get_volatility_value(company_data["industry"]) + 0.05*get_sector_value(company_data["industry"]) + 0.2*profit_rating + 0.1 *infomation_flow_efficency + 0.1 *structure_rating
         + 0.1 *selected_data_laws + 0.05*selected_anti + 0.1*Customer_feedbacks + 0.05*physical_workplace_rating + 0.294) / 12)*10, 2)

    report["total_environment"] = total_environment
    report["total_social"] = total_social
    report["total_governance"] = total_governance
    return report
