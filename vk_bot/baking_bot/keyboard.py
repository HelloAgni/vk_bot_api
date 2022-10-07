from vk_api.keyboard import VkKeyboard

from db import baking_type, baking_products_title
from config import *


def simple_keys_start():
    menu = VkKeyboard()
    menu.add_button(
        'Команды', payload={'bot_button': PL_BOT})
    menu.add_line()
    menu.add_button(
        'Десерты', color='primary', payload={'button_baking': PL_DESSERT})
    menu.add_line()
    menu.add_button(
        'Длительность работы Бота', color='primary', payload={'time_bot': PL_TIME})
    menu = menu.get_keyboard()
    return menu


def baking_buttons():
    array = baking_type()
    menu = VkKeyboard(inline=True)
    for button in array:
        menu.add_button(button.get('type'), payload=button)
    menu = menu.get_keyboard()
    return menu


def baking_type_list():
    return [x.get('type') for x in baking_type()]
    # ['a', 'b', 'c', 'd', 'e']


def baking_buttons_prod(text):
    array = baking_products_title(text)
    # [('asdasd',), ('bbb',)]
    menu = VkKeyboard(inline=True)
    for button in [','.join(x) for x in array]:  # ['asdasd', 'bbb']
        menu.add_button(button, payload={'title_button': button})
    menu = menu.get_keyboard()
    return menu


# print(baking_buttons_prod(text='b'))
# print(baking_type_list())
