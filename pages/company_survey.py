import streamlit as st
import uuid

from firebase_config import store_company_data

def run():
    st.header("Company Survey Form")
    # company_name = st.text_input("Company Name")
    company_answers = {}
    
    # # Collect dynamic survey data
    # for i in range(1, 6):
    #     company_answers[f"q{i}"] = st.slider(f"Question {i}", 0, 10, 5)

    company_answers["company_name"] = st.text_input("Company name") 
    company_answers["year_of_opening"] = st.number_input("Year of Opening", min_value=1900, max_value=2100, step=1)
    company_answers["selected_locations"] = st.multiselect(
    "Select Office Location:",
    ["Worli", "Malabar & Cumballa Hill", "Juhu", "Bandra Kurla Complex", "Nariman Point", 
     "Andheri", "Lower Parel", "Parel", "Bandra", "Santacruz", "Ghatkopar", "Thane", 
     "Goregaon", "Byculla", "Fort", "Borivali", "Jogeshwari", "Khar", "Malad", 
     "Vile Parle", "Chembur", "Dharavi", "Colaba", "Dadar"]
)
    company_answers["industry"] = st.radio(
    "Select Industry:",
    [
        "Financial Services", "FMCG", "Healthcare", "IT", "Media",
        "Metal", "Pharma", "Realty", "Consumer Durables",
        "Oil and Gas", "Other"
    ]
)
    company_answers["health_practices"] = st.multiselect(
    "Which of the following health practices does your business currently implement?",
    [
        "Comprehensive health and safety policies",
        "Mental health support resources",
        "Physical wellness programs (e.g., fitness initiatives)",
        "Ergonomic workspaces",
        "Health insurance and wellness benefits",
        "Healthy food options in the workplace",
        "Adequate sick leave and flexible work policies",
        "Hygiene and cleanliness of workplace facilities",
        "Regular health education and training sessions",
        "Mechanisms for employee feedback on health and wellness",
    ]
)

)
    company_answers["csr_person"] = st.radio(
    "Does the entity have a specified Committee of the Board/Director responsible for corporate responsibility-related activities?", 
    ("Yes", "No")
)
    company_answers["form_filler"] = st.text_input("Name of person responsible for filling out this form")
    company_answers["website"] = st.text_input("Website")
    company_answers["email_address"] = st.text_input("Email address")
    company_answers["telephone"] = st.text_input("Telephone")
    company_answers["social_media"] = st.text_input("Social Media")
    company_answers["mission_statement"] = st.text_area("Mission statement")

    # Financial and Operational Metrics
    company_answers["monthly_water_bill"] = st.number_input("What is the monthly Water Bill?", min_value=0.0, step=0.01)
    company_answers["monthly_electricity_bill"] = st.number_input("What is the monthly Electricity bill?", min_value=0.0, step=0.01)
    company_answers["monthly_profit"] = st.number_input("Monthly Profit", min_value=0.0, step=0.01)
    company_answers["monthly_labor_costs"] = st.number_input("Monthly Labor Costs", min_value=0.0, step=0.01)
    company_answers["monthly_land_costs"] = st.number_input(
        "Monthly Land Costs (Rent, Storage facilities, Manufacturing facilities)", min_value=0.0, step=0.01
    )
    company_answers["monthly_raw_material_costs"] = st.number_input(
        "Monthly costs of acquiring new raw material (if applicable)", min_value=0.0, step=0.01
    )
    company_answers["total_monthly_revenue"] = st.number_input("Total Monthly Revenue", min_value=0.0, step=0.01)

    # Employee Information
    company_answers["total_employees"] = st.number_input("Total number of Employees", min_value=0, step=1)
    company_answers["male_employees"] = st.number_input("Number of Male Employees", min_value=0, step=1)
    company_answers["female_employees"] = st.number_input("Number of Female employees", min_value=0, step=1)
    company_answers["lgbtq_employees"] = st.number_input("Number of LGBTQ+ Employees", min_value=0, step=1)
    company_answers["differently_abled_workers"] = st.number_input("Differently abled workers", min_value=0, step=1)
    company_answers["employee_separations"] = st.number_input("Number of employee separations over the past 2 years?", min_value=0, step=1)
    company_answers["customer_feedback_score"] = st.slider(
        "Customer feedback score (using company feedback system or Google Business rating)", min_value=0, max_value=5, step=1
    )

    # Supplier Information
    company_answers["all_time_suppliers"] = st.number_input("How many all-time suppliers have you had?", min_value=0, step=1)
    company_answers["remaining_suppliers"] = st.number_input("What is the Number of remaining suppliers?", min_value=0, step=1)

    # Environmental and Energy Metrics
    company_answers["carbon_credits_bought"] = st.number_input("Carbon credits bought (Co2 emissions)", min_value=0.0, step=0.01)
    company_answers["green_product_revenue"] = st.number_input("Green Product Revenue", min_value=0.0, step=0.01)
    company_answers["green_energy"] = st.number_input("Energy from Sustainable sources (KwH)", min_value=0.0, step=0.01)
    company_answers["total_energy"] = st.number_input("Total Energy Used per month (KwH)", min_value=0.0, step=0.01)
    ##########Waste values 
    # waste_values = {
    #     "Plastic": 7,
    #     "Food Waste": 6,
    #     "Electronic Waste (e-waste)": 5,
    #     "Fabric Scraps": 4,
    #     "Damaged or Expired Goods": 3,
    #     "Scrap Metals": 2,
    #     "Paper Waste": 1,
    # }
    company_answers["primary_waste_generator"] = st.radio(
        "What is your company's primary waste generator:", ["Plastic", "Food Waste", 
        "Electronic Waste (e-waste)", "Fabric Scraps", "Damaged or Expired Goods", "Scrap Metals", "Paper Waste"]
    )
    company_answers["company_stance_sustainability"] = st.text_area(
        "Business’ current stance on environmental sustainability (100 words or less)"
    )
    company_answers["clean_tech_initiatives"] = st.text_area(
        "Company initiatives on clean technology, energy efficiency, renewable energy, etc."
    )

    # Governance and Policies
    company_answers["anti_corruption_policy"] = st.selectbox(
        "Does the business have anti-corruption policies?", ("Yes", "No")
    )
    company_answers["anti_corruption_policy_link"] = st.text_input("Anti-corruption policy link (if available)")
    company_answers["board_director_responsibility"] = st.selectbox(
        "Entity has Board/Director responsible for corporate responsibility activities", ("Yes", "No")
    )
    company_answers["Investor/Shareholder_statement"] = st.text_area("How does your company ensure that its investments and shareholder activities align with sustainable environmental, social, and governance (ESG) practices, and what steps are taken to support long-term responsible growth?")
    company_answers["Business Partners_statement"] = st.text_area("What measures does your company take to ensure that its business partnerships align with sustainable practices across environmental, social, and governance (ESG) aspects, and how do you assess their commitment to these values?")
    company_answers["supply_statement"] = st.text_area("How does your company ensure sustainability across its supply chain, and what specific measures are taken to align with environmental, social, and governance (ESG) principles?")


    # Social and Community Engagement
    company_answers["NGO_statement"] = st.text_area("In what ways does your company collaborate with non-profit and NGO partners to foster sustainability, and how do you ensure these partnerships contribute positively to environmental, social, and governance (ESG) objectives?")
    company_answers["social_impact_partnerships"] = st.text_area(
        "Has your organization partnered with Social impact organizations, NGOs, or charities? If so, please list")

    company_answers["health_confidence"] = st.slider(
        "Rate your confidence in workplace health and safety measures (1-10):", 1, 10
    )
    company_answers["compliance_certifications"] = st.text_area("List any Compliance certifications received by the business")
    company_answers["awards_received"] = st.text_area(
        "List any Awards received by the business, upload pictures"
    )
    company_answers["selected_sdgs"] = st.multiselect(
        "Choose 3 SDGs that relate best to your organization", [
            "No Poverty", "Zero Hunger", "Good Health and Well-Being", "Quality Education",
            "Gender Equality", "Clean Water and Sanitation", "Affordable and Clean Energy",
            "Decent Work and Economic Growth", "Industry, Innovation and Infrastructure",
            "Reduced Inequality", "Sustainable Cities and Communities",
            "Responsible Consumption and Production", "Climate Action",
            "Life Below Water", "Life on Land", "Peace, Justice, and Strong Institutions",
            "Partnerships for the Goals"
        ]
    )

    # Management and Structure
    company_answers["roles"] = st.multiselect(
        "Please list the management structure of your company from the top down by selecting positions from the dropdowns below:",
        [
            "Chairman", "CEO", "COO", "CFO", "General Manager", "Department Head", "Employee"
        ]
    )

    # Additional Information
    company_answers["current_financial_year_month"] = st.text_input("Current financial year and month")
    company_answers["main_business_activity"] = st.text_area("Description of main business activity (product/service)")
    company_answers["info_flow_time"] = st.number_input(
        "Time for information flow to reach required employees (mins)", min_value=0.0, step=0.01
    )
    company_answers["rating"] = st.number_input(
        "Select your rating:"
)
    # Year of Opening Input
    # company_name = sl.text_input("Company name")
    # year_of_opening = sl.number_input("Year of Opening", min_value=1900, max_value=2100, step=1)

    if st.button("Submit"):
        company_code = str(uuid.uuid4())[:8]  # Generate unique code
        store_company_data(company_code, company_answers)
        st.success(f"Survey submitted! Share this code with your employees: {company_code}")
