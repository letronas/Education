t = {'�': 'yo', '�': 'a', '�': 'b', '�': 'v', '�': 'g', '�': 'd', '�': 'e', '�': 'zh',
     '�': 'z', '�': 'i', '�': 'y', '�': 'k', '�': 'l', '�': 'm', '�': 'n', '�': 'o', '�': 'p',
     '�': 'r', '�': 's', '�': 't', '�': 'u', '�': 'f', '�': 'h', '�': 'c', '�': 'ch', '�': 'sh',
     '�': 'shch', '�': '', '�': 'y', '�': '', '�': 'e', '�': 'yu', '�': 'ya',
     ' ': '-', '"': '-', ':': '-', ';': '-', '.': '-', ',': '-', '_': '-', '-': '-'}


def decorator_func(func):
    def wrapper(in_str: str):
        out_str: str = func(in_str)
        while out_str.find('--') != -1:
            out_str = out_str.replace('--', '-')
        
        return out_str
    
    return wrapper


@decorator_func
def func_replace(in_str: str):
    in_str = in_str.lower()
    new_str = ''
    for i in in_str:
        if i in t:
            new_str += t[i]
        else:
            new_str += i
    
    return new_str

s = input()

print(func_replace(s))
