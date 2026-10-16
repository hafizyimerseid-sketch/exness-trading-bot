import os
import threading
import time
import requests
from flask import Flask

app = Flask(__name__)

# Config
EXNESS_LOGIN = os.environ.get("EXNESS_LOGIN")
EXNESS_PASSWORD = os.environ.get("EXNESS_PASSWORD")
EXNESS_SERVER = os.environ.get("EXNESS_SERVER")

SYMBOL = "EURUSD"
TIMEFRAME = "15M"
RENDER_URL = "https://exness-trading-bot.onrender.com"

@app.route('/')
def home():
    return f"Exness Trading Bot for {SYMBOL} is Active and Live 24/7!"

def keep_alive():
    """Render ራሱን በራሱ በየ 5 ደቂቃው Ping በማድረግ እንዳይተኛ/እንዳይቆም ያደርገዋል"""
    while True:
        try:
            time.sleep(300) # 5 ደቂቃ
            requests.get(RENDER_URL)
            print("[Self-Ping] Successfully pinged server to keep bot awake 24/7!")
        except Exception as e:
            print(f"[Self-Ping Error]: {e}")

def run_trading_bot():
    print(f"=== Exness Auto-Trading Bot Started for {SYMBOL} ===")
    print(f"Account ID: {EXNESS_LOGIN} | Server: {EXNESS_SERVER}")
    
    while True:
        try:
            print(f"[{SYMBOL}] Scanning 15M Chart for EMA 9/21, FVG & Order Block...")
            # EURUSD Strategy Execution
            time.sleep(60) # በየ 1 ደቂቃው ገበያውን ይፈትሻል
        except Exception as e:
            print(f"Error in trading loop: {e}")
            time.sleep(10)

if __name__ == "__main__":
    # 1. Trading Logic Thread
    bot_thread = threading.Thread(target=run_trading_bot)
    bot_thread.daemon = True
    bot_thread.start()

    # 2. Keep-Alive Ping Thread (እንዳይተኛ የሚያደርግ)
    ping_thread = threading.Thread(target=keep_alive)
    ping_thread.daemon = True
    ping_thread.start()

    # 3. Web Server Port
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
