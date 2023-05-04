t = {'�': 'yo', '�': 'a', '�': 'b', '�': 'v', '�': 'g', '�': 'd', '�': 'e', '�': 'zh',
     '�': 'z', '�': 'i', '�': 'y', '�': 'k', '�': 'l', '�': 'm', '�': 'n', '�': 'o', '�': 'p',
     '�': 'r', '�': 's', '�': 't', '�': 'u', '�': 'f', '�': 'h', '�': 'c', '�': 'ch', '�': 'sh',
     '�': 'shch', '�': '', '�': 'y', '�': '', '�': 'e', '�': 'yu', '�': 'ya',
     ' ': '-'}


def decor_param_func(chars='!?'):
    def decorator_func(func):
        def wrapper(in_str: str):
            new_str_in: str = func(in_str, dict(zip(list(chars), '-' * len(chars))))
            final_str: str = func(new_str_in)
            while '--' in final_str:
                final_str = final_str.replace('--', '-')
            return final_str
        
        return wrapper
    
    return decorator_func


@decor_param_func(chars="?!:;,. ")
def replace_lat_str(in_str: str, char_dict_or_list=t):
    new_str = ''
    for i in in_str:
        if i in char_dict_or_list:
            new_str += char_dict_or_list[i]
        else:
            new_str += i
    return new_str


s = input().lower()
print(replace_lat_str(s))
