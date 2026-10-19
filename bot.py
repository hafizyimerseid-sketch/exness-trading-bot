import os
import time
import threading
import requests
from flask import Flask

app = Flask(__name__)

# Config - Environment Variables
EXNESS_LOGIN = os.environ.get("EXNESS_LOGIN")
EXNESS_PASSWORD = os.environ.get("EXNESS_PASSWORD")
EXNESS_SERVER = os.environ.get("EXNESS_SERVER")

SYMBOL = "EURUSD"

@app.route('/')
def home():
    return f"Exness Trading Bot for {SYMBOL} is Active (EMA 9/21 Crossover Strategy)!"

def calculate_ema(prices, period):
    """የ EMA ዋጋን የሚያሰላ ተግባር"""
    multiplier = 2 / (period + 1)
    ema = sum(prices[:period]) / period
    for price in prices[period:]:
        ema = (price - ema) * multiplier + ema
    return ema

def run_trading_bot():
    print(f"=== Exness Auto-Trading Bot Started for {SYMBOL} (EMA Crossover Strategy) ===")
    print(f"Account ID: {EXNESS_LOGIN} | Server: {EXNESS_SERVER}")
    
    # ለሙከራ እና ለሎግ የሚረዱ ያለፉ የ EMA ዋጋዎች
    previous_ema9 = None
    previous_ema21 = None

    while True:
        try:
            print("\n-----------------------------------------")
            print(f"[{SYMBOL}] የ 15M ቻርት የ EMA 9 እና EMA 21 መቋረጥን በመፈተሽ ላይ...")
            
            # እዚህ ጋር ከ Exness/MetaTrader የቅርብ ጊዜ የ EURUSD ዋጋዎች ይወሰዳሉ
            # (ምሳሌ ያህል የአሁኑ የ EMA ስሌት)፦
            current_ema9 = 1.0860   # የአሁኑ EMA 9 ዋጋ
            current_ema21 = 1.0855  # የአሁኑ EMA 21 ዋጋ
            
            print(f"የአሁኑ EMA 9: {current_ema9} | የአሁኑ EMA 21: {current_ema21}")

            if previous_ema9 is not None and previous_ema21 is not None:
                # 1. Bullish Crossover (EMA 9 ወደ ላይ ሲያቋርጥ)
                if previous_ema9 <= previous_ema21 and current_ema9 > current_ema21:
                    print(">>> [BUY SIGNAL DETECTED!] EMA 9 EMA 21ን ወደ ላይ አቋርጧል! BUY Trade እየተከፈተ ነው...")
                    # እዚህ ጋር የ Exness BUY Trade መክፈቻ ኮድ ይፈጸማል

                # 2. Bearish Crossover (EMA 9 ወደ ታች ሲያቋርጥ)
                elif previous_ema9 >= previous_ema21 and current_ema9 < current_ema21:
                    print(">>> [SELL SIGNAL DETECTED!] EMA 9 EMA 21ን ወደ ታች አቋርጧል! SELL Trade እየተከፈተ ነው...")
                    # እዚህ ጋር የ Exness SELL Trade መክፈቻ ኮድ ይፈጸማል

                else:
                    print("EMA 9 እና EMA 21 ገና አልተቋረጡም፤ ቦቱ መጠበቁን ይቀጥላል...")
            else:
                print("የመጀመሪያውን የ EMA ዋጋ በመመዝገብ ላይ...")

            # ዋጋዎቹን ለቀጣዩ ዙር ማስታወስ
            previous_ema9 = current_ema9
            previous_ema21 = current_ema21

        except Exception as e:
            print(f"!!! Error in trading loop: {e}")

        # በየ 1 ደቂቃው ገበያውን ይፈትሻል
        time.sleep(60)

if __name__ == '__main__':
    # 1. Trading Thread
    bot_thread = threading.Thread(target=run_trading_bot)
    bot_thread.daemon = True
    bot_thread.start()

    # 2. Render Web Server
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
