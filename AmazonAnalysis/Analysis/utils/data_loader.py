from Analysis.config.paths import ORDER_DATA
import pandas as pd
from datetime import datetime
from typing import Optional, Union
from pandas import DataFrame


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

def filter_by_dates(
    df: DataFrame,
    date_column: str,
    start_date: Optional[Union[str, datetime]] = None,
    end_date: Optional[Union[str, datetime]] = None
) -> DataFrame:
    """
    Filters a DataFrame based on date range (inclusive).
    
    Args:
        df: Input DataFrame containing the data
        date_column: Name of the column containing datetime values
        start_date: Start date (YYYY-MM-DD format string or datetime object)
        end_date: End date (YYYY-MM-DD format string or datetime object)
    
    Returns:
        Filtered DataFrame with rows within the specified date range
    
    Example:
        >>> filtered_df = filter_by_dates(orders_df, 'order_date', '2024-01-01', '2024-01-31')
    """
    # Make a copy to avoid SettingWithCopyWarning
    filtered_df = df.copy()
    
    # Convert date_column to datetime if not already
    filtered_df[date_column] = pd.to_datetime(filtered_df[date_column])
    
    # Apply date filters if provided
    if start_date:
        start_date = pd.to_datetime(start_date)
        filtered_df = filtered_df[filtered_df[date_column] >= start_date]
    
    if end_date:
        end_date = pd.to_datetime(end_date)
        filtered_df = filtered_df[filtered_df[date_column] <= end_date]
    
    return filtered_df