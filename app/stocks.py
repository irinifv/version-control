# Import necessary modules
import requests
import pandas as pd 
import sys
sys.path.append('/Users/irinifourniv/Desktop/version-control2/app')
from app.env_helper import get_env_variable
from app.utils import format_usd
from pandas import read_csv
import plotly.express as px

# Get the API key from environment variables
API_KEY = get_env_variable("ALPHAVANTAGE_API_KEY", default_value="demo")

def format_usd(my_price):
    return f"${float(my_price):,.2f}"

# Define the function for fetching stock data
def fetch_stock_data(symbol):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&outputsize=full&datatype=csv"
    df = read_csv(request_url)
    return df

# Main script
if __name__ == "__main__":
    # Get user input for the stock symbol
    symbol = input("Please input a symbol (e.g., 'NFLX'): ")
    print("SYMBOL:", symbol)

    # Call fetch_stock_data to get the stock data
    df = fetch_stock_data(symbol)
    
    # Print the first few rows of the data for inspection
    print(df.head())

    # --- Report Generation ---
    print("-------------------------")
    print("LATEST CLOSING PRICE:")
    first_row = df.iloc[0]
    print(f"${first_row['adjusted_close']:.2f} as of {first_row['timestamp']}")

    recent_df = df.iloc[0:100]  # Last 100 days for recent stats
    print("-------------------------")
    print("RECENT STATS...")
    print(f"MEAN PRICE: ${recent_df['adjusted_close'].mean():.2f}")
    print(f"MEDIAN PRICE: ${recent_df['adjusted_close'].median():.2f}")
    print(f"MIN PRICE: ${recent_df['adjusted_close'].min():.2f}")
    print(f"MAX PRICE: ${recent_df['adjusted_close'].max():.2f}")
    print(f"75TH PERCENTILE: ${recent_df['adjusted_close'].quantile(0.75):.2f}")
    print(f"25TH PERCENTILE: ${recent_df['adjusted_close'].quantile(0.25):.2f}")

    # --- Plotting the Data ---
    fig = px.line(x=df["timestamp"], y=df["adjusted_close"],
                  title=f"Stock Prices ({symbol})",
                  labels={"x": "Date", "y": "Stock Price ($)"})
    fig.show()