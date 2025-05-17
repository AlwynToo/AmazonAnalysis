from Analysis.config.paths import ORDER_DATA
import pandas as pd

# utils/data_loader.py
def load_order_data(start_date: str, end_date: str) -> pd.DataFrame:
    """Load and filter order data by date"""
    df = pd.read_excel(ORDER_DATA)
    
    # Standardize column names (spaces → underscores + lowercase)
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    # Now use the standardized column name
    df['purchase_date'] = pd.to_datetime(df['purchase_date'])
    
    # Filter by date range
    mask = (df['purchase_date'] >= start_date) & (df['purchase_date'] <= end_date)
    return df.loc[mask]

# Add Validation Checks
def load_order_data(start_date: str, end_date: str) -> pd.DataFrame:
    df = pd.read_excel(ORDER_DATA)
    
    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    # Validate critical columns
    required_columns = {
        'purchase_date', 
        'ship_postal_code', 
        'item_price', 
        'amazon_order_id',
        'sku'
    }
    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in order data: {missing}")
    
    # Process dates
    df['purchase_date'] = pd.to_datetime(df['purchase_date'])
    
    # Filter
    mask = (df['purchase_date'] >= start_date) & (df['purchase_date'] <= end_date)
    return df.loc[mask]