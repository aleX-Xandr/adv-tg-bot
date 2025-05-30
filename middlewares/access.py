import json

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from typing import Callable, Dict, Any, Awaitable

from config import ADMINS_LIST

with open(ADMINS_LIST, "r", encoding="utf-8") as file:
    admins = json.load(file)


class AccessMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, Message):
            user_id = event.from_user.id
            if user_id not in admins:
                await event.answer("❌ У вас нет доступа к использованию этого бота.")
                return
        return await handler(event, data)