import requests
import json

DISCORD_WEBHOOK_URL = "your-discord-webhook-url"

with open("analysis.txt", "r") as f:
    analysis = json.load(f)

message = f"""
📊 **BTC Trading Analysis** 📊
🔹 **Session Summary:** {analysis.get("session_summary", "N/A")}
🔹 **Hourly Predictions:** {analysis.get("hourly_predictions", "N/A")}
🔹 **Trading Strategy:** {analysis.get("strategy", "N/A")}
🔹 **Key Findings:** {analysis.get("summary", "N/A")}
"""

payload = {"content": message}
headers = {"Content-Type": "application/json"}

response = requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(payload), headers=headers)

if response.status_code == 204:
    print("✅ Analysis sent to Discord!")
else:
    print(f"❌ Error: {response.status_code}, {response.text}")
