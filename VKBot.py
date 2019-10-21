# coding: utf8
import time
import vk_api.longpoll
from vk_api.longpoll import VkEventType
import GameMaster


def getSession():
    while (True):
        try:
            file = open("token.conf", "r")
            token = file.read()
            return vk_api.vk_api.VkApi(token=token)
        except Exception as exc:
            time.sleep(10)


session = getSession()
vk = session.get_api()
longpoll = vk_api.longpoll.VkLongPoll(session)

GM = GameMaster.GameMaster()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.from_user and event.text:
        try:
            result = GM.sendMessage(event.text, event.user_id)
            vk.messages.send(user_id=event.user_id, message=result, random_id=time.time())
        except Exception as e:
            vk.messages.send(user_id=event.user_id, message="Непредвиденная ошибка", random_id=time.time())
            print(e)