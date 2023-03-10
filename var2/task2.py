############################################
#                    #                     #
#     Вариант 2      #      Задание 2      #
#                    #                     #
############################################
#                                          #
#                 Условие:                 #
#                                          #
############################################
#                                          #
#   Y and (X -> W) and (-X -> (-W == Z))   #
#                                          #
############################################
#                                          #
#            +   +   +   +   F             #
#            0   0   -   -   1             #
#            0   -   -   0   1             #
#            1   1   1   -   1             #
#                                          #
############################################
from itertools import product
from kernel.columner import Columner

columner = Columner()

result = []
for data in product(range(2), repeat=4):
    if data[1] and (data[0] <= data[3]) and ((not data[0]) <= ((not data[3]) == data[2])):
        result.append(data)

print(columner(["x", "y", "z", "w"], result))