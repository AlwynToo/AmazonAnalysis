# Analysis/utils/period_detector.py
from datetime import datetime
from dateutil.relativedelta import relativedelta

def detect_report_period(start_date_str: str, end_date_str: str) -> str:
    """Auto-detect if date range is weekly/monthly/custom"""
    start = datetime.strptime(start_date_str, "%Y-%m-%d")
    end = datetime.strptime(end_date_str, "%Y-%m-%d")
    
    # Check for weekly (7 days or less)
    if (end - start).days <= 6:
        return "Weekly"
        
    # Check for calendar month
    if (start.day == 1) and (end.month != (end + relativedelta(days=1)).month):
        return "Monthly"
        
    return "Custom"