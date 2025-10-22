# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.openai_client import get_finance_advice

app = FastAPI(title="AI Finance Advisor API")

# Allow frontend (vanilla JS) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FinanceRequest(BaseModel):
    income: float
    expenses: float
    goal: str

@app.get("/")
def home():
    return {"message": "AI Finance Advisor Backend is running ✅"}

@app.post("/ai-advice")
def ai_advice(data: FinanceRequest):
    advice = get_finance_advice(data.income, data.expenses, data.goal)
    return {"suggestion": advice}

# backend/app/main.py
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.db import SessionLocal, engine
from app.openai_client import get_finance_advice

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Finance Advisor API")

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency: Get DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "AI Finance Advisor Backend running ✅"}

@app.post("/ai-advice")
def ai_advice(data: schemas.FinanceBase, db: Session = Depends(get_db)):
    suggestion = get_finance_advice(data.income, data.expenses, data.goal)
    entry_data = schemas.FinanceCreate(
        income=data.income,
        expenses=data.expenses,
        goal=data.goal,
        suggestion=suggestion
    )
    crud.create_finance_entry(db, entry_data)
    return {"suggestion": suggestion}

@app.get("/entries")
def list_entries(db: Session = Depends(get_db)):
    entries = crud.get_all_entries(db)
    return entries
