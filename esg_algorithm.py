import math

def calculate_esg_score(company_data, employee_data):
    # Dummy algorithm: You can replace this with your own logic
    company_score = sum(company_data.values()) / len(company_data)
    employee_score = sum([sum(emp.values()) / len(emp) for emp in employee_data]) / len(employee_data)
    return {"company_score": company_score, "employee_score": employee_score, "final_score": (company_score + employee_score) / 2}
    
    