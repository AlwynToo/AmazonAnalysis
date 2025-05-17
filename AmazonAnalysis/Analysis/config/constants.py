# config/constants.py
SKU_COL = 'sku'  # Lowercase to match data_loader's standardization
ASIN_COL = 'asin'
DATE_COL = 'purchase_date'

# product_analyzer.py
from ..config import constants

def _calculate_sales_velocity(self, df):
    return df.groupby(constants.SKU_COL).agg(...)  # Use constants