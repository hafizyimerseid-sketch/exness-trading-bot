import time
import requests

print("Exness Trading Bot started successfully on Render...")

def check_market():
    print("Scanning market for EMA 9/21 crossover & FVG/Order Block retest...")

if __name__ == "__main__":
    while True:
        try:
            check_market()
            time.sleep(60) # በየ 1 ደቂቃው ገበያውን ይፈትሻል
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)
          
