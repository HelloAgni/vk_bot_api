from vk_api.keyboard import VkKeyboard


def simple_keys():
    # menu = VkKeyboard(inline=True)  # каждая кнопка отдельно
    menu = VkKeyboard()
    menu.add_button('Without label')
    menu.add_button("ИД 100", color="positive", payload={'A': 123, 'B': 777})
    menu.add_button("ИД 101", color="positive")
    menu.add_line()
    menu.add_button("ИД 2", color="primary")
    menu.add_button("ИД 3", color="positive")
    menu = menu.get_keyboard()
    return menu

