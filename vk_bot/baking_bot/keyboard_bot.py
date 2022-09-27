from vk_api.keyboard import VkKeyboard
from alchemy_bot import baking_type, baking_products_title


def simple_keys_start():
    # menu = VkKeyboard(inline=True)  # каждая кнопка отдельно
    menu = VkKeyboard()
    menu.add_button('/Бот!')
    # menu.add_button("ИД 100", color="positive", payload={'A': 123, 'B': 777})
    # menu.add_button("ИД 101", color="positive")
    menu.add_line()
    menu.add_button("Выпечки", color="primary")
    # menu.add_button("ИД 3", color="positive")
    menu = menu.get_keyboard()
    return menu


def baking_buttons():
    array = baking_type()
    menu = VkKeyboard(inline=True)
    for button in array:
        menu.add_button(button.get('type'))
    menu = menu.get_keyboard()
    return menu


def baking_type_list():
    return [x.get('type') for x in baking_type()]


def baking_buttons_prod(text):
    array = baking_products_title(text)
    menu = VkKeyboard(inline=True)
    for button in array:
        menu.add_button(button[0])
    menu = menu.get_keyboard()
    return menu


# print(baking_buttons_prod(text='b'))
