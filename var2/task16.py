##################################
#               #                # 
#   Вариант 2   #   Задание 16   #
#               #                # 
##################################
def foo(n):
    if n < 3:
        return n
    
    if n > 2 and n % 2 == 0:
        return 3 * (n - 1) + foo(n - 1) + 5
    else:
        return 3 * (n + 1) + foo(n - 2) - 2

print(foo(35))