import time
import os
from flask import Flask # ዌብ ሰርቨሩ በ Render እንዲሰቅል የሚረዳ (ካለዎት)

app = Flask(__name__)

@app.route('/')
def home():
    return "Exness Trading Bot is running live!"

# የትሬዲንግ ሎጂክ እና ሉፕ (Loop) የሚሰራበት ዋናው ክፍል
def run_trading_bot():
    print(">>> ትሬዲንግ ቦቱ መሥራት ጀምሯል! (Trading Bot Started)")
    
    while True:
        try:
            print("\n-----------------------------------------")
            print("--- ገበያውን በመፈተሽ ላይ... (Checking Market) ---")
            
            # እዚህ ጋር የ Exness ዋጋን እና አመልካቾችን (RSI/EMA) የሚቀበልበት ኮድዎ ይኖራል
            # ምሳሌ ያህል፦
            current_price = 1.0855  # ከ Exness የሚመጣው ዋጋ
            current_rsi = 35.5      # የ RSI ዋጋ
            
            print(f"የአሁኑ የ EURUSD ዋጋ: {current_price} | RSI: {current_rsi}")
            
            # የ ግዢ (Buy) ወይም ሽያጭ (Sell) ሁኔታዎችን ማረጋገጥ
            if current_rsi < 30:
                print(">>> [BUY SIGNAL] RSI ከ 30 በታች ወርዷል! ትሬድ ሊከፈት ነው...")
                # እዚህ ጋር ትሬድ የሚከፍትበት ኮድዎ ይጻፋል
                
            elif current_rsi > 70:
                print(">>> [SELL SIGNAL] RSI ከ 70 በላይ ወጥቷል! ትሬድ ሊከፈት ነው...")
                # እዚህ ጋር ሽያጭ የሚከፍትበት ኮድዎ ይጻፋል
                
            else:
                print("ስታንዳርዱ አሁንም አልተሟላም፤ ቦቱ መጠበቁን ይቀጥላል...")

        except Exception as e:
            print(f"!!! ስህተት አጋጥሟል (Error): {e}")

        # ቀጣዩን ምርመራ ከማድረጉ በፊት ለተወሰነ ደቂቃ (ለምሳሌ 60 ሰከንድ) ማቆም
        time.sleep(60)

if __name__ == '__main__':
    # ቦቱ ከሰርቨሩ ጋር በአንድ ጊዜ እንዲሰራ (Threading) ማድረግ ከፈለጉ እዚህ ይጨመራል
    import threading
    bot_thread = threading.Thread(target=run_trading_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Render ዌብ ሰርቨሩን እንዲያገኘው ማሰራት
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
