import streamlit as st
import uuid

from firebase_config import store_company_data





# Display logo in the top-left corner
st.logo(image="images/GElogo.png", size="large", link="https://greenequities.org")

def run():
    st.header("Company Survey Form")
    # company_name = st.text_input("Company Name")
    company_answers = {}

    #General Company Infomation 
    company_answers["company_name"] =  st.text_input("Enter Company Name")
    company_answers["form_filler"] = st.text_input("Full name of the CEO")
    company_answers["CEO_message"] = st.text_area("Brief message from the CEO on sustainability and corporate responsibility")
    #company_answers["CEO_pic"] = st.file_uploader("Upload a image of the CEO ", type=["jpg", "jpeg", "png"])
    company_answers["current_financial_year_month"] = st.text_input("Todays date YYYY/MM/DD")
    company_answers["main_business_activity"] = st.text_area("Description of main business activity (product/service)")
    company_answers["website"] = st.text_input("Website")
    company_answers["email_address"] = st.text_input("Email address")
    company_answers["telephone"] = st.text_input("Telephone")
    company_answers["social_media"] = st.text_input("Social Media")
    company_answers["mission_statement"] = st.text_area("Mission statement")
    company_answers["year_of_opening"] = st.number_input("Year of Opening", min_value=1900, max_value=2100, step=1)
    company_answers["selected_locations"] = st.selectbox(
    "Select Main Office Location:", 
    ["Bengaluru", "Delhi", "Hyderabad", "Worli", "Malabar & Cumballa Hill", "Juhu", "Bandra Kurla Complex", "Nariman Point", 
     "Andheri", "Lower Parel", "Parel", "Bandra", "Santacruz", "Ghatkopar", "Thane", 
     "Goregaon", "Byculla", "Fort", "Borivali", "Jogeshwari", "Khar", "Malad", 
     "Vile Parle", "Chembur", "Dharavi", "Colaba", "Dadar", "Other"])
    
    company_answers["custom_location"] = st.text_input("If your location is not in the list, please specify other location")
    company_answers["industry"] = st.radio(
    "Select Industry:",
    [
        "Financial Services", "FMCG", "Healthcare", "IT", "Media",
        "Metal", "Pharma", "Realty", "Consumer Durables",
        "Oil and Gas", "Other"
    ]
)
    company_answers["csr_person"] = st.radio(
    "Does the entity have a specified Committee of the Board/Director responsible for corporate responsibility-related activities?", 
    ("Yes", "No"))

    company_answers["materiality_assessment"] = st.multiselect("Please select and rank the aspects that are most material to your organization",[
    "Climate Change Impact", 
        "Energy Management and Renewable Energy Usage", 
        "Carbon Emissions and Offsetting", 
        "Water and Waste Management", 
        "Biodiversity and Ecosystem Preservation", 
        "Employee Wellbeing and Safety", 
        "Diversity, Equity, and Inclusion (DEI)", 
        "Human Rights and Labor Practices", 
        "Community Engagement and Social Impact", 
        "Customer Privacy and Data Protection", 
        "Corporate Governance and Leadership", 
        "Compliance and Business Ethics",
    ])
 
    
    
    # Environmental 
    company_answers["carbon_credits_bought"] = st.number_input("Carbon credits bought (Co2 emissions)", min_value=0.0, step=0.01)
    company_answers["green_product_revenue"] = st.number_input("Green Product Revenue", min_value=0.0, step=0.01)
    company_answers["green_energy"] = st.number_input("Monthly Cost of Energy from Sustainable sources per month (Rs)", min_value=0.0, step=0.01)

    company_answers["primary_waste_generator"] = st.radio(
        "What is your companys primary waste generator:", ["Plastic Waste",
            "Food Waste",
            "Electronic Waste (e-waste)",
            "Fabric Scraps",
            "Scrap Metals",
            "Paper Waste",
            "Glass Waste",
            "Hazardous Chemicals or Substances",
            "Construction and Demolition Debris",
            "Packaging Waste"]

    )

    company_answers["waste_stance"] = st.text_area("Briefly describe your companys waste management practices. (Optional)")

    company_answers["compliant_laws"] = st.multiselect(
        "Is your entity compliant with the following environmental laws? Select all that apply:",
        [
            "The Water (Prevention and Control of Pollution) Act, 1974",
            "The Air (Prevention and Control of Pollution) Act, 1981",
            "The Environment (Protection) Act, 1986",
            "The Hazardous Waste (Management and Handling) Rules, 1989",
            "The Forest (Conservation) Act, 1980",
            "The Wildlife Protection Act, 1972",
            "The E-Waste (Management) Rules, 2016",
            "The Plastic Waste Management Rules, 2016",
            "The Bio-Medical Waste Management Rules, 2016",
            "The National Green Tribunal Act, 2010"
        ]
    )
    
    company_answers["company_stance_sustainability (Optional)"] = st.text_area(
        "Business current stance on environmental sustainability (100 words or less)"
    )
    company_answers["clean_tech_initiatives"] = st.text_area(
        "Has your company implemented any clean technologies or innovative processes to reduce emissions, waste, or improve resource efficiency? Briefly describe the initiative(s) and any measurable outcomes.")
    
    # Social Metrics

    #Employee Information
    company_answers["total_employees"] = st.number_input("Total number of Employees", min_value=0, step=1)
    company_answers["male_employees"] = st.number_input("Number of Male Employees", min_value=0, step=1)
    company_answers["female_employees"] = st.number_input("Number of Female employees", min_value=0, step=1)
    company_answers["differently_abled_workers"] = st.number_input("Differently abled workers", min_value=0, step=1)
    company_answers["internal_promotions"] = st.number_input("Number of internal promotions over the last 12 months")

    company_answers["employee_separations"] = st.number_input("Number of employee separations over the past 2 years?", min_value=0, step=1)
    company_answers["customer_feedback_score"] = st.slider(
        "Customer feedback score (using company feedback system or Google Business rating)", min_value=0, max_value=5, step=1)
    company_answers["customer_feedback"] = st.text_area("Describe the mechanisms in place to receive and respond to consumer complaints and feedback. (Optional)")
    
    company_answers["health_practices"] = st.multiselect(
    "Which of the following health practices does your business currently implement? Select all that apply.",
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

       # NGO Community Engagement
    company_answers["social_impact_partnerships"] = st.text_area(
        "Has your organization partnered with Social impact organizations, NGOs, or charities? If so, list them")

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
   
         
    # Financial and Operational Metrics
    company_answers["monthly_water_bill"] = st.number_input("What is the monthly Water Bill? (Rs)", min_value=0.0, step=0.01)
    company_answers["monthly_electricity_bill"] = st.number_input("What is the monthly Electricity cost? (Rs)", min_value=0.0, step=0.01)
    company_answers["monthly_profit"] = st.number_input("Average Monthly Profit (Rs)", min_value=0.0, step=0.01)
    company_answers["monthly_salary_costs"] = st.number_input("Monthly salary Costs (Rs)", min_value=0.0, step=0.01)
    company_answers["monthly_land_costs"] = st.number_input(
        "Monthly Land Costs (Office Rent, Storage facilities, Manufacturing facilities) (Rs)", min_value=0.0, step=0.01)
    company_answers["monthly_raw_material_costs"] = st.number_input(
        "Monthly costs of acquiring new raw material (if applicable)(Rs)", min_value=0.0, step=0.01)
    company_answers["total_yearly_revenue"] = st.number_input("Average Monthly Revenue (Rs)", min_value=0.0, step=0.01)
     
     
     # Supplier Information
    company_answers["all_time_suppliers"] = st.number_input("How many all-time suppliers have you had?", min_value=0, step=1)
    company_answers["remaining_suppliers"] = st.number_input("What is the Number of current suppliers?", min_value=0, step=1)
    
    
    
    company_answers["Anti_Corruption"] = st.multiselect("Which of the following anti-corruption measures does your business currently implement? Select all that apply." ,
    [
        "Formal Code of Ethics and Anti-Corruption Policy",
        "Secure Whistleblower Mechanism",
        "Third-Party Due Diligence Process",
        "Regular Anti-Corruption Training for Employees",
        "Clear Gift and Hospitality Guidelines",
        "Conflict of Interest Disclosure System",
        "Transparent Financial Record-Keeping",
        "Regular (Quarterly or Annually) Internal Audits for Corruption Risks",
        "Anti-Corruption Clauses in Vendor/Partner Contracts",
        "Leadership Commitment to Ethical Standards"
    ]                                                
)

    company_answers["data_comp"] = st.multiselect(
    "Which of the following data protection and tech-related laws is your business compliant with? Select all that apply:",
    [
        "Digital Personal Data Protection Act (DPDP Act), 2023",
        "Information Technology Act, 2000 (IT Act)",
        "Information Technology (Reasonable Security Practices and Procedures and Sensitive Personal Data or Information) Rules, 2011",
        "Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021",
        "Consumer Protection (E-Commerce) Rules, 2020",
        "The Aadhaar Act, 2016",
        "The Payment and Settlement Systems Act, 2007",
        "The Companies Act, 2013",
        "Reserve Bank of India (RBI) Guidelines on Cyber Security Framework",
        "Telecom Regulatory Authority of India (TRAI) Guidelines"
    ]
)

    company_answers["anti_corruption_policy_link"] = st.text_input("Anti-corruption policy link (if available)")
    company_answers["Investor/Shareholder_statement"] = st.text_area("How does your company ensure that its investments and shareholder activities align with sustainable business practices, and long-term responsible growth? (Optional)" )
    company_answers["supply_statement"] = st.text_area("How does your company ensure sustainability and ethical practices across its supply chain (Optional)")


 

    company_answers["compliance_certifications"] = st.text_area("List any Compliance certifications received by the business (Optional)")
    company_answers["awards_received"] = st.text_area(
        "List any Awards received by the business (Optional)"
    )


    if st.button("Submit"):
        form_valid = True  
        if company_answers["monthly_water_bill"] == 0.0:
            st.error("Please enter your monthly water bill.")
            form_valid = False
        if company_answers["monthly_electricity_bill"] == 0.0:
            st.error("Please enter your monthly electricity bill.")
            form_valid = False
        if company_answers["monthly_profit"] == 0.0:
            st.error("Please enter your average monthly profit.")
            form_valid = False
        if company_answers["monthly_salary_costs"] == 0.0:
            st.error("Please enter your monthly salary costs.")
            form_valid = False
        if company_answers["monthly_land_costs"] == 0.0:
            st.error("Please enter your monthly land costs.")
            form_valid = False
        if company_answers["monthly_raw_material_costs"] == 0.0:
            st.error("Please enter your monthly raw material costs.")
            form_valid = False
        if company_answers["total_yearly_revenue"] == 0.0:
            st.error("Please enter your total monthly revenue.")
            form_valid = False
        if company_answers["all_time_suppliers"] == 0:
            st.error("Please enter the number of all-time suppliers.")
            form_valid = False
        if company_answers["remaining_suppliers"] == 0:
            st.error("Please enter the number of current suppliers.")
            form_valid = False
        if company_answers["total_employees"] == 0:
            st.error("Please enter the total number of employees.")
            form_valid = False
        if company_answers["male_employees"] == 0:
            st.error("Please enter the number of male employees.")
            form_valid = False
        if company_answers["female_employees"] == 0:
            st.error("Please enter the number of female employees.")
            form_valid = False
        if company_answers["differently_abled_workers"] == 0:
            st.error("Please enter the number of differently abled workers.")
            form_valid = False
        if company_answers["internal_promotions"] == 0:
            st.error("Please enter the number of internal promotions in the last 12 months.")
            form_valid = False
        if company_answers["employee_separations"] == 0:
            st.error("Please enter the number of employee separations in the past 2 years.")
            form_valid = False
        if company_answers["carbon_credits_bought"] == 0.0:
            st.error("Please enter the amount of carbon credits bought.")
            form_valid = False
        if company_answers["green_product_revenue"] == 0.0:
            st.error("Please enter your green product revenue.")
            form_valid = False
        if company_answers["green_energy"] == 0.0:
            st.error("Please enter your monthly cost for green energy.")
            form_valid = False
            
        if form_valid:
            st.success("All required fields are filled. Submitting form...")
            company_code = str(uuid.uuid4())[:8]
            store_company_data(company_code, company_answers)
            st.success(f"Survey submitted! Share this code with your employees: {company_code} — ask them to fill out the Employee survey (Min 5 Employees)")