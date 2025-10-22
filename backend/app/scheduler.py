# backend/app/scheduler.py
import time

def run_daily_summary():
    print("Running daily finance summary (placeholder)...")
    # In real app: Fetch user data, analyze spending, send AI tips automatically

if __name__ == "__main__":
    while True:
        run_daily_summary()
        time.sleep(86400)  # Run every 24 hours
