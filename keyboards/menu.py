import random

from aiogram.types import ChatAdministratorRights, KeyboardButtonRequestChat
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_menu():
    random_id = random.randrange(1, 10000000)
    builder = ReplyKeyboardBuilder()
    builder.button(
        text= "Добавить группу", 
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
                # can_manage_topics=True
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
                #can_manage_topics=True
            ),
            request_id=random_id,
            chat_is_channel=False,
            chat_is_forum=False,
        )
    ).button(
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
            request_id=random_id+1,
            chat_is_channel=True,
            chat_is_forum=False
        )
    )
    builder.button(text="Добавить пост")
    return builder.adjust(2).as_markup(resize_keyboard=True)
