import os
import time
from telegram import Bot
from telegram.error import TelegramError

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=BOT_TOKEN)

def send_message(chat_id, text):
    try:
        bot.send_message(chat_id=chat_id, text=text)
    except TelegramError as e:
        print(f"Error: {e}")

print("Aesthify Manager Bot Started...")

while True:
    try:
        send_message(ADMIN_ID, "Bot is Running...")
    except Exception as e:
        print(f"Loop Error: {e}")
    time.sleep(30)
