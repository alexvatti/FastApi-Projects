# routes/sip_calculator.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SIPCalculatorInput(BaseModel):
    principal: float  # Monthly investment
    rate: float  # Annual interest rate in percentage
    months: int  # Number of months

def calculate_sip(principal: float, rate: float, months: int) -> float:
    monthly_rate = rate / (12 * 100)
    future_value = principal * (((1 + monthly_rate) ** months - 1) / monthly_rate)
    return future_value

@router.post("/calculate-sip/")
def calculate_sip_endpoint(input: SIPCalculatorInput):
    future_value = calculate_sip(input.principal, input.rate, input.months)
    return {"future_value": round(future_value, 2)}
