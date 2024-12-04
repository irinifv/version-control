import pandas as pd
from pandas import DataFrame
from app.stocks import fetch_stock_data
from app.utils import format_usd  

def test_example():
    assert 1 + 1 == 2

def test_usd_formatting():
    assert format_usd(3.5) == "$3.50"
    assert format_usd(0.44444) == "$0.44"
    assert format_usd(123456789) == "$123,456,789.00"

def test_data_fetching():
    df = fetch_stock_data("SPOT")
    print(df.head())  # View the first few rows for debugging
    assert isinstance(df, pd.DataFrame)  # Ensure the result is a DataFrame
    assert not df.empty  # Ensure the DataFrame is not empty
    
    expected_columns = ["timestamp", "open", "high", "low", "close", "volume"]
    if df.columns.tolist() != expected_columns:
        # Check for prefixed column names and validate
        expected_prefixed_columns = ["timestamp", "open", "high", "low", "close", "volume"]
        assert df.columns.tolist() == expected_prefixed_columns
