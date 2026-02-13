import os
import time
import requests
from datetime import datetime
# ===== настройки из переменных окружения =====
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
CHAT_ID = os.getenv("CHAT_ID", "")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "60"))  # секунд
def send_telegram(text: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print("Telegram error:", e)


def main():
    send_telegram("✅ Spread-bot запущен и работает")

    counter = 0
    while True:
        counter += 1

        # ====== ЗАГЛУШКА ЛОГИКИ ======
        # Здесь позже подключим Excel / Google Sheets / API
        if counter % 6 == 0:
            send_telegram(
                f"📊 ТЕСТОВЫЙ СИГНАЛ\n"
                f"Время: {datetime.now().strftime('%H:%M:%S')}\n"
                f"Статус: ENTER"
            )
        # ============================

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
