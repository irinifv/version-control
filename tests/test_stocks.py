import pandas as pd
from app.stocks import fetch_stock_data
from pandas import DataFrame

def test_example():
    assert 1 + 1 == 2

def test_data_fetching():
    df = fetch_stock_data("SPOT")
    print(df.head())  # View the first few rows for debugging
    assert isinstance(df, pd.DataFrame)  # Ensure the result is a DataFrame
    assert not df.empty  # Ensure the DataFrame is not empty
    
    expected_columns = ["timestamp", "open", "high", "low", "close", "volume"]
    if df.columns.tolist() != expected_columns:
        # Check for prefixed column names and validate
        expected_prefixed_columns = ["1. open", "2. high", "3. low", "4. close", "5. volume"]
        assert df.columns.tolist() == expected_prefixed_columns
