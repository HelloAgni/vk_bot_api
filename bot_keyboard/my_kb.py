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


# def carousel_keys():
#     carousel = {
#         "type": "carousel",
#         "elements": [{
#             "photo_id": "215977715_457239022",
#             "title": "Заголовок",
#             "description": "Описание",
#             "action": {
#                 "type": "open_link",
#                 "link": "https://dev.vk.com/guide"
#             },
#             "buttons": [
#                     ["action": {
#                         "type": "text",
#                         "label": "Текст кнопки 🌚",
#                         "payload": "{'a':123}"
#                     }],
#                     ["action": {
#                         "type": "open_link",
#                         "link": "ссылка",
#                         "label": "Текст кнопки 🌚",
#                         "payload": "{'b':777}"
#                     }]
#                 }
#             ]
#         }]
#     }
#     carousel = json.dumps(carousel, ensure_ascii=False).encode('utf-8')
#     carousel = str(carousel.decode('utf-8'))
#     return carousel
