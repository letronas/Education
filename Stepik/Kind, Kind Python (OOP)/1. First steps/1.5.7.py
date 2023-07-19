"""
Lesson 1.5
Task 7
    
CPU - ����� ��� �������� �����������;
Memory - ����� ��� �������� ������;
MotherBoard - ����� ��� �������� ����������� ����.

���������� ����������� �������� �������� ������� ������ ���������:

cpu = CPU(������������, �������� �������)
mem = Memory(������������, ������ ������)
mb = MotherBoard(������������, ���������, ������1, ������2, ..., ������N)
�������� �������� ��� �������� ������� ������ MotherBoard ����� ���������� ��������� �������� ������ Memory, �������� N - �� ����� ������ ������ �� ����������� ����� (N = 4).

������� ������� ������ ����� ��������� ��������� ��������: 

��� ������ CPU: name - ������������; fr - �������� �������;
��� ������ Memory: name - ������������; volume - ����� ������;
��� ������ MotherBoard: name - ������������; cpu - ������ �� ������ ������ CPU; total_mem_slots = 4 - ����� ����� ������ ������ (������� ������������� � ���� ��������� � �� ��������); mem_slots - ������ �� �������� ������ Memory (�������� total_mem_slots = 4 ���� �� ������������� ����� ������ ������).

����� MotherBoard ������ ����� ����� get_config(self) ��� ����������� ������� ������������ ����������� �� ����������� ����� � ���� ���������� ������ �� ������� �����:

['����������� �����: <������������>',
'����������� ���������: <������������>, <�������� �������>',
'������ ������: <����� ����� ������ ������>',
'������: <������������_1> - <�����_1>; <������������_2> - <�����_2>; ...; <������������_N> - <�����_N>']

�������� ������ mb ������ MotherBoard � ����� CPU (������ ������ CPU) � ����� ������� ������ (������� ������ Memory).

P.S. ���������� �� ������ ������ �� �����, ������ ������� ������ �� ��������� �����������.
"""

class CPU:
    def __init__(self, name: str, fr: int):
        # ������������
        self.name = name
        # �������� �������
        self.fr = fr


class Memory:
    def __init__(self, name: str, volume: int):
        # ������������
        self.name = name
        # ����� ������
        self.volume = volume


class MotherBoard:
    def __init__(self, name: str, cpu: CPU, *mem_slots: Memory):
        # ������������
        self.name = name
        # ������ �� ������ ������ CPU
        self.cpu = cpu
        # ����� ����� ������ ������ (������� ������������� � ���� ��������� � �� ��������)
        self.total_mem_slots = 4
        # ������ �� �������� ������ Memory (�������� total_mem_slots = 4 ���� �� ������������� ����� ������ ������).
        self.mem_slots = [*mem_slots][:self.total_mem_slots]
    
    def get_config(self):
        mem = '������: '
        for i in self.mem_slots:
            mem += f'{i.name} - {i.volume}; '
        
        mem = mem.rstrip('; ')
        ret_lst = [f'����������� �����: {self.name}', f'����������� ���������: {self.cpu.name}, {self.cpu.fr}',
                   f'������ ������: {self.total_mem_slots}', mem]
        return ret_lst


cpu = CPU('asus', 1333)
mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 4000)
mb = MotherBoard('Asus', cpu, mem1, mem2)
print(mb.get_config())

'''
assert isinstance(mb, MotherBoard) and hasattr(MotherBoard, 'get_config')


def get_config():
    mem_str = "; ".join([f"{x.name} - {x.volume}" for x in mb.mem_slots])
    
    return [f"����������� �����: {mb.name}",
            f"����������� ���������: {mb.cpu.name}, {mb.cpu.fr}",
            f"������ ������: {mb.total_mem_slots}",
            f"������: {mem_str}"]


res1 = ("".join(mb.get_config())).replace(" ", "")
res2 = ("".join(get_config())).replace(" ", "")
print(res1, res2, sep='\n')
assert res1 == res2, "����� get_config ��������� �������� ������"
'''