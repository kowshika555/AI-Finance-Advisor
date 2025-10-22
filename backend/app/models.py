# backend/app/models.py
from pydantic import BaseModel

class FinanceData(BaseModel):
    id: int | None = None
    income: float
    expenses: float
    goal: str
    suggestion: str | None = None

# backend/app/models.py
from sqlalchemy import Column, Integer, Float, String
from app.db import Base

class FinanceEntry(Base):
    __tablename__ = "finance_entries"

    id = Column(Integer, primary_key=True, index=True)
    income = Column(Float, nullable=False)
    expenses = Column(Float, nullable=False)
    goal = Column(String, nullable=False)
    suggestion = Column(String, nullable=True)
