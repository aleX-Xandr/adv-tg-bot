from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirm_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Подтвердить", callback_data="approve_send_post"),
            InlineKeyboardButton(text="❌ Отменить", callback_data="cancel_send_post")
        ]
    ]
)
