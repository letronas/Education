i_start = 0  # ������
i_stop = 0  # ����� ������
i = 0  # ������� ��� ��������
# '---some--words---that--i should repalce ------ to normal view --------'
some_string = input()
new_string = ''  # ������ ����� ������
len_our_string = len(some_string)-1
while i <= len_our_string:
    if some_string[i] == '-' and (i != 0 and some_string[i - 1] != '-'):
        i_start = i
        i_stop = i
        if i == len_our_string and some_string[i-1] != '-': # ����� ������ ������������, � �� ����� �� ���� -
            i += 1  # ����� �� ���� � ��������� �������� � ������� ����
            new_string += '-'
            
    elif some_string[i] == '-' and some_string[i-1] == '-':
        i_stop = i
        if i == len_our_string and some_string[i-1] == '-': # ����� ������ ������������ --
            i += 1  # ����� �� ���� � ��������� �������� � ������� ����
            new_string += '-'

    elif i_stop != 0 and i_stop-i_start >= 1:
        new_string += '-' + some_string[i]
        i_start = 0
        i_stop = 0
    elif i_start == i_stop and i_stop != 0:  # ����������� ���� �� ������, ���� ������ ����� ����
        new_string += some_string[i-1] + some_string[i]
        i_start = 0
        i_stop = 0
    else:
        new_string += some_string[i]
        
        
    i += 1
    
print(new_string)