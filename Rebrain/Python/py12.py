from os import getlogin as get_pc_logic
from psutil import virtual_memory as get_pc_memory
from psutil import getloadavg as get_ld_avg


class PCMemory:
    # 1.1.
    def __init__(self, pc_id, user_name, memory_total, memory_used, memory_percent=None):
        self.pc_id = pc_id
        self.user_name = user_name
        self.memory_total = memory_total
        self.memory_used = memory_used
        if memory_percent:
            self.memory_percent = memory_percent
        else:
            self.memory_percent = round((memory_used / memory_total) * 100, 1)
    
    # 1.2
    def show_used_percent(self):
        print(f'PC with id {self.pc_id} used {self.memory_percent} percent of memory')
    
    # 1.3
    def is_enough_memory(self):
        if self.memory_percent < 10:
            return False
        else:
            return True


class PCAdvanced(PCMemory):
    def __init__(self, pc_id, user_name, memory_total, memory_used, ld_avg_1m, ld_avg_15m, memory_percent=None):
        super().__init__(pc_id, user_name, memory_total, memory_used, memory_percent)
        # 2
        self.ld_avg_1m = ld_avg_1m
        self.ld_avg_15m = ld_avg_15m
    
    def is_overloaded(self):
        if self.ld_avg_15m == 0:  # из-за этого пришлось переписать тернарник
            return False
        elif self.ld_avg_1m / self.ld_avg_15m < 3:
            return False
        else:
            return True
    
    def __call__(self, p_str='memory', *args, **kwargs):
        if p_str == 'memory':
            return self.is_enough_memory()
        elif p_str == 'load':
            return self.is_overloaded()
        else:
            return None


pc_mem = get_pc_memory()
ld_avg = get_ld_avg()
# Параметры указал для себя явно, просто так. Привычки из PL/SQL, кажется это правильным
new_pc = PCAdvanced(pc_id=1, user_name=get_pc_logic(), memory_total=pc_mem[0], memory_used=pc_mem[0] - pc_mem[1],
                    ld_avg_1m=ld_avg[0], ld_avg_15m=ld_avg[2])

new_pc.show_used_percent()
print(new_pc.is_enough_memory())

# 5
print(new_pc('load'))
print(new_pc('Test'))
# 6
print(new_pc())
