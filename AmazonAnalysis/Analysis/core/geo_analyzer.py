import pandas as pd
import plotly.express as px
from pathlib import Path

class GeoAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def generate_dashboard(self, start_date: str, end_date: str, period: str) -> Path:
        """Generate interactive HTML dashboard with regional metrics"""
        # Calculate regional sales data
        regional_data = self.df.groupby(['ship_postal_code', 'ship_city', 'ship_state']).agg(
            total_orders=('amazon_order_id', 'nunique'),
            total_revenue=('item_price', 'sum')
        ).reset_index().sort_values('total_revenue', ascending=False)

        # Create Plotly figure
        fig = px.bar(
            regional_data.head(10),
            x='ship_postal_code',
            y='total_revenue',
            color='ship_state',
            labels={'ship_postal_code': 'Postal Code', 'total_revenue': 'Revenue'},
            title=f"Top Regional Performers ({period} Report)"
        )

        # Configure output paths
        output_dir = Path("Outputs") / period
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"RegionalDashboard_{period}_{start_date}_to_{end_date}.html"
        
        # Save dashboard
        fig.write_html(output_path)
        return output_path