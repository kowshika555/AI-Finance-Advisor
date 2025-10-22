# backend/app/openai_client.py
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_finance_advice(income, expenses, goal):
    savings = income - expenses
    prompt = f"""
    You are an AI personal finance advisor.
    User income: ₹{income}
    User expenses: ₹{expenses}
    User goal: {goal}
    Savings: ₹{savings}

    Give a short, practical, and motivational financial suggestion in 3-4 sentences.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
