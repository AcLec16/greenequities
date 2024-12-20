import math

def calculate_esg_score(company_data, employee_data):
    report = {}
    
        company_data["monthly_electricity_bill"] = 
        kwh_electricity = company_data["monthly_electricity_bill"] / 8
        #Enviroment 
        # Value Based Revenue Efficiency
        VRE_denominator = company_data["monthly_electricity_bill"] + company_data["monthly_water_bill"] + company_data["monthly_salary_costs"] + company_data["monthly_land_costs"] + company_data["monthly_raw_material_costs"]
        report["value_based_resource_efficiency"] = company_data["total_yearly_revenue"] /  VRE_denominator
        report["value_based_resource_efficiency_s"] = (f"Value-Based Resource Efficiency (value_based_resource_efficiency) for every ₹1 of stressed resources: {value_based_resource_efficiency:.2f}")

        #sustainability_statement
        report["sustainability_stance"] = company_data["company_stance_sustainability"]
        
        # Green Product Revenue Percentage
        
        report["green_product_revenue_percentage"] = company_data["green_product_revenue"] / company_data["total_yearly_revenue"]
        
        # Waste Generator Score
        report["waste_generator_score"] = (1 / company_data["primary_waste_generator"]) * 10
        
        # Green Energy Score
        report["green_energy_score"] = (company_data["green_energy"] / company_data["total_energy"]) * 10
                
        # Annual Electricity Emissions
        annual_electricity_emissions"] = kwh_electricity * 0.85 * 12
        report["phone_charges"] = (kwh_electricity * 1000) * 5
        report["emissions_rating"] = 10 - ((annual_electricity_emissions - 871.25 * company_data["total_employees"]) / (403.75 * company_data["total_employees"])) * 9

        # Water Usage Rating
        water_usage_rating = 10 - ((water_cost / 0.05 - 62.85 * company_data["total_employees"]) / (25.7 * company_data["total_employees"])) * 9
        bath_tubs_full = (water_cost / 0.05) / 302
        
        # Flight Emissions Rating
        total_flight_time = 0
        for emp in employee_data:
            total_flight_time += emp["work_travel_hours_year"]
        flight_time_per_employee = total_flight_time / len(employee_data)
         
        flight_emissions = total_employees * flight_time_per_employee * 48 * 3.1
        flight_emissions_rating = 10 - ((flight_emissions - 119398.2466 * company_data["total_employees"]) / (255136.7094 * company_data["total_employees"])) * 9
        distance_to_the_moon = (company_data["total_employees"] * flight_time_per_employee * 835) / 384400  # Distance to the moon in km
        
        # Travel Distance Emissions
        total_car_dist = 0
        for emp in employee_data:
            total_car_dist += emp["travel_distance_private_car"]
        average_travel_distance = total_car_time / len(employee_data)
        
        travel_emissions = (((total_employees * average_travel_distance * 255) / 100) * fuel_efficiency) * 2.474
        travel_emissions_rating = 10 - ((travel_emissions - 971.5 * total_employees) / (403.7 * total_employees)) * 9
        times_around_earth = (total_employees * avg_travel_distance_per_employee * 255) / 40075  # Earth circumference in km

        total_carbon = annual_electricity_emissions + flight_emissions + travel_emissions

        # Carbon Credit Score
        report["carbon_credit_score"] = (company_data["carbon_credits_bought"]/company_data["total_carbon"]) * 10
        report["average_energy_score"] = (travel_emissions_rating + emissions_rating + flight_emissions_rating) / 3

        #Primary Waste generator 
        
        def get_waste_value(waste_value):
             waste_values = {
         "Plastic": 7,
         "Food Waste": 6,
         "Electronic Waste (e-waste)": 5,
         "Fabric Scraps": 4,
         "Damaged or Expired Goods": 3,
         "Scrap Metals": 2,                        #?????????????????????
         "Paper Waste": 1,
     }
            return waste_values[waste_value]
        report["waste_value"] = get_waste_value(company_data["waste_value"])
        

        #SDGs
        report["selected_sdgs"] = company_data["selected_sdgs"]

                #Social
        # Average of Employee Answers for "Company Culture" + EMP Satisfaction / 2
        total_emp_culture = 0 
        for emp in employee_data:
            total_emp_culture += emp["company_culture_alignment"]
        employee_answers_culture = total_emp_culture / len(employee_data)
        total_emp_satisfaction = 0 
        for emp in employee_data:
            total_emp_satisfaction += emp["employer_satisfaction"]
        emp_satisfaction = total_emp_satisfaction / len(employee_data)
        average_culture_satisfaction = employee_answers_culture + emp_satisfaction) / 2
        
        # Inclusion at the workplace
        total_respect_rating = 0
        for emp in employee_data:
            total_respect_rating += emp["colleague_respect"]
        emp_opinion = total_respect_rating / len(employee_data)
        total_inclusion_rating = 0
        for emp in employee_data:
            total_inclusion_rating += emp["inclusion"]
        emp_social = total_inclusion_rating / len(employee_data)
        report["employee_inclusion"] = (emp_opinion + emp_social) / 2
        
        # Diversity Index
        diversity_index_score = ((company_data["male_employees"] / company_data["total_employees"]) * 100 + 
                           (company_data["female_employees"] / company_data["total_employees"]) * 100 + 
                           (company_data["lgbtq_employees"] / company_data["total_employees"]) * 100 + 
                           (company_data["differently_abled_employees"] / company_data["total_employees"]) * 100) / 4
        
        report["diversity_index"] = max(1, min(10, math.ceil((diversity_index_score / 100) * 9 + 1)))
    
        
        # Average Employee Salary Rating
        total_salary_rating = 0
        for emp in employee_data:
            total_salary_rating += emp["compensation_fairness"]
            average_salary_rating = total_salary_rating / len(employee_data)
    report["employee_compensation_fairness"] = average_salary_rating
        
        # Work Hours Rating
        total_work_hours = 0
        for emp in employee_data:
            total_work_hours == emp["work_hours_week"]
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
            total_emp_tenure += employee_data["company_tenure"]               #??????????????????????????????? conditional (exec only)
        average_tenure_employees = total_emp_tenure / len(employee_data)
        total_exec_tenure = 0
        num_executives = 0
        for emp in employee_data:
            if employee_data["executice_tenure"] > 0:
                total_exec_tenure += employee_data["executive_tenure"]
                num_executives++
        average_tenure_executives =  total_exec_tenure / num_executives
        report["tenure_promotion_index"] = ((average_tenure_employees / average_tenure_executives) * 
                                  (company_data["total_employees"] / company_data["internal_promotions"])) * 10
        
        # Health and Satisfaction Index
        selected_practices = len(company_data["health_practices"])
        health_confidence = (selected_practices / 10) * 10
        total_employee_health = 0
        for emp in employee_data:
            total_employee_health += emp["health_wellbeing"]
        employee_health = total_employee_health / len(employee_data)
        report["health_satisfaction_index"] = (health_confidence + employee_health) / 2
        
        # Employee Separation Rate
        report["turnover_rate"] = (company_data["employee_separations"] / company_data["total_employees"]) * 100
        
        # Mental Wellbeing and Non-Job-Related Training
        total_employee_training = 0 
        for emp in employee_data:
            total_employee_training += emp["training_opportunities"]
        employee_training_opportunities = total_employee_training / len(employee_data)
        report["wellbeing_training_index"] = (employee_health + employee_training_opportunities) / 2
        

 
        

    
    
        ##########################################################################################################################################
        ##########################################################################################################################################
        #Governance
        #Stakeholder_engagment
        report["Customer_feedbacks"] = company_answers["customer_feedback_score"]
        report["customer_statement"] = company_answers["customer_feedback"]
        #NGOs 
        report["NGO_statement"] = company_answers["NGO_statement"]
        company_answers["social_impact_partnerships"] = company_answers["social_impact_partnerships"]
        
         # 2. Supply chain ESG
        report["supplier_retention_score"] = (company_data["remaining_suppliers"] / company_date["all_time_suppliers"]) * 10
        report["supply_statement"] = company_data["supply_statement"]
        
        #Investor/Shareholder Feedback
        report["Investor/Shareholder_statement"] = company_data["Investor/Shareholder_statement"]

        # 1. Hiring Cost Formula
        report["hiring_cost"] = (company_data["total_employees"] * report["turnover_rate"] * average_departure_cost) + (
            hiring_manager_cost + average_hours_required + (percentage_salary_spent_on_development * hiring_manager_cost)
        )
        
       
        # 3. Sector Growth Rating
        
        def get_sector_value(industry):                #####################?????????????????????????/
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
            else industry in sector_ratings:
                return sector_ratings[industry]
        report["Sector_growth_Rating"] = get_sector_value(company_data["industry"])
        # 4. Workplace Average
        total_health_wellbeing = 0 
        for emp in employee_data:
            total_health_wellbeing += emp["workplace_rating"]
            physical_workplace_rating = total_health_wellbeing / len(employee_data)
        report["workplace_average"] = (company_data["location_rating"] + physical_workplace_rating) / 2
       
        #Business Awards and Recognition
        report["awards_received"] = company_data["awards_received"]
        
        #Compliance certifications
        report["compliance_certifications"] = company_data["compliance_certifications"]

        #Anti Corruption
        selected_anti = len(company_data["Anti_Corruption"])
        report["Anti_Corruption_score"] = (selected_anti / 10) * 10

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
            else industry in sector_ratings_volatility:
                return sector_ratings_volatility[industry]
        
        #Information Asymmetry
        total_informed = 0 
        for emp in employee_data:
            total_informed += emp["informed_by_management"]
            informed_rating = total_informed / len(employee_data)
        total_time
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
            report["infomation_flow_efficency"] = (informed_rating + time_score) / 2
        #GeoPoli Risk 
        report["Geopolitical_Risk_Index"] = 6.6 
        report["India_News_sentiment"] = 5.09
        report["India_Google_Uncertainty"] = 6.08
        report["Market_Uncertainty"] = 5.78
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

#Strategic Risk

#Compliance and Regulatory Risk

#Financial Risk

#Operational Risk 

#Total Environment

#Total social

#Total Governance 



return report

   
    if sl.form_submit_button("Submit"):
