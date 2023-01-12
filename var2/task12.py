##################################
#               #                # 
#   Вариант 2   #   Задание 12   #
#               #                # 
##################################
string = f"22{'1' * 2050}22"

while "211" in string or "112" in string:
    string = string.replace("11", "1")
    if "21" in string:
        string = string.replace("21", "12")
    else:
        string = string.replace("12", "1")

print(string)