from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(0, 102, 204)  # Blue color for the header
        self.cell(0, 10, 'ESG Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

        # Add image to bottom-right corner of every page
        image_width = 25
        image_height = 25
        image_x = self.w - image_width - 10
        image_y = self.h - image_height - 10
        self.image("logo1.png", x=image_x, y=image_y, w=image_width, h=image_height)


    def add_section_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(0, 0, 0)  # Black color for section titles
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def add_dynamic_text(self, label, value):
        self.set_font('Arial', '', 12)

        # Set black color for the label
        self.set_text_color(0, 0, 0)  
        label_width = self.get_string_width(f"{label}: ") + 5

        # Set blue color for the value
        self.set_text_color(0, 102, 204)
        value_width = self.get_string_width(str(value))
        page_width = self.w - self.l_margin - self.r_margin

        # Adjust for dynamic text wrapping
        if label_width + value_width > page_width:
            self.set_text_color(0, 0, 0)  # Black for the key
            self.cell(label_width, 10, f"{label}: ", 0, 0, 'L')
            self.set_text_color(0, 102, 204)  # Blue for the value
            self.multi_cell(0, 10, str(value), border=0, align='L')
        else:
            self.set_text_color(0, 0, 0)  # Black for the key
            self.cell(label_width, 10, f"{label}: ", 0, 0, 'L')
            self.set_text_color(0, 102, 204)  # Blue for the value
            self.cell(0, 10, str(value), 0, 1, 'L')
        self.ln(3)

# Function to generate the PDF report
def generate_pdf(report, filename="ESG_Report.pdf"):
    pdf = PDF()
    pdf.add_page()

    # Company Details Section
    pdf.add_section_title("Company Details")
    for key, value in report.get("company_details", {}).items():
        pdf.add_dynamic_text(key, value)

    # Environment Data Section
    pdf.add_page()
    pdf.add_section_title("Environment Data")
    for key, value in report.get("environment_data", {}).items():
        pdf.add_dynamic_text(key, value)

    # Social and Governance Data Section
    pdf.add_page()
    pdf.add_section_title("Social and Governance Data")
    for key, value in report.get("social_governance_data", {}).items():
        pdf.add_dynamic_text(key, value)

    # Additional Information Section
    pdf.add_page()
    pdf.add_section_title("Additional Information")
    for key, value in report.get("additional_information", {}).items():
        pdf.add_dynamic_text(key, value)

    # Save the PDF
    pdf.output(filename)
    return filename
