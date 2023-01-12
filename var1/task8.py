##################################
#               #                # 
#   Вариант 2   #    Задание 8   #
#               #                # 
##################################
from kernel.math import convert_to

count = 0
for i in range(10000, 100000):
    fourInteger = convert_to(i, 8)
    
    if fourInteger.count('4') != 2: continue
    
    for i in range(1, fourInteger.__len__() - 1):
        if fourInteger[i] == '4' and ((int(fourInteger[i - 1]) % 2 == 0) or (int(fourInteger[i + 1]) % 2 == 0)):
            continue
        count += 1
print(count)