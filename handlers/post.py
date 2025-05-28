import datetime

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from config import DAYS_DELTA
from keyboards.confirm import confirm_kb
from keyboards.menu import main_menu
from keyboards.post import brand_kb, company_kb
from keyboards.skip import skip_kb
from utils.channel_store import load_channels
from utils.google_sheets import append_row


router = Router()

class PostStates(StatesGroup):
    date = State()
    invoice = State()
    brand = State()
    manufacturer = State()
    photos = State()
    price = State()


async def send_post(bot, chat_id, data) -> Message:

    text = f"""Күні: {data['date']}
Жүкқұжат: {data['invoice']}
Бренд: {data['brand']}
Өндіруші: {data['manufacturer']}
Фотосуреттер саны: {len(data['photos'])}
Қорап бағасы: {data['price']}

Дата: {data['date']}
Накладная: {data['invoice']}
Бренд: {data['brand']}
Производитель: {data['manufacturer']}
Количество фото: {len(data['photos'])}
Цена за коробку: {data['price']}"""
    
    if data['photos']:
        media_group = [InputMediaPhoto(media=file_id, caption=text if i == 0 else None) for i, file_id in enumerate(data['photos'])]
        messages = await bot.send_media_group(chat_id, media_group) # send_photo(chat_id, photo=last_photo, caption=text)
        message = messages[0]
    else:
        message = await bot.send_message(chat_id, text)
    return message

@router.message(F.text == "Добавить пост")
async def start_post(message: Message, state: FSMContext):
    await message.answer("Введите дату в формате ДД.ММ.ГГГГ:")
    await state.set_state(PostStates.date)

@router.message(PostStates.date)
async def get_date(message: Message, state: FSMContext):
    try:
        datetime.datetime.strptime(message.text, "%d.%m.%Y")
        user_date = datetime.datetime.strptime(message.text, "%d.%m.%Y").date()
        current_date = datetime.datetime.now().date()
        delta_date = current_date - user_date
        if delta_date.days > DAYS_DELTA:
            await message.answer("Дата слишком старая. Введите дату не старше 2 дней от текущей.")
            return

        await state.update_data(date=message.text)
        await message.answer("Введите идентификатор накладной:")
        await state.set_state(PostStates.invoice)
    except ValueError:
        await message.answer("Неверный формат. Повторите в формате ДД.ММ.ГГГГ")

@router.message(PostStates.invoice)
async def get_invoice(message: Message, state: FSMContext):
    await state.update_data(invoice=message.text)
    await message.answer("Введите бренд:", reply_markup=brand_kb)
    await state.set_state(PostStates.brand)

@router.callback_query(PostStates.brand, F.data.startswith("brand:"))
async def get_brand_callback(callback: CallbackQuery, state: FSMContext):
    brand = callback.data.split(":", 1)[1]
    await state.update_data(brand=brand)
    await callback.message.edit_text("Выберите производителя:", reply_markup=company_kb)
    await state.set_state(PostStates.manufacturer)
    await callback.answer()

@router.callback_query(PostStates.manufacturer, F.data.startswith("company:"))
async def get_manufacturer_callback(callback: CallbackQuery, state: FSMContext):
    manufacturer = callback.data.split(":", 1)[1]
    await state.update_data(manufacturer=manufacturer)
    await callback.message.edit_text("Загрузите фото (или нажмите 'Пропустить')", reply_markup=skip_kb)
    await state.set_state(PostStates.photos)
    await state.update_data(photos=[])

@router.message(PostStates.photos, F.photo)
async def collect_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    data["photos"].append(message.photo[-1].file_id)
    await state.update_data(photos=data["photos"])
    await message.answer("Добавьте ещё или нажмите 'Пропустить'")

@router.callback_query(PostStates.photos, F.data == "skip_photo")
async def skip_photo(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите цену за коробку:")
    await state.set_state(PostStates.price)
    await callback.answer()

@router.callback_query(F.data == "skip_photo")
async def skip_photo(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    callback.message.answer()

@router.message(PostStates.price)
async def get_price(message: Message, state: FSMContext):

    await state.update_data(price=message.text)
    data = await state.get_data()

    await send_post(message.bot, message.from_user.id, data)
    await message.answer(
        "Вот превью бота, подтвердите начало рассылки если все указано верно:",
        reply_markup=confirm_kb
    )


@router.callback_query(F.data == "approve_send_post")
async def skip_photo(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Начинаю рассылку...")
    data = await state.get_data()
    channels = load_channels()
    post_links = []
    for channel in channels:
        message = await send_post(callback.bot, channel, data)
        if message.chat.username:
            chat_link = message.chat.username
        else:
            chat_link = "c/{}".format(str(channel).replace("-100", ""))
        post_links.append(f"https://t.me/{chat_link}/{message.message_id}")


    append_row([
        data['date'],
        data['invoice'],
        data['brand'],
        data['manufacturer'],
        len(data['photos']),
        data['price'],
        "\n".join(post_links)
    ])

    await callback.message.answer("Пост отправлен по всем каналам ✅", reply_markup=main_menu())
    await state.clear()
    await callback.answer()

@router.callback_query(F.data == "cancel_send_post")
async def cancel_post(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text("Публикация отменена ❌", reply_markup=main_menu())
    await callback.answer()
