from dotenv import load_dotenv
import os

load_dotenv() 

BOT_TOKEN = os.getenv("BOT_TOKEN")
DAYS_DELTA = int(os.getenv("DAYS_DELTA"))

GOOGLE_SHEET_CREDS = "data/creds.json"
ADMINS_LIST = "data/admins.json"
SPREADSHEET_NAME = "TelegramPostsV2"
CHANNELS_FILE = "data/channels.json"
KEYBOARD_CONFIG_FILE = "data/config.json"
