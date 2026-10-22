"""
Конфигурация бота.
"""
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "8866849877:AAGCru1pDKU-NRVR7JTXlpm_7RKbFK9PSec")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID", "1242592772"))
ADMIN_IDS = [int(uid.strip()) for uid in os.getenv("ADMIN_IDS", "1242592772").split(",") if uid.strip()]
DB_PATH = os.getenv("DB_PATH", "orders.db")
DEFAULT_CARD_NUMBER = os.getenv("CARD_NUMBER", "9860082520089739")
ADMIN_CONTACTS = os.getenv("ADMIN_CONTACTS", "@realkass")
WITHDRAW_VIDEO_FILE_ID = os.getenv("WITHDRAW_VIDEO_FILE_ID", "")

# Канал для подписки (не обязательная)
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "0"))
CHANNEL_URL = os.getenv("CHANNEL_URL", "https://t.me/your_channel")
CHANNEL_NAME = os.getenv("CHANNEL_NAME", "канал")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан.")
if not ADMIN_IDS:
    raise RuntimeError("ADMIN_IDS не задан.")
