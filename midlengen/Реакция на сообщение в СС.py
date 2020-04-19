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

a = 1

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print("User: vk.com/id"+str(event.user_id))
        response = event.text.lower()
        if event.from_user and not (event.from_me):
            if response == "привет":
                vk_session.method('messages.send',{'user_id': event.user_id, 'message': 'Привет, друг!', 'random_id': 0})
            elif response == "пока":
                    vk_session.method('messages.send',{'user_id': event.user_id, 'message': 'Пока, друг!', 'random_id': 0})