# unemployment.py

print("THIS IS AN UNEMPLOYMENT REPORT...")

# IMPORTS
import os
import json
import requests
from pprint import pprint
from statistics import mean
import plotly.express as px

#getting the env variables
from app.env_helper import get_env_variable
API_KEY = get_env_variable("ALPHAVANTAGE_API_KEY", default_value="demo")

# Helper function to format percentages
def format_pct(value):
    """
    Converts a numeric value into a percentage string with one decimal place.
    """
    return f"{value:.1f}%"

#fetching unemployment data:
def fetch_unemployment_data(API_KEY):
   
    request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"
    response = requests.get(request_url)

    if response.status_code != 200:
        raise Exception("Error fetching unemployment data.")

    data = response.json()
    if "data" not in data:
        raise Exception("Unexpected response format.")

    return data["data"]  # Returns the unemployment data section

# Fetch data
data = fetch_unemployment_data(API_KEY)

# Challenge A
#
# What is the most recent unemployment rate? And the corresponding date?
# Display the unemployment rate using a percent sign.

print("-------------------------")
print("LATEST UNEMPLOYMENT RATE:")
# print(data[0])
print(f"{data[0]['value']}%", "as of", data[0]["date"])


# Challenge B
#
# What is the average unemployment rate for all months during this calendar year?
# ... How many months does this cover?

this_year = [d for d in data if "2022-" in d["date"]]

rates_this_year = [float(d["value"]) for d in this_year]

# print(rates_this_year)
print("-------------------------")
print("AVG UNEMPLOYMENT THIS YEAR:", f"{mean(rates_this_year)}%")
print("NO MONTHS:", len(this_year))


# Challenge C
#
# Plot a line chart of unemployment rates over time.
dates = [d["date"] for d in data]
rates = [float(d["value"]) for d in data]
fig = px.line(x=dates, y=rates, title="United States Unemployment Rate over time", labels={"x": "Month", "y": "Unemployment Rate"})
fig.show()

