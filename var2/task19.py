##################################
#               #                # 
#   Вариант 2   #   Задание 19   #
#               #                # 
##################################
def check(s: int) -> bool:
    fa, sa = s+1, s*2
    
    if fa > 300 or sa > 300:
        return False
    
    if (fa + 1) > 300 and (fa * 2) > 300:
        return True
    elif (sa + 1) > 300 and (sa * 2) > 300:
        return True
    return False

for i in range(1, 301):
    if check(i):
        print(i)