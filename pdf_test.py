from fpdf import FPDF
import os

# Custom PDF class for generating reports
class PDF(FPDF):
    
    
    def add_cover_page(self, company_name):
        self.add_page()

        # Add a background image
        self.image("images/Untitled design (24).png", x=0, y=0, w=self.w, h=self.h)
        # Add title text
        self.set_xy(5, 30)  # Adjust the X position slightly to the left
        self.set_font('Helvetica', 'B', 44)  # Increase font size for larger text
        self.set_text_color(255, 255, 255)  # Navy blue
        self.multi_cell(self.w - 10, 20, 'Environmental, Social, \nGovernance Report', align='C')  # Reduce margins to stretch wider


        # Add company name
        self.set_xy(10, 95)
        self.set_font('Helvetica', 'B', 30)
        self.set_text_color(255, 255, 255)  # Blue
        self.cell(self.w - 20, 15, company_name, 0, 1, 'C')

        # Add subtext
        self.set_xy(10, 130)
        self.set_font('Helvetica', 'I', 20)
        self.set_text_color(255, 255, 255)  # Gray
        self.cell(self.w - 20, 10, 'ESG metrics and company performance', 0, 1, 'C')


    def footer(self):
        # Position to the bottom of the page
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
        

        # Add image to bottom-right corner of every page
        image_width = 25  # Width of the image
        image_height = 25  # Height of the image
        image_x = self.w - image_width - 10  # X position (right margin)
        image_y = self.h - image_height - 10  # Y position (bottom margin)
        
        # Place the image (bottom-right corner)
        self.image("images/GElogo.png", x=image_x, y=image_y, w=image_width, h=image_height)


    def add_section_title(self, title):
        self.set_font('Helvetica', 'B', 20)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def add_text(self, label, value, max_width=180):
        self.set_font('Helvetica', '', 12)
        self.set_text_color(255, 255, 255)
        self.multi_cell(0, 10, f'{label}: {value}', border=0, align='L')  # multi_cell for wrapping text
        self.ln(3)

    def add_box(self, title, value):
        self.set_font('Helvetica', '', 12)
        self.set_fill_color(240, 240, 240)  # Light gray background
        self.multi_cell(0, 10, f'{title}: {value}', border=1, align='L', fill=True)
        self.ln(5)
    

# Function to generate the PDF report
def generate_pdf(report, suggestion):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)  # Enable auto page break
    
    pdf.add_cover_page(report["company_name"])
    
    pdf.add_page()
    background_image_path = "images/pg. 01 (1).png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    
    pdf.add_page()
    background_image_path = "images/black_back.png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    pdf.add_section_title("Message from the CEO")
    pdf.set_y(40)
    pdf.add_text("Message", report["CEO_message"])
    pdf.add_text("Regards: ", report["form_filler"])
 
    about = "This ESG Report from Green Equities offers an integrated snapshot of your company's performance across environmental, social, and governance dimensions. It consolidates essential metrics and data points to reflect your sustainability practices, risk management, and corporate responsibility, providing a clear picture of your current ESG status. Designed to support internal review and facilitate transparent communication with stakeholders, the report demonstrates your commitment to sustainable business practices and regulatory compliance. It serves as a vital resource for understanding how your operations align with ESG principles and guides your companys ongoing efforts toward long-term, responsible growth."
    pdf.add_page()
    background_image_path = "images/black_back.png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    pdf.add_section_title("About the report")
    pdf.set_y(40)
    pdf.add_text("About the report", about)

    pdf.add_page()
    background_image_path = "images/black_back.png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    pdf.add_section_title("Executive Summary")
    pdf.add_text("Financial Year (Month)", report["current_financial_year_month"])
    pdf.add_text("Company Name", report["company_name"])
    pdf.add_text("Mission Statement", report["mission_statement"])
    pdf.add_text("Year of Opening", report["year_of_opening"])
    pdf.add_text("Main Business Activity", report["main_business_activity"])
    pdf.add_text("Selected Locations", report["selected_locations"])


    # Company Details
    pdf.add_page()
    background_image_path = "images/black_back.png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    pdf.set_y(20)
    pdf.add_section_title("Corporate Overview")
    pdf.set_y(40)
    pdf.add_text("Website", report["website"])
    pdf.add_text("Email Address", report["email_address"])
    pdf.add_text("Telephone", report["telephone"])
    pdf.add_text("Social Media", report["social_media"])
    
    pdf.add_page()
    background_image_path = "images/black_back.png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    pdf.set_y(30)
    pdf.add_text("Company sustainability", report["sustainability_stance"])
    materiality_list = report["materiality_assessment"]
    formatted_materiality = "\n".join([f"{i + 1}. {item}" for i, item in enumerate(materiality_list)])
    pdf.add_text("Materiality Assessment","\n" + formatted_materiality)

    # Add a new page for environment data
    pdf.add_page()
    background_image_path = "images/black_back.png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    pdf.set_y(20)
    pdf.add_section_title("Environmental Performance")
    pdf.set_y(40)
    pdf.add_text("Value-Based Resource Efficiency", report["value_based_resource_efficiency_s"])
    pdf.add_text("Environment Laws Compliance", report["Enviroment_Laws_Compliance_list"])
    pdf.add_text("Green Product Revenue Percentage", report["green_product_revenue_percentage"])
    pdf.add_text("Green Energy Score", report["green_energy_score"])
    pdf.add_text("Electricity Rating", report["emissions_rating"])
    pdf.add_text("Phone Charges", report["phone_charges"])
    env_list = report["Enviroment_Laws_Compliance_list"]
    formatted_env = "\n".join([f"{i + 1}. {item}" for i, item in enumerate(env_list)])
    pdf.add_text("Enviromental Law compliance", "\n" + formatted_env)
    
    pdf.add_page()
    background_image_path = "images/pg. 01 (3).png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    pdf.add_text("Water Usage Rating", report["water_usage_rating"])
    pdf.add_text("Bath Tubs Full", report["bath_tubs_full"])
    pdf.add_text("Flight Emissions Rating", report["flight_emissions_rating"])
    pdf.add_text("Distance to the Moon", report["distance_to_the_moon"])
    pdf.add_text("Travel Emissions Rating", report["travel_emissions_rating"])
    pdf.add_text("Times Around Earth", report["times_around_earth"])
    pdf.add_text("Total Carbon", report["total_carbon"])
    pdf.add_text("Carbon Credit Rating", report["carbon_credit_rating"])
    pdf.add_text("Selected SDGs", ", ".join(report["selected_sdgs"]))
# Adding images for the selected SDGs
    y_offset = pdf.get_y() + 10  # Start placing images below the last text
    x_start = 10  # X-coordinate for images
    image_width = 40  # Width of each image
    image_height = 40  # Height of each image
    space_between = 10  # Space between images

    page_height = pdf.h - pdf.t_margin - pdf.b_margin  # Usable page height

    for index, image_path in enumerate(report["sdg_image_paths"]):
        if os.path.exists(image_path):
            x_position = x_start + (index % 4) * (image_width + space_between)
            y_position = y_offset + (index // 4) * (image_height + space_between)

            # Add a new page if necessary
            if y_position + image_height > page_height:
                pdf.add_page()
                y_offset = pdf.t_margin
                y_position = y_offset + (index // 4) * (image_height + space_between)

            pdf.image(image_path, x=x_position, y=y_position, w=image_width, h=image_height)
        else:
            print(f"Warning: Image file not found - {image_path}")


    # Add a new page for social and governance data
    pdf.add_page()
    background_image_path = "images/Untitled design (22).png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    pdf.set_y(20)
    pdf.add_section_title("Social Sustainability")
    pdf.set_y(45)
    pdf.add_text("Average Culture Satisfaction", report["average_culture_satisfaction"])
    pdf.add_text("Employee Inclusion", report["employee_inclusion"])
    pdf.add_text("Diversity Index", report["diversity_index"])
    pdf.add_text("Employee Compensation Fairness", report["employee_compensation_fairness"])
    pdf.add_text("Work Hours", report["work_hours"])
    pdf.add_text("Career Growth", report["tenure_promotion_index"])
    pdf.add_text("Health & Safety", report["health_satisfaction_index"])
    pdf.add_text("Employee Turnover Rating", report["turnover_rating"])
    pdf.add_text("Employee Wellbeing Development Index", report["wellbeing_training_index"])
    pdf.add_text("Employee Job-Related Development", report["employee_job_related_training"])
    pdf.add_text("Workplace Average", report["workplace_average"])


    # Add additional sections as needed
    pdf.add_page()
    background_image_path = "images/Untitled design (23).png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    # Adding content on top of the background
    pdf.set_y(20)
    pdf.add_section_title("Stakeholder engagement")
    pdf.set_y(50)
    pdf.add_text("Customer Feedbacks", report["Customer_feedbacks"])
    pdf.add_text("Customer Statement", report["customer_statement"])
    pdf.add_text("Social Impact Partnerships", report["social_impact_partnerships"])
    pdf.add_text("Supplier Retention Score", report["supplier_retention_score"])
    pdf.add_text("Supplier Statement", report["supply_statement"])
    pdf.add_text("Investor/Shareholder Statement", report["Investor/Shareholder_statement"])

    pdf.add_page()
    background_image_path = "images/black_back.png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    pdf.set_y(20)
    pdf.add_section_title("Leadership and Governance")
    pdf.set_y(40)
    # Adding other sections
    pdf.add_text("Corporate Structure", report["cooperate_stucture"]) 
    pdf.add_text("Information Flow Efficiency", report["infomation_flow_efficency"])
    pdf.add_text("Profit to Revenue Ratio", report["profit_to_revenue_ratio"])
    pdf.add_text("Business Location Rating", report["buissnes_location_rating"])
    pdf.add_text("Awards Received", report["awards_received"])
    
    pdf.add_page()
    background_image_path = "images/black_back.png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    pdf.set_y(20)
    pdf.add_section_title("Business Compliance")
    pdf.set_y(40)
    pdf.add_text("Compliance Certifications", report["compliance_certifications"])
    pdf.add_text("Anti-Corruption Score", report["Anti_Corruption_score"])
    soc_list = report["Anti_Corruption_score_list"]
    formatted_soc = "\n".join([f"{i + 1}. {item}" for i, item in enumerate(soc_list)])
    pdf.add_text("Anti-Corruption Law compliance", "\n" +  formatted_soc)
    pdf.add_text("Anti-Corruption Policy link", report["anti_corruption_policy_link"])
    data_list = report["data_law_compliance_list"]
    formatted_data = "\n".join([f"{i + 1}. {item}" for i, item in enumerate(data_list)])
    pdf.add_text("Data and Technology Law compliance", "\n" + formatted_data)

    pdf.add_page()
    background_image_path = "images/black_back.png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    pdf.set_y(20)
    pdf.add_section_title("Market Sentiment & Sector Growth")
    pdf.set_y(40)
    pdf.add_text("Sector Growth Rating", report["Sector_growth_Rating"])
    pdf.add_text("Sector Volatility Rating", report["sector_volatility"])


    # Adding risk and other sections
    pdf.add_page()
    background_image_path = "images/black_back.png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    pdf.set_y(20)
    pdf.set_font("Arial", size=26)
    pdf.add_section_title("Final Scores")
    pdf.set_y(50)
    pdf.add_text("Strategic Risk", report["Strategic_risk"])
    pdf.add_text("Compliance and Regulatory Risk", report["Compliance_and_Regulatory_Risk"])
    pdf.add_text("Financial Risk", report["Financial_Risk"])
    pdf.add_text("Operational Risk", report["Operational_Risk"])

    # Environmental, Social, Governance (ESG) Scores
    pdf.add_text("Total Environment", report["total_environment"])
    pdf.add_text("Total Social", report["total_social"])
    pdf.add_text("Total Governance", report["total_governance"])

    # AI Recommendations
    pdf.add_page()
    background_image_path = "images/pg. 01 (3).png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)

    # Section title
    pdf.set_y(20)
    pdf.add_section_title("The ESG Solutions and Recommendations")

    # ESG Diagnosis and Analysis
    pdf.set_y(40)
    pdf.add_text("Intelligent Assessment", suggestion["diagnosis"])
    pdf.add_text("Environmental Analysis", suggestion["analysis"]["environmental"])
    pdf.add_text("Social Analysis", suggestion["analysis"]["social"])
    pdf.add_text("Governance Analysis", suggestion["analysis"]["governance"])
    
    pdf.add_page()
    background_image_path = "images/pg. 01 (3).png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)
    # Section title
    pdf.set_y(20)
    # Suggestions
    pdf.add_section_title("Improvement Insights")
    for i, text in enumerate(suggestion["suggestions"], start=1):
        pdf.add_text(f"Suggestion {i}", text)


 
    pdf.add_page()
    background_image_path = "images/pg. 01 (3).png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)

    # Set the font size smaller
    pdf.set_font("Arial", size=8)

    # Add section title
    pdf.add_section_title("Risk Disclaimer")

    # Add the disclaimer text
    disclaimer_text = (
        "The recommendations and diagnostic scores provided in this report by Green Equities are based on our best judgment and the information available at the time of publication. "
        "While we strive for accuracy and thoroughness, we make no representations or warranties regarding the completeness, reliability, or suitability of the information contained herein. "
        "The recommendations should be considered as general guidance and not as specific financial advice. Users are encouraged to conduct their own due diligence and consult with qualified financial professionals before making any investment decisions based on the insights presented. "
        "Green Equities disclaims any liability for losses or damages incurred as a result of using or relying on the information, recommendations, or diagnostic scores provided in this report. "

    )
    pdf.add_text("Risk Disclaimer", disclaimer_text) 

    # Save the PDF
    pdf_file = "ESG_Report.pdf"
    pdf.output(pdf_file)
    return pdf_file
