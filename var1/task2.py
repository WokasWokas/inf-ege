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
#   X and (Y <= Z) and (-Y <= (-Z == W))   #
#                                          #
############################################
#                                          #
#            +   +   +   +   F             #
#            -   -   0   0   1             #
#            -   0   0   -   1             #
#            1   -   1   1   0             #
#                                          #
############################################
from itertools import product
from kernel.columner import Columner

columner = Columner()

result = []
for data in product(range(2), repeat=4):
    if not (data[0] and (data[1] <= data[2]) and ((not data[1]) <= ((not data[2]) == data[3]))):
        result.append(data)

print(columner(["x", "y", "z", "w"], result))