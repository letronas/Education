class Viber:
    _message_list = []
    
    @classmethod
    def add_message(cls, msg):
        cls._message_list.append(msg)
    
    @classmethod
    def remove_message(cls, msg):
        cls._message_list.remove(msg)
    
    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like
    
    @classmethod
    def show_last_message(cls, num):
        for i in cls._message_list[-num:]:
            print(i.text, i.fl_like)
    
    @classmethod
    def total_messages(cls):
        return len(cls._message_list)


class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.show_last_message(10)
Viber.set_like(msg)
# Viber.show_last_message(10)
Viber.remove_message(msg)
# Viber.show_last_message(10)
