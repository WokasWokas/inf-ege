##################################
#               #                # 
#   Вариант 2   #   Задание 17   #
#               #                # 
##################################
import os

file = f"{os.path.dirname(__file__)}\\files\\task17.txt"
data = []

with open(file, "r") as file:
    for line in file.readlines():
        data.append(int(line))

maximum = max(data) 

count, msum = 0, 0
for i in range(data.__len__() - 1):
    if (data[i] + data[i + 1]) == maximum:
        count += 1
        msum = max(msum, (data[i]**2 + data[i+1]**2))

print(count, msum)