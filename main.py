from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers import start, post
from utils.google_sheets import get_or_create_sheet

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(post.router)
    print("BOT STARTED")
    get_or_create_sheet()
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())