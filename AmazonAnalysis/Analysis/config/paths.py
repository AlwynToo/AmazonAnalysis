# AmazonAnalysis/Analysis/config/paths.py
import os
from pathlib import Path


# Root directory: AmazonAnalysis/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Adjust based on your structure
LOG_DIR = os.path.join(BASE_DIR, "Logs")  # Points to AmazonAnalysis/Logs

# Base directory: Points to "AmazonAnalysis/" folder
ROOT_DIR = Path(__file__).parent.parent.parent.parent

# Data Sources
ORDER_DATA = ROOT_DIR / "AutomateSupplierOrders/Order Report/order_report.xlsx"
INVENTORY_DATA = ROOT_DIR / "AutomateSupplierOrders/FBA Manage Inventory"
SHIPMENT_DATA = ROOT_DIR / "AutomateSupplierOrders/Inbound Shipments"

# Analysis Outputs
OUTPUT_DIR = ROOT_DIR / "Outputs"
REPORTS_DIR = OUTPUT_DIR / "Reports"
DASHBOARDS_DIR = OUTPUT_DIR / "Dashboards"

# Logging
LOGS_DIR = ROOT_DIR / "Logs"

# Templates
TEMPLATES_DIR = ROOT_DIR / "Analysis/templates"

def create_directories():
    """Create required directories if missing"""
    directories = [
        OUTPUT_DIR,
        REPORTS_DIR,
        DASHBOARDS_DIR,
        LOGS_DIR,
        TEMPLATES_DIR
    ]
    
    for dir_path in directories:
        dir_path.mkdir(parents=True, exist_ok=True)

# Optional: Auto-create on import
create_directories()

# Example usage:
if __name__ == "__main__":
    print(f"Order data path: {ORDER_DATA}")
    print(f"Logs directory: {LOGS_DIR}")