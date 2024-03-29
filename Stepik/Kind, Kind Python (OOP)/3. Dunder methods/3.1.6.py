"""
Подвиг 6. Вам необходимо написать программу описания музеев. Для этого нужно объявить класс Museum, объекты которого формируются командой:

mus = Museum(название музея)
В объектах этого класса должны формироваться следующие локальные атрибуты:

name - название музея (строка);
exhibits - список экспонатов (изначально пустой список).

Сам класс Museum должен иметь методы:

add_exhibit(self, obj) - добавление нового экспоната в музей (в конец списка exhibits);
remove_exhibit(self, obj) - удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)
get_info_exhibit(self, indx) - получение информации об экспонате (строка) по индексу списка (нумерация с нуля).

Экспонаты представляются объектами своих классов. Для примера объявите в программе следующие классы экспонатов:

Picture - для картин;
Mummies - для мумий;
Papyri - для папирусов.

Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):

p = Picture(название, художник, описание)            # локальные атрибуты: name - название; author - художник; descr - описание
m = Mummies(имя мумии, место находки, описание)      # локальные атрибуты: name - имя мумии; location - место находки; descr - описание
pr = Papyri(название папируса, датировка, описание)  # локальные атрибуты: name - название папируса; date - датировка (строка); descr - описание
Метод get_info_exhibit() класса Museum должен возвращать значение атрибута descr указанного экспоната в формате:

"Описание экспоната {name}: {descr}"

Например:

"Описание экспоната Девятый вал: Айвазовский написал супер картину."

"""


class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []
    
    def add_exhibit(self, obj):
        """Добавление нового экспоната в музей (в конец списка exhibits)"""
        self.exhibits.append(obj)
    
    def remove_exhibit(self, obj):
        """Удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)"""
        self.exhibits.remove(obj)
    
    def get_info_exhibit(self, indx):
        """Получение информации об экспонате (строка) по индексу списка (нумерация с нуля)"""
        _i_link_to_object = self.exhibits[indx]
        return f"Описание экспоната {_i_link_to_object.name}: {_i_link_to_object.descr}"


class Picture:
    def __init__(self, name: str, author: str, descr: str):
        self.name = name  # название
        self.author = author  # художник
        self.descr = descr  # описание


class Mummies:
    def __init__(self, name: str, location: str, descr: str):
        self.name = name  # имя мумии
        self.location = location  # место находки
        self.descr = descr  # описание


class Papyri:
    def __init__(self, name: str, date: str, descr: str):
        self.name = name  # название папируса
        self.date = date  # датировка (строка)
        self.descr = descr  # описание


# TEST-TASK___________________________________
mus = Museum("Эрмитаж")
assert type(mus.name) is str, "название должно быть строкой"
assert mus.exhibits == [], "exhibits должен быть списком"
assert hasattr(mus, "add_exhibit"), "метод не объявлен"
assert hasattr(mus, "remove_exhibit"), "метод не объявлен"
assert hasattr(mus, "get_info_exhibit"), "метод не объявлен"

pic = Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор",
              "Вдохновляющая, устрашающая, волнующая картина")
assert 'name' in pic.__dict__.keys() and 'descr' in pic.__dict__.keys() and 'author' in pic.__dict__.keys(), "ошибка в локальных атрибутах"

mum = Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации")
assert 'name' in mum.__dict__.keys() and 'location' in mum.__dict__.keys() and 'descr' in mum.__dict__.keys(), "ошибка в локальных атрибутах"

p = Papyri("Ученья для, не злата ради",
           "Древняя Россия",
           "Самое древнее найденное рукописное свидетельство о языках программирования")
assert 'name' in p.__dict__.keys() and 'date' in p.__dict__.keys() and 'descr' in p.__dict__.keys(), "ошибка в локальных атрибутах"
assert type(p.date) is str, "название должно быть строкой"

mus.add_exhibit(pic)
assert mus.exhibits[0] == pic and len(mus.exhibits) == 1, "некорректно отработал метод add_exhibit"

mus.remove_exhibit(pic)
assert len(mus.exhibits) == 0 and pic not in mus.exhibits, "некорректно отработал метод remove_exhibit"

mus.add_exhibit(p)
mus.add_exhibit(pic)
answ = mus.get_info_exhibit(0)
print(answ)
assert answ == f"Описание экспоната {mus.exhibits[0].name}: {mus.exhibits[0].descr}", "некорректно отработал метод get_info_exhibit"
print("Правильный ответ.")
