import os
import random

import vk_api
from dotenv import load_dotenv
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

load_dotenv()

TOKEN = os.getenv('ACCESS_TOKEN')
GROUP_ID = os.getenv('GROUP_ID')

vk_session = vk_api.VkApi(token=TOKEN)
long_poll = VkBotLongPoll(vk_session, GROUP_ID)

# Вызов методов vk_api
session_api = vk_session.get_api()


def send_message(session_api, peer_id, message=None,
                 attachment=None, keyboard=None, payload=None):
    session_api.messages.send(
        peer_id=peer_id, message=message,
        random_id=random.randint(-2147483648, +2147483648),
        attachment=attachment, keyboard=keyboard, payload=payload
    )


def get_user_name(user_id):
    return vk_session.users.get(user_id=user_id)[0].get('first_name')


def get_user_city(user_id):
    return vk_session.users.get(user_id=user_id, fields="city")[0].get('city').get('title')


# while True:
for event in long_poll.listen():
    obj = event.obj
    print('Main_event ->', event)
    print('1 ->', obj)
    # print('Else - 2 ->', vk_session.method('users.get', {'user_ids': obj.message.get("from_id")}))
    if event.type == VkBotEventType.MESSAGE_NEW:
        user_name = vk_session.method(
            'users.get', {'user_ids': obj.message.get(
                "from_id")})[0].get('first_name')
        user_city = vk_session.method(
            'users.get', {'user_ids': obj.message.get(
                "from_id"), 'fields': 'city'})[0].get('city').get('title')
        print('Имя ->', user_name)
        print('Город ->', user_city)
        print("В чате появилось новое сообщение!")
        send_message(
            session_api,
            peer_id=obj.message.get('peer_id'),
            message=f'Привет - Я бот, проверка связи. Ваш ID >> '
                    f'{obj.message.get("from_id")}\n'
                    f'Ваше имя: {user_name}, '
                    f'город {user_city}'
        )
        print('11->', get_user_name(obj.message.get("from_id")))
        print('22->', get_user_city(obj.message.get("from_id")))
    if event.type == VkBotEventType.WALL_POST_NEW:
        print('На стене появилась новая запись')
        send_message(
            session_api,
            peer_id=obj.from_id,
            message='Привет - Я бот, проверка связи!!!')
    else:
        print('Else type ->', event.type)
