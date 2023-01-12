##################################
#               #                # 
#   Вариант 2   #    Задание 5   #
#               #                # 
##################################
def foo(integer: int) -> int:
    binInteger = bin(integer)[2:]
    
    if integer % 2 == 0:
        binInteger += "0"
    else:
        binInteger += "1"
        
    if binInteger.count("1") % 3 == 0:
        binInteger = "11" + binInteger[2:]
    else:
        binInteger = "10" + binInteger[2:]
        
    return int(binInteger, 2)

for i in range(100, 0, -1):
    if foo(i) >= 26:
        print(i, " = ", foo(i))