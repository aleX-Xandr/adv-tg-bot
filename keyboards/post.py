import json

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta

from config import KEYBOARD_CONFIG_FILE, DAYS_DELTA
with open(KEYBOARD_CONFIG_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

def build_keyboard_from_list(items: list[str], prefix: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=item, callback_data=f"{prefix}:{item}")]
        for item in items
    ])
    return keyboard


class PostKeyboards:
    brand_kb = build_keyboard_from_list(data.get("brand", []), prefix="brand")
    company_kb = build_keyboard_from_list(data.get("company", []), prefix="company")

    @staticmethod
    def date_kb():
        today = datetime.now().date()
        date_range =  [
            (today - timedelta(days=i)).isoformat()
            for i in range(DAYS_DELTA + 1)
        ]
        return build_keyboard_from_list(date_range, prefix="date")