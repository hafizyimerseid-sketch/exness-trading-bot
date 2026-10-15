import os
import threading
import time
from flask import Flask

app = Flask(__name__)

# ከ Render Environment Variables ሚስጥራዊ መረጃዎችን በአስተማማኝ ሁኔታ ማንበብ
EXNESS_LOGIN = os.environ.get("EXNESS_LOGIN")
EXNESS_PASSWORD = os.environ.get("EXNESS_PASSWORD")
EXNESS_SERVER = os.environ.get("EXNESS_SERVER")

SYMBOL = "EURUSD"
TIMEFRAME = "15M"

@app.route('/')
def home():
    return f"Exness Trading Bot for {SYMBOL} is Securely Running Live 24/7!"

def run_trading_bot():
    print(f"=== Secure Exness Bot Started for {SYMBOL} ===")
    print(f"Connected Account ID: {EXNESS_LOGIN} on Server: {EXNESS_SERVER}")
    
    while True:
        try:
            print(f"[{SYMBOL}] Scanning 15M Chart for EMA 9/21, FVG & Order Block...")
            # እዚህ ጋር ከ Exness Server ጋር ተገናኝቶ Trade የማድረግ ስራ ይከናወናል
            time.sleep(60)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_trading_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    app.run(host='0.0.0.0', port=10000)
    
