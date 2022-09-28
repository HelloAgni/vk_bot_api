from vk_api.keyboard import VkKeyboard
from alchemy_bot import baking_type, baking_products_title


def simple_keys_start():
    # menu = VkKeyboard(inline=True)  # каждая кнопка отдельно
    menu = VkKeyboard()
    menu.add_button(
        'Бот!', payload={'bot_button': 'Бот!'})
    # menu.add_button('Бот!', payload={'my_bot': True})
    menu.add_line()
    menu.add_button(
        'Выпечки', color='primary', payload={'button_baking': 'Выпечки'})
    menu.add_line()
    menu.add_button(
        "New button", color="primary", payload={'new': 'New button'})
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
