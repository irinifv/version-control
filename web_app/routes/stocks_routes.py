# this is the "web_app/routes/stocks_routes.py" file ...
from flask import Blueprint, request, render_template, redirect, flash
from app.stocks import fetch_stock_data, format_usd

stocks_routes = Blueprint("stocks_routes", __name__)

@stocks_routes.route("/stocks/form")
def stocks_form():
    print("STOCKS FORM...")
    symbol = request.args.get("symbol", "MSFT")
    return render_template("stocks_form.html", symbol=symbol)

@stocks_routes.route("/stocks/dashboard", methods=["GET", "POST"])
def stocks_dashboard():
    
    print("STOCKS DASHBOARD...")
    if request.method == "POST":
        request_data = dict(request.form)
    else:
        request_data = dict(request.args)
    print("REQUEST DATA:", request_data)
    
    symbol = request_data.get("symbol") or "MSFT"  # Get form input or default
    
    try:
        df = fetch_stock_data(symbol=symbol)

        if df.empty:
            raise Exception("No data available for this symbol.")
        if "adjusted_close" not in df.columns:
            raise Exception("Missing adjusted_close column in stock data.")

        latest_close_usd = format_usd(df.iloc[0]["adjusted_close"])
        latest_date = df.iloc[0]["timestamp"]
        data = df.to_dict("records")

        flash("Fetched Real-time Market Data!", "success")
        return render_template(
            "stocks_dashboard.html",
            symbol=symbol,
            latest_close_usd=latest_close_usd,
            latest_date=latest_date,
            data=data
        )
    except Exception as err:
        print("OOPS:", err)
        flash(f"Error: {err}", "danger")
        return redirect("/stocks/form")
        
#
# API ROUTES
#
@stocks_routes.route("/api/stocks.json")
def stocks_api():
    print("STOCKS DATA (API)...")

    # for data supplied via GET request, url params are in request.args:
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    symbol = url_params.get("symbol") or "NFLX"

    try:
        df = fetch_stock_data(symbol=symbol)
        print("FETCHED DATAFRAME:", df)
        data = df.to_dict("records") # convert dataframe to list of dict
        return {"symbol": symbol, "data": data}
    except Exception as err:
        print('OOPS', err)
        return {"message":"Market Data Error. Please try again."}, 404
