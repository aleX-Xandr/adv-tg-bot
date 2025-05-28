from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

skip_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пропустить", callback_data="skip_photo")]
    ]
)
