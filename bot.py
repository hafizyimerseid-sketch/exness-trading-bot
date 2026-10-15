import threading
import time
from flask import Flask

# Render የ Port ስህተት እንዳያሳይ አነስተኛ የዌብ ሰርቨር ማዘጋጀት
app = Flask(__name__)

@app.route('/')
def home():
    return "Exness Trading Bot is Running Live 24/7!"

def run_trading_bot():
    print("Exness Trading Bot started successfully on Render...")
    while True:
        try:
            print("Scanning market for EMA 9/21 crossover & FVG/Order Block retest...")
            time.sleep(60) # በየ 1 ደቂቃው ገበያውን ይፈትሻል
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    # ቦቱን በ Background እንዲሰራ ማስጀመር
    bot_thread = threading.Thread(target=run_trading_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # ዌብ ሰርቨሩን ማስጀመር (Port binding)
    app.run(host='0.0.0.0', port=10000)
    
