import requests
import pandas as pd
from datetime import datetime

API_KEY = ""  # Leave empty if not using API key
API_URL = "https://min-api.cryptocompare.com/data/v2/histohour"

start_date = datetime(2025, 2, 27)  # Change as needed
end_date = datetime.utcnow()

params = {
    "fsym": "BTC",
    "tsym": "USD",
    "limit": 2000,
    "toTs": int(end_date.timestamp()),
}
if API_KEY:
    params["api_key"] = API_KEY

response = requests.get(API_URL, params=params)

if response.status_code == 200:
    df = pd.DataFrame(response.json()["Data"]["Data"])
    df["timestamp"] = pd.to_datetime(df["time"], unit="s")
    df = df[["timestamp", "close"]].rename(columns={"close": "price"})
    df.to_csv("btc_hourly_prices.csv", index=False)
    print("✅ Data saved: btc_hourly_prices.csv")
else:
    print(f"❌ Error: {response.status_code}, {response.text}")
