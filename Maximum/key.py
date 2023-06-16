token = "vk1.a.FL1Vfd9hw12iJSHVN7kBehYkTBGcRIJaFLd9SFootY2eaaf1Gc9qmFAUXUQKEr4-eoBkVWrHMZWrhtU0lBeUNMnVxKFE-Lwp94kvrZGFkreRpY8S8SgF9MQXHFmXPRXwG45zAk6sFDeaL4iycXWOTdeDGfWcmRRMraWFD8pw8kRuSaZagA6FK-pJ7KJYh0Tj4XJq0H-WEEIQ-wnkoDRCfQ"
from cbrf import get_course
import vk_api
import random

while True:
    vk = vk_api.VkApi(token=token)

    messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
    if messages['count'] > 0:
        message_text = messages['items'][0]['last_message']['text']
        if message_text == "курс":
            answer = f"Курс доллара на сегодня составляет: {get_course()} руб."
        else:
            answer = "Неизвестная комманда"
        user_id = messages['items'][0]['last_message']['from_id']
        random_id = random.randint(-10**7, 10**7)
    
        vk.method("messages.send", {
            "user_id": user_id,
            "random_id": random_id,
            "message": answer
        })

