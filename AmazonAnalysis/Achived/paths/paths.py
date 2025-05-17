from pathlib import Path

AUTOMATION_ROOT = Path(r"C:\Users\Admin\Desktop\Automation - Local")
ORDER_DATA = AUTOMATION_ROOT / "AutomateSupplierOrders/Order Report/order_report.xlsx"
# OUTPUT_DIR = AUTOMATION_ROOT / "AmazonAnalysis/Outputs/Weekly_Reports"
LOG_DIR = AUTOMATION_ROOT / "AmazonAnalysis/Logs/"
# config/paths.py
OUTPUT_DIR = Path(__file__).parent.parent.parent / 'Outputs'

# product_analyzer.py
output_dir = paths.OUTPUT_DIR / period  # Now dynamic