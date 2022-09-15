import os
import random

import vk_api
from dotenv import load_dotenv
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

load_dotenv()

TOKEN = os.getenv('ACCESS_TOKEN')
GROUP_ID = os.getenv('GROUP_ID')

vk_session = vk_api.VkApi(token=TOKEN)
session_api = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, GROUP_ID)


def send_message(session_api, peer_id, message=None,
                 attachment=None, keyboard=None, payload=None):
    session_api.messages.send(
        peer_id=peer_id, message=message,
        random_id=random.randint(-2147483648, +2147483648),
        attachment=attachment, keyboard=keyboard, payload=payload
    )


# while True:
for event in longpoll.listen():
    print('1 ->', event)
    print('1.1 ->', event.obj)
    if event.type == VkBotEventType.MESSAGE_NEW:
        print('Chat-2 ->', event.obj.get('peer_id'))
        print('Chat-1 ->', event.message.get('peer_id'))
        print("В чате появилось новое сообщение!")
        send_message(
            session_api,
            peer_id=event.message.get('peer_id'),
            # message='Привет, {0}!'.format(last_and_first_name))
            message=f'Привет - Я бот, проверка связи ID >>'
                    f'{event.message.get("from_id")}')
    if event.type == VkBotEventType.WALL_POST_NEW:
        print('На стене появилась новая запись')
        send_message(
            session_api,
            peer_id=event.object.from_id,
            # message='Привет, {0}!'.format(last_and_first_name))
            message='Привет - Я бот, проверка связи!!!')
    # if event.type == VkBotEventType.LIKE_ADD:
    #     print('Лайкнули запись!')
