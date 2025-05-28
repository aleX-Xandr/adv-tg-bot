import json
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import KEYBOARD_CONFIG_FILE
with open(KEYBOARD_CONFIG_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

def build_keyboard_from_list(items: list[str], prefix: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=item, callback_data=f"{prefix}:{item}")]
        for item in items
    ])
    return keyboard

brand_kb = build_keyboard_from_list(data.get("brand", []), prefix="brand")
company_kb = build_keyboard_from_list(data.get("company", []), prefix="company")