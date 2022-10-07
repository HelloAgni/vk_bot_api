import datetime
import json
import os

import vk_api
from dotenv import load_dotenv
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id

from db import bot_commands, photo_bot, full_info
from exceptions import BotStop
from keyboard import *
from config import *

load_dotenv()

TOKEN = os.getenv('FULL_ACCESS')
GROUP_ID = os.getenv('GROUP_ID')


class Server:
    """Бот для сообществ"""
    NEW_MSG = VkBotEventType.MESSAGE_NEW

    def __init__(self, token, group_id):
        self.vk_session = vk_api.VkApi(token=token)
        self.long_poll = VkBotLongPoll(self.vk_session, group_id=group_id)
        self.vk = self.vk_session.get_api()

    def send_message(self, peer_id, keyboard=None, message=None,
                     attachment=None, payload=None):
        self.vk.messages.send(
            peer_id=peer_id, message=message,
            random_id=get_random_id(),
            attachment=attachment,
            keyboard=keyboard,
            payload=payload
        )

    def send_photo(self, peer_id, title=None):
        upload = VkUpload(self.vk_session)
        photo = upload.photo_messages(photo_bot(prod_title=title))  # Docker
        # photo = upload.photo_messages(photo_bot())  # Local
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        attachment = f'photo{owner_id}_{photo_id}_{access_key}'
        self.vk.messages.send(
            peer_id=peer_id,
            attachment=attachment,
            random_id=get_random_id(),
            message=f'{title}')

    def get_user_name(self, user_id):
        # Method 1: extract from vk
        return self.vk.users.get(
            user_ids=user_id)[0].get('first_name')
        # Method 2: extract from event and vk_session
        # user_name = self.vk_session.method(
        #     'users.get', {'user_ids': event.obj.message.get(
        #         "from_id")})[0].get('first_name')

    def get_user_city(self, user_id):
        # Method 1: extract from vk
        return self.vk.users.get(
            user_ids=user_id, fields="city")[0].get('city').get('title')
        # Method 2: extract from event and vk_session
        # user_city = self.vk_session.method(
        #     'users.get', {'user_ids': event.obj.message.get(
        #         "from_id"), 'fields': 'city'})[0].get('city').get('title')

    def start(self):
        print('Бот активирован')
        start_time = datetime.datetime.now()
        for event in self.long_poll.listen():
            if event.type == Server.NEW_MSG:
                # event.obj.message == event.message => True
                message = event.obj.message
                from_id = message.get('from_id')
                peer_id = message.get('peer_id')
                if message.get('text') == BOT_START:
                    self.send_message(
                        peer_id=peer_id,
                        message=(
                            f'{MSG_HI}\n'
                            f'{MSG_NAME} {self.get_user_name(user_id=from_id)}, '
                            f'{MSG_CITY} {self.get_user_city(user_id=from_id)}\n'
                        ),
                        keyboard=simple_keys_start(),
                    )
                elif message.get('text') == BOT_STOP:
                    self.send_message(
                        peer_id=event.message.get('peer_id'),
                        message=f'{MSG_STOP}'
                    )
                    raise BotStop  # => System Stop!
                elif message.get('payload'):
                    payload = event.message.get('payload')
                    if json.loads(payload).get('bot_button') == PL_BOT:
                        self.send_message(
                            peer_id=peer_id,
                            message=(
                                    f'{MSG_INFO}\n'
                                    f'{MSG_COMMANDS}\n'
                                    f'{bot_commands()}'),
                            keyboard=simple_keys_start()
                        )
                    if json.loads(payload).get('button_baking') == PL_DESSERT:
                        self.send_message(
                            peer_id=peer_id,
                            message=f'{MSG_CHOOSE}',
                            keyboard=baking_buttons(),
                        )
                    if json.loads(payload).get('type') in baking_type_list():
                        text = json.loads(payload).get('type')
                        self.send_message(
                            peer_id=peer_id,
                            message=f'{MSG_TYPE} {text}',
                            keyboard=baking_buttons_prod(text),
                        )
                    if json.loads(payload).get('title_button'):
                        prod = json.loads(payload).get('title_button')
                        items = full_info(prod=prod)
                        title = items.get('title')
                        self.send_photo(
                            peer_id=peer_id, title=title)
                        self.send_message(
                            peer_id=peer_id,
                            message=f'{MSG_DESC}\n'
                                    f'{items.get("desc")}'
                        )
                    if json.loads(payload).get('time_bot') == PL_TIME:
                        current_time = datetime.datetime.now() - start_time
                        h, m, s = str(current_time).split(':')
                        self.send_message(
                            peer_id=peer_id,
                            message=(
                                f'{MSG_TIME} \n'
                                f'{h}д. {m}м. {str(s).split(".")[0]}c.'),
                            keyboard=simple_keys_start(),
                        )


if __name__ == '__main__':
    server = Server(token=TOKEN, group_id=GROUP_ID)
    while True:
        try:
            server.start()
        except BotStop:
            break
        except Exception as e:
            print(f'Some error, do we need to fix it? -> {e}')
