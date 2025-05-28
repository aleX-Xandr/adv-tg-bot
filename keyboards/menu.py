import random

from aiogram.types import ChatAdministratorRights, KeyboardButtonRequestChat
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(
        text= "Добавить канал", 
        request_chat=KeyboardButtonRequestChat(
            user_administrator_rights=ChatAdministratorRights(
                is_anonymous=False,
                can_manage_video_chats=False,
                can_change_info=True,
                can_invite_users=True,
                can_restrict_members=True,
                can_manage_chat=True,
                can_promote_members=True,
                can_post_messages=True,
                can_edit_messages=True,
                can_delete_messages=True,
                can_pin_messages=True,
                can_post_stories=False,
                can_edit_stories=False,
                can_delete_stories=False
            ),
            bot_administrator_rights=ChatAdministratorRights(
                is_anonymous=False,
                can_manage_video_chats=False,
                can_change_info=True,
                can_invite_users=True,
                can_manage_chat=True,
                can_restrict_members=True,
                can_promote_members=True,
                can_post_messages=True,
                can_edit_messages=True,
                can_delete_messages=True,
                can_pin_messages=True,
                can_post_stories=False,
                can_edit_stories=False,
                can_delete_stories=False
            ),
            request_id=random.randrange(1, 1000000),
            chat_is_channel=True,
            chat_is_forum=False
        )
    )
    builder.button(text="Добавить пост")
    return builder.as_markup(resize_keyboard=True)
