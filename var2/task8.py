##################################
#               #                # 
#   Вариант 2   #    Задание 8   #
#               #                # 
##################################
from kernel.math import convert_to

count = 0
for i in range(10000, 100000):
    fourInteger = convert_to(i, 4)
    
    if fourInteger.count('3') != 1: continue
    
    index = fourInteger.index('3')
    
    if (index + 1) == fourInteger.__len__():
        if fourInteger[index - 1] == "0":
            continue
        count += 1
    elif index == 0:
        if fourInteger[index + 1] == "0":
            continue
        count += 1
    else:
        if fourInteger[index - 1] == "0":
            continue
        if fourInteger[index + 1] == "0":
            continue
        count += 1

print(count)