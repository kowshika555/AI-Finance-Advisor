# backend/app/crud.py

# Placeholder functions — can connect to DB later
def save_finance_data(income, expenses, goal, suggestion):
    print(f"Saving to database: Income={income}, Expenses={expenses}, Goal={goal}, Suggestion={suggestion}")
    # Later connect to actual DB here (SQLite, PostgreSQL, etc.)

# backend/app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas

def create_finance_entry(db: Session, data: schemas.FinanceCreate):
    entry = models.FinanceEntry(
        income=data.income,
        expenses=data.expenses,
        goal=data.goal,
        suggestion=data.suggestion
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

def get_all_entries(db: Session):
    return db.query(models.FinanceEntry).all()
