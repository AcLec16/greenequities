import openai
import streamlit as st

def extract_all_esg_fields(report):
    fields = {
        "Company Name": report.get("company_name", "N/A"),
        "Form Filler": report.get("form_filler", "N/A"),
        "CEO Message": report.get("CEO_message", "N/A"),
        "Financial Year Month": report.get("current_financial_year_month", "N/A"),
        "Main Business Activity": report.get("main_business_activity", "N/A"),
        "Website": report.get("website", "N/A"),
        "Email": report.get("email_address", "N/A"),
        "Telephone": report.get("telephone", "N/A"),
        "Social Media": report.get("social_media", "N/A"),
        "Mission Statement": report.get("mission_statement", "N/A"),
        "Year of Opening": report.get("year_of_opening", "N/A"),
        "CSR Person": report.get("csr_person", "N/A"),
        "Materiality Assessment": report.get("materiality_assessment", "N/A"),
        "Anti-Corruption Policy Link": report.get("anti_corruption_policy_link", "N/A"),
        "Value-Based Resource Efficiency": report.get("value_based_resource_efficiency_s", "N/A"),
        "Environmental Laws Compliance": report.get("Enviroment_Laws_Compliance", "N/A"),
        "Environmental Laws List": ", ".join(report.get("Enviroment_Laws_Compliance_list", [])),
        "Sustainability Stance": report.get("sustainability_stance", "N/A"),
        "Green Product Revenue %": report.get("green_product_revenue_percentage", "N/A"),
        "Green Energy Score": report.get("green_energy_score", "N/A"),
        "Phone Charges": report.get("phone_charges", "N/A"),
        "Emissions Rating": report.get("emissions_rating", "N/A"),
        "Bath Tubs Full": report.get("bath_tubs_full", "N/A"),
        "Water Usage Rating": report.get("water_usage_rating", "N/A"),
        "Flight Emissions Rating": report.get("flight_emissions_rating", "N/A"),
        "Distance to Moon": report.get("distance_to_the_moon", "N/A"),
        "Travel Emissions Rating": report.get("travel_emissions_rating", "N/A"),
        "Times Around Earth": report.get("times_around_earth", "N/A"),
        "Total Carbon": report.get("total_carbon", "N/A"),
        "Carbon Credit Rating": report.get("carbon_credit_rating", "N/A"),
        "Average Energy Score": report.get("average_energy_score", "N/A"),
        "Waste Value": report.get("waste_value", "N/A"),
        "Selected SDGs": report.get("selected_sdgs", "N/A"),
        "SDG Image Paths": report.get("sdg_image_paths", "N/A"),
        "Leader Confidence": report.get("leader_confidence", "N/A"),
        "Avg Culture Satisfaction": report.get("average_culture_satisfaction", "N/A"),
        "Employee Inclusion": report.get("employee_inclusion", "N/A"),
        "Diversity Index": report.get("diversity_index", "N/A"),
        "Compensation Fairness": report.get("employee_compensation_fairness", "N/A"),
        "Work Hours": report.get("work_hours", "N/A"),
        "Tenure Promotion Index": report.get("tenure_promotion_index", "N/A"),
        "Health Satisfaction Index": report.get("health_satisfaction_index", "N/A"),
        "Turnover Rating": report.get("turnover_rating", "N/A"),
        "Wellbeing Training Index": report.get("wellbeing_training_index", "N/A"),
        "Job Training": report.get("employee_job_related_training", "N/A"),
        "Data Law Compliance": report.get("data_law_compliance", "N/A"),
        "Data Law List": ", ".join(report.get("data_law_compliance_list", [])),
        "Customer Feedbacks": report.get("Customer_feedbacks", "N/A"),
        "Customer Statement": report.get("customer_statement", "N/A"),
        "NGO Statement": report.get("NGO_statement", "N/A"),
        "Social Impact Partnerships": report.get("social_impact_partnerships", "N/A"),
        "Supplier Retention Score": report.get("supplier_retention_score", "N/A"),
        "Supply Statement": report.get("supply_statement", "N/A"),
        "Investor/Shareholder Statement": report.get("Investor/Shareholder_statement", "N/A"),
        "Sector Growth Rating": report.get("Sector_growth_Rating", "N/A"),
        "Awards": report.get("awards_received", "N/A"),
        "Certifications": report.get("compliance_certifications", "N/A"),
        "Anti-Corruption Score": report.get("Anti_Corruption_score", "N/A"),
        "Anti-Corruption List": ", ".join(report.get("Anti_Corruption_score_list", [])),
        "Sector Volatility": report.get("sector_volatility", "N/A"),
        "Information Flow Efficiency": report.get("infomation_flow_efficency", "N/A"),
        "Geopolitical Risk Index": report.get("Geopolitical_Risk_Index", "N/A"),
        "India News Sentiment": report.get("India_News_sentiment", "N/A"),
        "India Internet Sentiment": report.get("India_Internet_sentiment", "N/A"),
        "Market Uncertainty": report.get("Market_Uncertainty", "N/A"),
        "Corporate Structure": report.get("cooperate_stucture", "N/A"),
        "Profit to Revenue Ratio": report.get("profit_to_revenue_ratio", "N/A"),
        "Business Location Rating": report.get("buissnes_location_rating", "N/A"),
        "Selected Locations": report.get("selected_locations", "N/A"),
        "Workplace Average": report.get("workplace_average", "N/A"),
        "Strategic Risk": report.get("strategic_risk", "N/A"),
        "Compliance Risk": report.get("Compliance_and_Regulatory_Risk", "N/A"),
        "Financial Risk": report.get("Financial_Risk", "N/A"),
        "Operational Risk": report.get("Operational_Risk", "N/A"),
        "Total Environmental Score": report.get("total_environment", "N/A"),
        "Total Social Score": report.get("total_social", "N/A"),
        "Total Governance Score": report.get("total_governance", "N/A"),
    }
    return fields

def create_prompt_from_report_fields(fields):
    prompt = "Below is the report;\n\n"
    for key, value in fields.items():
        prompt += f"{key}: {value}\n"
    return prompt

def get_esg_ai_recommendations(report):
    client = openai.OpenAI(api_key=st.secrets["openai"])
    prompt_text = create_prompt_from_report_fields(report)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": """
You are a sustainability consultant specialized in Indian startups.

Below is ESG data from a startup's ESG report. Based on this, do the following in **valid Python dictionary** format (not JSON):

1. Briefly diagnose the startup's Environmental, Social, and Governance performance.
2. Provide a short analysis (1-2 lines each) for each ESG category: "environmental", "social", and "governance".
3. Provide 8 to 10 realistic, clear, and actionable recommendations for improving their ESG performance. These must be tailored for a startup operating in India.

Respond strictly in the following JSON format:

{
  'diagnosis': '<short paragraph about overall ESG status>',
  'analysis': {
    'environmental': '<1-2 lines>',
    'social': '<1-2 lines>',
    'governance': '<1-2 lines>'
  },
  'suggestions': [
    '<suggestion 1>',
    '<suggestion 2>',
    # ... up to 10 suggestions
  ]
}
"""
            },
            {"role": "user", "content": prompt_text}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content
