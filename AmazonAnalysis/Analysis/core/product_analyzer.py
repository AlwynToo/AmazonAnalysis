# AmazonAnalysis/Analysis/core/product_analyzer.py
import pandas as pd
from datetime import datetime
from pathlib import Path
from typing import Tuple
from ..utils import logger, data_loader, period_detector
from ..config import paths, constants

class ProductAnalyzer:
    def __init__(self):
        self.log = logger.get_logger(__name__)
        self.log.info("Initializing product analyzer")
        
        try:
            self.order_df = data_loader.load_order_data()
            self.log.success("Order data loaded successfully")
        except Exception as e:
            self.log.error(f"Failed to load order data: {str(e)}")
            raise

    def analyze_product_performance(self, start_date: str, end_date: str) -> Tuple[pd.DataFrame, str]:
        """Main analysis workflow with full integration"""
        try:
            # Date filtering using data_loader utility
            filtered_df = data_loader.filter_by_dates(self.order_df, start_date, end_date)
            self.log.info(f"Filtered {len(filtered_df)} orders between {start_date} and {end_date}")

            # Period detection
            period_type = period_detector.detect_period(start_date, end_date)
            self.log.info(f"Period type detected: {period_type}")

            # Core analyses
            velocity_df = self._calculate_sales_velocity(filtered_df, start_date, end_date)
            revenue_df = self._calculate_revenue_metrics(filtered_df)
            concentration_df = self._analyze_sku_concentration(revenue_df)
            top_asins_df = self._identify_top_asins(filtered_df)

            # Save results
            output_path = self._save_results(
                period_type, 
                start_date, 
                end_date,
                velocity_df,
                revenue_df,
                concentration_df,
                top_asins_df
            )
            
            return concentration_df, output_path

        except Exception as e:
            self.log.error(f"Analysis failed: {str(e)}")
            raise

    def _calculate_sales_velocity(self, df: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
        """Calculate daily sales velocity with date validation"""
        try:
            start_dt = datetime.strptime(start, "%Y-%m-%d")
            end_dt = datetime.strptime(end, "%Y-%m-%d")
            days = (end_dt - start_dt).days + 1
            
            velocity_df = df.groupby(constants.SKU_COL).agg(
                total_units=('quantity', 'sum'),
                total_orders=('amazon_order_id', 'nunique')
            ).reset_index()
            
            velocity_df['daily_velocity'] = velocity_df['total_units'] / days
            return velocity_df.sort_values('daily_velocity', ascending=False)
            
        except Exception as e:
            self.log.error(f"Velocity calculation failed: {str(e)}")
            raise

    def _calculate_revenue_metrics(self, df: pd.DataFrame) -> pd.DataFrame:
        """Standardized revenue calculations"""
        try:
            df['revenue'] = df['quantity'] * df['item_price']
            return df.groupby([constants.SKU_COL, constants.ASIN_COL]).agg(
                total_revenue=('revenue', 'sum'),
                average_price=('item_price', 'mean'),
                order_count=('amazon_order_id', 'nunique')
            ).reset_index().sort_values('total_revenue', ascending=False)
        except KeyError as e:
            self.log.error(f"Missing column in revenue calculation: {str(e)}")
            raise

    def _analyze_sku_concentration(self, df: pd.DataFrame) -> pd.DataFrame:
        """Pareto analysis of SKU revenue concentration"""
        try:
            sorted_df = df.sort_values('total_revenue', ascending=False)
            sorted_df['cumulative_pct'] = (sorted_df['total_revenue'].cumsum() / 
                                         sorted_df['total_revenue'].sum() * 100)
            return sorted_df[[constants.SKU_COL, 'total_revenue', 'cumulative_pct']]
        except ZeroDivisionError:
            self.log.error("No revenue data for SKU concentration analysis")
            return pd.DataFrame()

    def _identify_top_asins(self, df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
        """Identify top performing ASINs across metrics"""
        try:
            return df.groupby(constants.ASIN_COL).agg(
                total_units=('quantity', 'sum'),
                total_revenue=('revenue', 'sum'),
                unique_skus=('sku', 'nunique')
            ).reset_index().sort_values('total_revenue', ascending=False).head(top_n)
        except Exception as e:
            self.log.error(f"Top ASIN identification failed: {str(e)}")
            raise

    def _save_results(self, period: str, start: str, end: str, *dfs) -> str:
        """Save results to period-specific directory"""
        try:
            output_dir = paths.OUTPUT_DIR / period.lower()
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / f"product_analysis_{period}_{start}_to_{end}.xlsx"
            
            with pd.ExcelWriter(output_path) as writer:
                for i, df in enumerate(dfs):
                    sheet_name = [
                        'Sales Velocity', 
                        'Revenue Metrics',
                        'SKU Concentration',
                        'Top ASINs'
                    ][i]
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            
            self.log.success(f"Results saved to {output_path}")
            return str(output_path)
            
        except Exception as e:
            self.log.error(f"Failed to save results: {str(e)}")
            raise

# Example usage in main.py would call:
# analyzer = ProductAnalyzer()
# report_df, report_path = analyzer.analyze_product_performance(start_date, end_date)