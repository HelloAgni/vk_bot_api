import os

import vk_api
from dotenv import load_dotenv
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
# import random
from vk_api.utils import get_random_id

load_dotenv()

TOKEN = os.getenv('ACCESS_TOKEN')
GROUP_ID = os.getenv('GROUP_ID')

# vk_session = vk_api.VkApi(token=TOKEN)
# long_poll = VkBotLongPoll(vk_session, GROUP_ID)

# session_api = vk_session.get_api()


class Server:
    """Бот для сообществ"""

    def __init__(self, token, group_id):
        self.vk_session = vk_api.VkApi(token=token)
        self.long_poll = VkBotLongPoll(self.vk_session, group_id=group_id)
        self.session_api = self.vk_session.get_api()

    def send_message(self, peer_id, message=None,
                     attachment=None, keyboard=None, payload=None):
        self.session_api.messages.send(
            peer_id=peer_id, message=message,
            # random_id=random.randint(-2147483648, +2147483648),
            random_id=get_random_id(),
            attachment=attachment, keyboard=keyboard, payload=payload
        )

    def get_user_name(self, user_id):
        return self.session_api.users.get(
            user_ids=user_id)[0].get('first_name')

    def get_user_city(self, user_id):
        return self.session_api.users.get(
            user_ids=user_id, fields="city")[0].get('city').get('title')

    def start(self):
        for event in self.long_poll.listen():
            obj = event.obj
            print('Main_event ->', event)
            print('1 ->', obj)
            # print('Else - 2 ->', vk_session.method('users.get', {'user_ids': obj.message.get("from_id")}))
            if event.type == VkBotEventType.MESSAGE_NEW and obj.message.get(
                    'text') == '/stop!':
                self.send_message(
                    # session_api=self.session_api,
                    peer_id=obj.message.get('peer_id'),
                    message=f'Бот Вас покидает, выполнена команда - STOP'
                )
                return print('Бот остановлен!')
            if event.type == VkBotEventType.MESSAGE_NEW:
                user_name = self.vk_session.method(
                    'users.get', {'user_ids': obj.message.get(
                        "from_id")})[0].get('first_name')
                user_city = self.vk_session.method(
                    'users.get', {'user_ids': obj.message.get(
                        "from_id"), 'fields': 'city'})[0].get('city').get('title')
                print("В чате появилось новое сообщение!")
                self.send_message(
                    # session_api=self.session_api,
                    peer_id=obj.message.get('peer_id'),
                    message=f'Привет - Я бот, проверка связи. Ваш ID >> '
                            f'{obj.message.get("from_id")}\n'
                            f'Ваше имя: {user_name}, '
                            f'город {user_city}'
                )
                # print('11->', self.get_user_name(obj.message.get("from_id")))
                # print('22->', self.get_user_city(obj.message.get("from_id")))
            if event.type == VkBotEventType.WALL_POST_NEW:
                print('На стене появилась новая запись')
                self.send_message(
                    # session_api=self.session_api,
                    peer_id=obj.from_id,
                    message='Привет - Я бот, проверка связи!!!')
            else:
                print('Else type ->', event.type)


if __name__ == '__main__':
    server = Server(token=TOKEN, group_id=GROUP_ID)
    server.start()
