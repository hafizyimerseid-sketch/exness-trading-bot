import os
import time
import threading
import yfinance as yf
from flask import Flask

app = Flask(__name__)

SYMBOL = "EURUSD=X"

@app.route('/')
def home():
    return "Exness Trading Signal Bot with Real Market Data is Active!"

def check_ema_crossover():
    print("=== Exness Real-Time Trading Bot Started ===")
    
    while True:
        try:
            print("\n-----------------------------------------")
            print("የቀጥታ የ EURUSD ገበያ ዋጋዎችን ከ Yahoo Finance በመውሰድ ላይ...")
            
            # ያለፉትን የ 15 ደቂቃ ሻማዎች (15m Candles) መረጃ ያወርዳል
            data = yf.download(tickers=SYMBOL, period="1d", interval="15m")
            
            if not data.empty and len(data) >= 21:
                # EMA 9 እና EMA 21 ማሰላት
                data['EMA9'] = data['Close'].ewm(span=9, adjust=False).mean()
                data['EMA21'] = data['Close'].ewm(span=21, adjust=False).mean()

                last_ema9 = float(data['EMA9'].iloc[-1])
                last_ema21 = float(data['EMA21'].iloc[-1])
                prev_ema9 = float(data['EMA9'].iloc[-2])
                prev_ema21 = float(data['EMA21'].iloc[-2])

                print(f"የአሁኑ EMA 9: {last_ema9:.5f} | EMA 21: {last_ema21:.5f}")

                # 1. Bullish Crossover (BUY)
                if prev_ema9 <= prev_ema21 and last_ema9 > last_ema21:
                    print(">>> [BUY SIGNAL DETECTED!] EMA 9 EMA 21ን ወደ ላይ አቋርጧል!")
                    # እዚህ ጋር Trade መክፈቻ ጥሪ ይደረጋል

                # 2. Bearish Crossover (SELL)
                elif prev_ema9 >= prev_ema21 and last_ema9 < last_ema21:
                    print(">>> [SELL SIGNAL DETECTED!] EMA 9 EMA 21ን ወደ ታች አቋርጧል!")
                    # እዚህ ጋር Trade መክፈቻ ጥሪ ይደረጋል
                else:
                    print("EMA መስመሮቹ ገና አልተቋረጡም፤ ቦቱ በንቃት እየጠበቀ ነው...")
            else:
                print("በቂ የገበያ መረጃ ማግኘት አልተቻለም...")

        except Exception as e:
            print(f"Error in Trading Loop: {e}")

        # በየ 1 ደቂቃው ገበያውን ይፈትሻል
        time.sleep(60)

if __name__ == '__main__':
    t = threading.Thread(target=check_ema_crossover)
    t.daemon = True
    t.start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
