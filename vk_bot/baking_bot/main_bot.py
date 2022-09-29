import os
import json
import vk_api
from dotenv import load_dotenv
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id
from alchemy_bot import bot_commands, photo_bot, full_info
from keyboard_bot import simple_keys_start, baking_buttons, baking_type_list, baking_buttons_prod

load_dotenv()

TOKEN = os.getenv('FULL_ACCESS')
GROUP_ID = os.getenv('GROUP_ID')


class Server:
    """Бот для сообществ"""
    NEW_MSG = VkBotEventType.MESSAGE_NEW  # chat message
    REPLY_MSG = VkBotEventType.MESSAGE_REPLY  # private message

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

    def send_photo(self, peer_id):
        upload = VkUpload(self.vk_session)
        photo = upload.photo_messages(photo_bot())
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        attachment = f'photo{owner_id}_{photo_id}_{access_key}'
        self.vk.messages.send(
            peer_id=peer_id,
            attachment=attachment,
            random_id=get_random_id(),
            message='Лови картинку')

    def get_user_name(self, user_id):
        return self.vk.users.get(
            user_ids=user_id)[0].get('first_name')
        # extract from event
        # user_name = self.vk_session.method(
        #     'users.get', {'user_ids': event.obj.message.get(
        #         "from_id")})[0].get('first_name')

    def get_user_city(self, user_id):
        return self.vk.users.get(
            user_ids=user_id, fields="city")[0].get('city').get('title')
        # extract from event
        # user_city = self.vk_session.method(
        #     'users.get', {'user_ids': event.obj.message.get(
        #         "from_id"), 'fields': 'city'})[0].get('city').get('title')

    def start(self):
        for event in self.long_poll.listen():
            print('Main_event ->', event)
            if (event.type == Server.NEW_MSG and event.obj.message.get(
                    'text') == '/стоп!'):
                self.send_message(
                    peer_id=event.obj.message.get('peer_id'),
                    message=f'Бот Вас покидает, выполнена команда - STOP'
                )
                return print('Бот остановлен!')
            elif (event.type == Server.NEW_MSG and event.obj.message.get(
                    'text') == '/Бот!'):
                message = event.obj.message
                user_id = message.get('from_id')
                peer_id = message.get('peer_id')
                self.send_message(
                    peer_id=peer_id,
                    message=(
                        f'Привет - Я Бот\n'
                        f'Ваше имя {self.get_user_name(user_id=user_id)}, '
                        f'Вы из города {self.get_user_city(user_id=user_id)}\n'
                        f'Доступные команды: {bot_commands()}'),
                    keyboard=simple_keys_start(),
                )
            elif event.type == Server.NEW_MSG and (json.loads(event.message.get(
                        'payload')).get('bot_button') == 'Бот!'):
                self.send_message(
                    peer_id=event.message.get('peer_id'),
                    message='Бот запущен, все в порядке'
                )
            elif event.type == Server.NEW_MSG and (json.loads(
                    event.message.get(
                        'payload')).get('button_baking') == 'Выпечки'):
                self.send_message(
                    peer_id=event.message.get('peer_id'),
                    message='Выбирайте тип выпечки',
                    keyboard=baking_buttons(),
                )
            elif event.type == Server.NEW_MSG and (json.loads(
                    event.message.get(
                        'payload')).get('type')) in baking_type_list():
                text = json.loads(
                    event.message.get(
                        'payload')).get('type')
                self.send_message(
                    peer_id=event.message.get('peer_id'),
                    message=f'Выбран тип: {text}',
                    keyboard=baking_buttons_prod(text),
                )
            elif event.type == Server.NEW_MSG and json.loads(
                    event.message.get(
                        'payload')).get('title_button'):
                prod = json.loads(
                    event.message.get(
                        'payload')).get('title_button')
                items = full_info(prod=prod)
                self.send_message(
                    peer_id=event.message.get('peer_id'),
                    message=f'Вы дошли до описания продукта...\n'
                            f'Название: {items.get("title")}\n'
                            f'Описание: {items.get("desc")}'
                    # keyboard=baking_buttons_prod(text),
                    # payload=[],
                )
                self.send_photo(peer_id=event.obj.message.get("peer_id"))
            elif (event.type == Server.NEW_MSG and event.obj.message.get(
                    'text') == '/картинку!'):
                self.send_photo(
                    peer_id=event.obj.message.get("peer_id"))
            else:
                print('Else type ->', event.type)


if __name__ == '__main__':
    server = Server(token=TOKEN, group_id=GROUP_ID)
    server.start()
