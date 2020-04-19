import sys

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time

token = "cc3b3d00ba89b971211aa28078bad88405d4f9dba2fa3b4540917739edfa5c7dde334070565cb70c8f3e9"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)


def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'клава':

        keyboard.add_button('Нажми, чтобы управлять ', color=VkKeyboardColor.NEGATIVE)

    elif response == 'одежда':
        keyboard.add_button('Одежда', color=VkKeyboardColor.POSITIVE)

    elif response == 'меню':
        keyboard.add_button('Меню', color=VkKeyboardColor.POSITIVE)

    elif response == 'секс':
        keyboard.add_button('Тут будет секс', color=VkKeyboardColor.POSITIVE)

    elif response == 'закрыть':
        print('закрываю клаву')
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard


def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print('Ссылка на пользователя: vk.com/id'+str(event.user_id))
        response = event.text.lower()
        keyboard = create_keyboard(response)

        if event.from_user and not event.from_me:
            if response == "одежда":
                send_message(vk_session, 'user_id', event.user_id, message='Нажми на кнопку', keyboard=keyboard)
            elif response == "меню":
                send_message(vk_session, 'user_id', event.user_id, message='Нажми на кнопку',keyboard=keyboard)
            elif response == "клава":
                send_message(vk_session, 'user_id', event.user_id, message= 'Открываю клаву',keyboard=keyboard)

            elif response == "секс":
                send_message(vk_session, 'user_id', event.user_id, message='Жми на кнопку', keyboard=keyboard)

            elif response=='закрыть':
                send_message(vk_session, 'user_id', event.user_id, message='Закрыть',keyboard=keyboard)