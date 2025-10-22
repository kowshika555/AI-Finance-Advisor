# backend/app/schemas.py
from pydantic import BaseModel

class FinanceRequest(BaseModel):
    income: float
    expenses: float
    goal: str

class FinanceResponse(BaseModel):
    suggestion: str

# backend/app/schemas.py
from pydantic import BaseModel

class FinanceBase(BaseModel):
    income: float
    expenses: float
    goal: str

class FinanceCreate(FinanceBase):
    suggestion: str

class FinanceResponse(FinanceBase):
    id: int
    suggestion: str

    class Config:
        orm_mode = True
