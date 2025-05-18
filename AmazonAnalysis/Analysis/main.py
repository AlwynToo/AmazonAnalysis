import argparse
from Analysis.core.geo_analyzer import GeoAnalyzer
from Analysis.utils.logger import logger
from Analysis.utils.data_loader import load_order_data  # Add this import
from Analysis.core import product_analyzer
from pathlib import Path
from Analysis.utils.period_detector import detect_report_period

def main():
    parser = argparse.ArgumentParser(description='Generate Amazon Sales Reports')
    parser.add_argument('--start_date', required=True, help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end_date', required=True, help='End date (YYYY-MM-DD)')
    parser.add_argument('--report_type', required=True, choices=['product', 'regional'])
    
    args = parser.parse_args()
    
    if args.report_type == 'regional':
        logger.info("Generating regional dashboard...")
        
        try:
            df = load_order_data(args.start_date, args.end_date)
            period = detect_report_period(args.start_date, args.end_date)
            
            analyzer = GeoAnalyzer(df)
            dashboard_path = analyzer.generate_dashboard(
                args.start_date, 
                args.end_date,
                period
            )
            
            logger.success(f"{period} report saved to {dashboard_path}")
            
        except Exception as e:
            logger.error(f"Dashboard generation failed: {str(e)}")
            raise

    if args.report_type == 'product':
        '''
        # Placeholder
        print("placeholder for new feature")
        '''

        logger.info("Generating product dashboard...")

        try:
            analyzer = product_analyzer.ProductAnalyzer(args.start_date, args.end_date)
            report_df, report_path = analyzer.analyze_product_performance(args.start_date, args.end_date)

        except Exception as e:
            logger.error(f"Dashboard generation failed: {str(e)}")
            raise

if __name__ == "__main__":
    main()