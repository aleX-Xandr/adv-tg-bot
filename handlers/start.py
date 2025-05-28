from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards.menu import main_menu
from utils.channel_store import save_channel

router = Router()

@router.message(F.text == "/start")
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Главное меню", reply_markup=main_menu())

@router.message(F.chat_shared)
async def channel_shared(message: Message):
    chat_id = message.chat_shared.chat_id
    save_channel(chat_id)
    await message.answer(f"Канал добавлен: {chat_id}")
