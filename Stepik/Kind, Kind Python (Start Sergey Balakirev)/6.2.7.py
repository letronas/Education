from operator import itemgetter, attrgetter

things = {'��������': 20, '���������': 100, '����': 500, '�������': 300,
          '�����': 1000, '������': 200, '�������': 600, '����': 400, '������': 1200,
          '��������': 40, '�������': 820, '�������': 5240, '�������': 2130, '������': 10}

new = [(thing, weight) for thing, weight in things.items()]

# https://docs.python.org/3/howto/sorting.html
new = sorted(new, key=itemgetter(1), reverse=True)


some_weigth = int(input()) * 1000
new_str = ''
for i in new:
    if some_weigth - i[1] >= 0:
        new_str += i[0] + ' '
        some_weigth -= i[1]

print(new_str.strip())
