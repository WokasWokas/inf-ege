##################################
#               #                # 
#   Вариант 2   #   Задание 14   #
#               #                # 
##################################
from kernel.math import convert_to

integer = pow(4, 2022) - 6 * pow(4, 522) + 5 * pow(64, 510) - 3 * pow(2, 330) - 100

t = convert_to(integer, 8)

print(t.count('7'))