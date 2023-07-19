# -*- coding: cp1251 -*-

from string import ascii_uppercase, digits


class CardCheck:
    # � ��� � ����� ������ ������ ���� ������
    CHARS_FOR_NAME = ascii_uppercase + digits + ' '
    
    @staticmethod
    def check_card_number(number):
        i_list = number.split('-')
        if len(i_list) != 4:
            return False
        
        sets_digits = set(digits)
        for i in i_list:
            # ���� ����� ������� �� 4, ��� ������
            if len(i) != 4:
                return False
            # ������ ��������� ������ ��������� � ��������� digits
            if set(i) <= sets_digits:
                continue
            else:
                return False
        # ���� �� �������, ���������� True
        return True
    
    @classmethod
    def check_name(cls, name):
        if len(name.split(' ')) != 2:
            return False
        else:
            return set(name) <= set(cls.CHARS_FOR_NAME)


## ��������
is_name = CardCheck.check_name("SERGEI BALAKIREV")
is_number = CardCheck.check_card_number("1244-5678-9012-0000-5643")

print(is_name)
