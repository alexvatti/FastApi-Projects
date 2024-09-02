# routes/bmi_calculator.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class BMICalculatorInput(BaseModel):
    weight: float  # weight in kilograms
    height: float  # height in meters

def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)

def categorize_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

@router.post("/calculate-bmi/")
def calculate_bmi_endpoint(input: BMICalculatorInput):
    bmi = calculate_bmi(input.weight, input.height)
    category = categorize_bmi(bmi)
    return {"bmi": round(bmi, 2), "category": category}
