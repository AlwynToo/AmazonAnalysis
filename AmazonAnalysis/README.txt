# Amazon Sales Automation Project  
# Optimizing Amazon Sales for Profit Growth
## Current State  
- Working: Regional hotspots dashboard (HTML)  
- WIP: Product performance analysis  
- Errors: Yes (last run Failure) as below
PS C:\Users\Admin\Desktop\Automation - Local\AmazonAnalysis> python -m Analysis.main --report_type product \
>>   --start_date "2024-01-01" --end_date "2024-01-31"
At line:2 char:5
+   --start_date "2024-01-01" --end_date "2024-01-31"
+     ~
Missing expression after unary operator '--'.
At line:2 char:5
+   --start_date "2024-01-01" --end_date "2024-01-31"
+     ~~~~~~~~~~
Unexpected token 'start_date' in expression or statement.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : MissingExpressionAfterOperator
  

## Next Goals  
1. Integrate product analyzer into dashboards  
2. Sales velocity metric, 
3. Revenue/SKU metric, 
4. Top ASINs metric, 
5. SKU concentration metric  

## Folder Structure  
C:\Users\Admin\Desktop\Automation - Local\
├── AutomateSupplierOrders\                      # Data collection only
│   ├── FBA_Inventory_Ledger.py\                 # Inventory Ledger script
│   ├── FBA_Inventory_Ledger\                    # Folder
│   │   ├── Weekly	\						      # Weekly
│   │   └── Monthly\						      # Monthly
│   ├── ShipmentTracker.py\                     # For FBA Shipments script only
│   ├── AWDShipmentTracker.py\                  # For AWD Shipments script only
│   ├── Inbound_Shipments\                      # Folder
|    │   ├── FBA\
|    │    │   ├── US\				
|    │    │   │   └── 2023-10-30_containers.csv
|    │    │   └── CA Shipments\
|    │    │       └── 2023-10-30_in_transit.csv
|    │    └── AWD\
|    │         └── US Shipments\
|    │             └── 2023-10-30_in_transit.csv
│   ├── 01 FBAManageInventoryReportR02.py   # Inventory Report Script
│   ├── FBA Manage Inventory\                   # Inventory reports
│   │   ├── manage_inventory_report.xlsx        # US
│   │   └── manage_inventory_report_CA.xlsx     # CA
│   ├── 02 OrderReportR06.py                    # Orders script
│   └── Order Report\
│       └── order_report.xlsx                   # Orders data
└── AmazonAnalysis\                             # Analysis system only
    ├── Analysis\
    │   ├── main.py                            # Master script
    │   ├── core\                              # Analysis logic
    │   │   ├── product_analyzer.py            # SKU/ASIN metrics 
    │   │   ├── pricing_analyzer.py           # Price optimization
    │   │   ├── margin_analyzer.py             # Margin analysis
    │   │   ├── geo_analyzer.py               # Regional hotspots
    │   │   ├── inventory_analyzer.py          # Stock analysis
    │   │   └── order_analyzer.py              # Order metrics
    │   ├── utils\
    │   │   ├── logger.py                      # Centralized logging
    │   │   ├── period_detector.py			     # Period checker
    │   │   └── data_loader.py                 # Load orders + inventory
    │   └── config\
    │   │   ├── paths.py                       # All file paths
    │   │   └── constants.py                   # Marketplace codes
    │   └── templates\
    │       └── dashboard_template.html        # html
    ├── Outputs\
    │   ├── Dashboards\
    │   ├── Reports\
    │   ├── Weekly\
    │   ├── Monthly\
    │   └── Custom\
    └── Logs\                                  # Central log storage
        ├── analysis_2023-10-30.log
        └── errors_2023-10-30.log
 

## GitHub repository link
https://github.com/AlwynToo/AmazonAnalysis

## Briefly tell me what you understand about these python files after you analyzed.
1. main.py
2. geo_analyzer.py
3. period_detector.py
4. logger.py
5. data_loader.py
6. paths.py
7. constants.py
8. dashboard_template.html
