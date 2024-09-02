# routes/home_loan_calculator.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class HomeLoanCalculatorInput(BaseModel):
    loan_amount: float  # Total loan amount
    annual_rate: float  # Annual interest rate in percentage
    tenure_years: int  # Tenure in years

def calculate_emi(loan_amount: float, annual_rate: float, tenure_years: int) -> float:
    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12
    emi = (loan_amount * monthly_rate * ((1 + monthly_rate) ** tenure_months)) / (((1 + monthly_rate) ** tenure_months) - 1)
    return emi

@router.post("/calculate-home-loan-emi/")
def calculate_home_loan_emi_endpoint(input: HomeLoanCalculatorInput):
    emi = calculate_emi(input.loan_amount, input.annual_rate, input.tenure_years)
    return {"emi": round(emi, 2)}
