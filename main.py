from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from handlers import start, post
from middlewares.access import AccessMiddleware
from utils.google_sheets import get_or_create_sheet

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.message.middleware(AccessMiddleware())
    dp.include_router(start.router)
    dp.include_router(post.router)
    print("BOT STARTED")
    get_or_create_sheet()
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())