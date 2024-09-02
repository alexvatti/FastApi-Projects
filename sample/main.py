# main.py
from fastapi import FastAPI
from routes import bmi_calculator, age_calculator, sip_calculator, home_loan_calculator
import uvicorn

app = FastAPI()

app.include_router(bmi_calculator.router, prefix="/bmi")
app.include_router(age_calculator.router, prefix="/age")
app.include_router(sip_calculator.router, prefix="/sip")
app.include_router(home_loan_calculator.router, prefix="/home-loan")

@app.get("/")
def read_root():
    return {"message": "Fast API!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
