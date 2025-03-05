import requests
import json

DEEPSEEK_API_KEY = "your-deepseek-api-key"
DEEPSEEK_URL = "your-deepseek-endpoint"

prompt = """
These are the trading sessions in UTC+0:
Asia (00:00 - 06:00 UTC)
London (06:00 - 12:00 UTC)
New York (12:00 - 20:00 UTC)
Close (20:00 - 00:00 UTC)

Analyze BTC price action in each session from the CSV file.
1. Count BULL (open > close) & BEAR (open < close) per session.
2. Identify patterns based on the day of the week/session.
3. Predict probability of BULL/BEAR for each hour.
4. Recommend a trading strategy for today.
5. Summarize findings.
"""

with open("btc_hourly_prices.csv", "rb") as file:
    files = {"file": file}
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    response = requests.post(DEEPSEEK_URL, files=files, headers=headers)

if response.status_code == 200:
    analysis_result = response.json()
    with open("analysis.txt", "w") as f:
        f.write(json.dumps(analysis_result, indent=4))
    print("✅ Analysis saved: analysis.txt")
else:
    print(f"❌ Error: {response.status_code}, {response.text}")
