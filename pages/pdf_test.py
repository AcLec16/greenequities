from fpdf import FPDF
import os

# Custom PDF class for generating reports
class PDF(FPDF):
    
    
    def add_cover_page(self, company_name):
        self.add_page()

        # Add a background image
        self.image("/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/back1.png", x=0, y=0, w=self.w, h=self.h)
        # Add title text
        self.set_xy(5, 50)  # Adjust the X position slightly to the left
        self.set_font('Helvetica', 'B', 44)  # Increase font size for larger text
        self.set_text_color(0, 51, 102)  # Navy blue
        self.multi_cell(self.w - 10, 20, 'Environmental, Social, \nGovernance Report', align='C')  # Reduce margins to stretch wider


        # Add company name
        self.set_xy(10, 120)
        self.set_font('Helvetica', 'B', 30)
        self.set_text_color(0, 0, 0)  # Blue
        self.cell(self.w - 20, 15, company_name, 0, 1, 'C')

        # Add subtext
        self.set_xy(10, 160)
        self.set_font('Helvetica', 'I', 20)
        self.set_text_color(0, 0, 0)  # Gray
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
        self.image("/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/GElogo.png", x=image_x, y=image_y, w=image_width, h=image_height)


    def add_section_title(self, title):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(0, 0, 0)
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
def generate_pdf(report):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)  # Enable auto page break
    
    pdf.add_cover_page("EcoSphere Solutions Pvt. Ltd.")
    
    pdf.add_page()
    
    
    # Company Details
    pdf.add_section_title("Company Details")
    pdf.add_text("Company Name", report["company_name"])
    pdf.add_text("Financial Year (Month)", report["current_financial_year_month"])
    pdf.add_text("Main Business Activity", report["main_business_activity"])
    pdf.add_text("Website", report["website"])
    pdf.add_text("Email Address", report["email_address"])
    pdf.add_text("Telephone", report["telephone"])
    pdf.add_text("Social Media", report["social_media"])
    pdf.add_text("Mission Statement", report["mission_statement"])
    pdf.add_text("Year of Opening", report["year_of_opening"])
    pdf.add_text("Selected Locations", ", ".join(report["selected_locations"]))

    # Add a new page for environment data
    pdf.add_page()
    pdf.add_section_title("Environment Data")
    pdf.add_text("Value-Based Resource Efficiency", report["value_based_resource_efficiency_s"])
    pdf.add_text("Environment Laws Compliance", report["Enviroment_Laws_Compliance"])
    pdf.add_text("Sustainability Stance", report["sustainability_stance"])
    pdf.add_text("Green Product Revenue Percentage", report["green_product_revenue_percentage"])
    pdf.add_text("Green Energy Score", report["green_energy_score"])
    pdf.add_text("Phone Charges", report["phone_charges"])
    pdf.add_text("Emissions Rating", report["emissions_rating"])
    
    pdf.add_page()
    background_image_path = "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/backlogoenv.png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    pdf.add_text("Bath Tubs Full", report["bath_tubs_full"])
    pdf.add_text("Water Usage Rating", report["water_usage_rating"])
    pdf.add_text("Flight Emissions Rating", report["flight_emissions_rating"])
    pdf.add_text("Distance to the Moon", report["distance_to_the_moon"])
    pdf.add_text("Travel Emissions Rating", report["travel_emissions_rating"])
    pdf.add_text("Times Around Earth", report["times_around_earth"])
    pdf.add_text("Total Carbon", report["total_carbon"])
    pdf.add_text("Carbon Credit Rating", report["carbon_credit_rating"])
    pdf.add_text("Selected SDGs", ", ".join(report["selected_sdgs"]))
# Adding images for the selected SDGs
    # y_offset = pdf.get_y() + 10  # Start placing images below the last text
    # x_start = 10  # X-coordinate for images
    # image_width = 40  # Width of each image
    # image_height = 40  # Height of each image
    # space_between = 10  # Space between images

    # page_height = pdf.h - pdf.t_margin - pdf.b_margin  # Usable page height

    # for index, image_path in enumerate(report["sdg_image_paths"]):
    #     if os.path.exists(image_path):
    #         x_position = x_start + (index % 4) * (image_width + space_between)
    #         y_position = y_offset + (index // 4) * (image_height + space_between)

    #         # Add a new page if necessary
    #         if y_position + image_height > page_height:
    #             pdf.add_page()
    #             y_offset = pdf.t_margin
    #             y_position = y_offset + (index // 4) * (image_height + space_between)

    #         pdf.image(image_path, x=x_position, y=y_position, w=image_width, h=image_height)
    #     else:
    #         print(f"Warning: Image file not found - {image_path}")


    # Add a new page for social and governance data
    pdf.add_page()
    background_image_path = "/Users/a.chhawchharia.26/Documents/GitHub/greenequities/pages/images/black_back.png"
    pdf.image(background_image_path, x=0, y=0, w=pdf.w, h=pdf.h)  # Full-page background
    pdf.add_section_title("Social and Governance Data")
    pdf.add_text("Average Culture Satisfaction", report["average_culture_satisfaction"])
    pdf.add_text("Employee Inclusion", report["employee_inclusion"])
    pdf.add_text("Diversity Index", report["diversity_index"])
    pdf.add_text("Employee Compensation Fairness", report["employee_compensation_fairness"])
    pdf.add_text("Work Hours", report["work_hours"])
    pdf.add_text("Tenure Promotion Index", report["tenure_promotion_index"])
    pdf.add_text("Health Satisfaction Index", report["health_satisfaction_index"])
    pdf.add_text("Turnover Rating", report["turnover_rating"])
    pdf.add_text("Wellbeing Training Index", report["wellbeing_training_index"])
    pdf.add_text("Employee Job-Related Training", report["employee_job_related_training"])
    pdf.add_text("Supplier Retention Score", report["supplier_retention_score"])

    # Add additional sections as needed
    pdf.add_page()


    # Adding content on top of the background
    pdf.add_section_title("Additional Information")
    pdf.add_text("Customer Feedbacks", report["Customer_feedbacks"])
    pdf.add_text("Customer Statement", report["customer_statement"])
    pdf.add_text("NGO Statement", report["NGO_statement"])
    pdf.add_text("Social Impact Partnerships", report["social_impact_partnerships"])
    pdf.add_text("Sector Growth Rating", report["Sector_growth_Rating"])
    pdf.add_text("Awards Received", report["awards_received"])
    pdf.add_text("Compliance Certifications", report["compliance_certifications"])
    pdf.add_text("Anti-Corruption Score", report["Anti_Corruption_score"])
    
    # Adding other sections
    pdf.add_text("Information Flow Efficiency", report["infomation_flow_efficency"])
    pdf.add_text("Geopolitical Risk Index", report["Geopolitical_Risk_Index"])
    pdf.add_text("India News Sentiment", report["India_News_sentiment"])
    pdf.add_text("India Internet Sentiment", report["India_Internet_sentiment"])
    pdf.add_text("Market Uncertainty", report["Market_Uncertainty"])
    pdf.add_text("Corporate Structure", report["cooperate_stucture"])
    pdf.add_text("Profit to Revenue Ratio", report["profit_to_revenue_ratio"])
    pdf.add_text("Business Location Rating", report["buissnes_location_rating"])
    pdf.add_text("Workplace Average", report["workplace_average"])

    # Adding risk and other sections
    pdf.add_text("Strategic Risk", report["strategic_risk"])
    pdf.add_text("Compliance and Regulatory Risk", report["Compliance_and_Regulatory_Risk"])
    pdf.add_text("Financial Risk", report["Financial_Risk"])
    pdf.add_text("Operational Risk", report["Operational_Risk"])

    # Environmental, Social, Governance (ESG) Scores
    pdf.add_text("Total Environment", report["total_environment"])
    pdf.add_text("Total Social", report["total_social"])
    pdf.add_text("Total Governance", report["total_governance"])

    # Save the PDF
    pdf_file = "ESG_Report.pdf"
    pdf.output(pdf_file)
    return pdf_file


# Sample data for testing
sample_report = {
    "company_name": "EcoSphere Solutions Pvt. Ltd.",
    "current_financial_year_month": "2025/01/11",
    "main_business_activity": "Manufacturing and distribution of eco-friendly packaging solutions.",
    "website": "www.ecospheresolutions.com",
    "email_address": "contact@ecospheresolutions.com",
    "telephone": "+91-9876543210",
    "social_media": "LinkedIn: EcoSphere Solutions Instagram: @ecospheresolutions",
    "mission_statement": "To revolutionize packaging by offering sustainable, biodegradable, and cost-effective solutions that reduce environmental harm.",
    "year_of_opening": 2015,
    "selected_locations": ["Bengaluru"],
    "value_based_resource_efficiency_s": "Value-Based Resource Efficiency 5 for every 1 of stressed resources",
    "Enviroment_Laws_Compliance": 4,
    "sustainability_stance": "We are committed to innovating sustainable packaging solutions that minimize environmental impact and support circular economies.",
    "green_product_revenue_percentage": 4.2,
    "green_energy_score": 6.67,
    "phone_charges": "You could charge your phone 75,000,000 times! Based on the electricity usage of 15,000 kWh.",
    "emissions_rating": 0.24684210526315775,
    "bath_tubs_full": "The monthly water bill equates to approximately 993 bath tubs full of water.",
    "water_usage_rating": 4.734893742621016,
    "flight_emissions_rating": -0.059941116556549545,
    "distance_to_the_moon": "The total flight time for all employees would cover approximately 1216.44 of the distance from Earth to the Moon.",
    "travel_emissions_rating": 4.746029960366605,
    "times_around_earth": "The total travel distance for all employees, with an average travel distance of 21.5 km per employee, would cover approximately 43.77 times around the Earth.",
    "total_carbon": 1372574.32,
    "carbon_credit_rating": 1,
    "average_culture_satisfaction": 6.25,
    "employee_inclusion": 5.75,
    "selected_sdgs": [
        "Quality Education",
        "No Poverty",
        "Decent Work and Economic Growth"
    ],
    "diversity_index": 4,
    "employee_compensation_fairness": 7.5,
    "work_hours": 5,
    "tenure_promotion_index": 4,
    "health_satisfaction_index": 7.5,
    "turnover_rating": 4.5,
    "wellbeing_training_index": 8.9,
    "employee_job_related_training": 8.75,
    "supplier_retention_score": 5.25,
    "Customer_feedbacks": "Customer service for eco-friendly packaging has been responsive and proactive.",
    "customer_statement": "We are committed to improving the quality of our products and services.",
    "NGO_statement": "Working with local NGOs to support environmental causes.",
    "social_impact_partnerships": "Partnered with the local sustainability nonprofit for a waste-reduction campaign.",
    "Sector_growth_Rating": 4.5,
    "awards_received": "Winner of the Green Business Award in 2023.",
    "compliance_certifications": "ISO 14001:2015 certified.",
    "Anti_Corruption_score": 7.8,
    "infomation_flow_efficency": 5.6,
    "Geopolitical_Risk_Index": 3.8,
    "India_News_sentiment": 5.7,
    "India_Internet_sentiment": 5.1,
    "Market_Uncertainty": 7.2,
    "cooperate_stucture": "Flexible organizational structure with regular cross-department collaboration.",
    "profit_to_revenue_ratio": 4.5,
    "buissnes_location_rating": 6.3,
    "workplace_average": 7.0,
    "strategic_risk": 6.5,
    "Compliance_and_Regulatory_Risk": 7.2,
    "Financial_Risk": 5.3,
    "Operational_Risk": 5.9,
    "total_environment": 7.8,
    "total_social": 7.5,
    "total_governance": 8.1
}

# Generate and save the PDF
pdf_file = generate_pdf(sample_report)
print(f"Report generated and saved as {pdf_file}")
