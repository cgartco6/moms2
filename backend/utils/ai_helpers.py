# utils/ai_helpers.py
import random
import time

class AIHelper:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def perform_task(self):
        tasks = {
            "Data Analyst": "Analyzing food cost patterns...",
            "Inventory Manager": "Optimizing stock levels...",
            "Cost Predictor": "Monitoring price fluctuations...",
            "Security Guardian": "Ensuring compliance with regulations..."
        }
        return tasks.get(self.role, "Performing task...")

def create_ai_team():
    return [
        AIHelper("DataBot", "Data Analyst"),
        AIHelper("StockBot", "Inventory Manager"),
        AIHelper("PriceBot", "Cost Predictor"),
        AIHelper("SecureBot", "Security Guardian")
    ]

def run_ai_tasks(team):
    for ai in team:
        print(f"{ai.name} ({ai.role}): {ai.perform_task()}")
        time.sleep(1)
