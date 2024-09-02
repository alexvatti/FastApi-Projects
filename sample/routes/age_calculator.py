# routes/age_calculator.py
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class AgeCalculatorInput(BaseModel):
    birth_year: int
    birth_month: int
    birth_day: int

def calculate_age(birth_date: datetime) -> int:
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

@router.post("/calculate-age/")
def calculate_age_endpoint(input: AgeCalculatorInput):
    birth_date = datetime(input.birth_year, input.birth_month, input.birth_day)
    age = calculate_age(birth_date)
    return {"age": age}
