token = "vk1.a.FL1Vfd9hw12iJSHVN7kBehYkTBGcRIJaFLd9SFootY2eaaf1Gc9qmFAUXUQKEr4-eoBkVWrHMZWrhtU0lBeUNMnVxKFE-Lwp94kvrZGFkreRpY8S8SgF9MQXHFmXPRXwG45zAk6sFDeaL4iycXWOTdeDGfWcmRRMraWFD8pw8kRuSaZagA6FK-pJ7KJYh0Tj4XJq0H-WEEIQ-wnkoDRCfQ"
from cbrf import get_course
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from wiki import get_article

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    print(event)
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_message = event.text.lower()
        user_id = event.user_id
        if user_message[:2] == "-k":
            response = 'Доллар стоит {0} руб.\nЕвро стоит {1} руб.\nЮань стоит {2} руб.'.format(
                get_course("R01235"), get_course("R01239"), get_course("R01375")
            )
        elif user_message[:2] == '-v':
            article = user_message[2:]
            response = get_article(article=article)
        else:
            response = 'Такой комманды я не знаю'
        vk.messages.send(
            user_id=user_id,
            message=response,
            random_id=random.randint(-10**7, 10**7)
        )
