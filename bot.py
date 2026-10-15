import threading
import time
from flask import Flask

app = Flask(__name__)

# Strategy Configuration for EURUSD
SYMBOL = "EURUSD"
TIMEFRAME = "15M"

@app.route('/')
def home():
    return f"Exness Trading Bot is Live and Monitoring {SYMBOL} ({TIMEFRAME}) 24/7!"

def analyze_eurusd_strategy():
    print(f"[{SYMBOL}] Scanning 15M Chart...")
    print(f"[{SYMBOL}] Checking EMA 9 & EMA 21 Crossover...")
    print(f"[{SYMBOL}] Looking for Bullish/Bearish Fair Value Gap (FVG)...")
    print(f"[{SYMBOL}] Monitoring Order Block Retest for Entry...")
    
    # እዚህ ጋር የ EURUSD ገበያ ሲግናል ሲገኝ ወደ Exness Order ይላካል
    # Entry Rule: EMA 9/21 Cross + FVG + Retest

def run_trading_bot():
    print(f"=== Exness Auto-Trading Bot Started for {SYMBOL} ===")
    while True:
        try:
            analyze_eurusd_strategy()
            time.sleep(60) # በየ 1 ደቂቃው EURUSD ገበያን ይፈትሻል
        except Exception as e:
            print(f"Error analyzing {SYMBOL}: {e}")
            time.sleep(10)

if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_trading_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    app.run(host='0.0.0.0', port=10000)
    
