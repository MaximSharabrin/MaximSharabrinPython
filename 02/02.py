
# employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]
# print(employee_list[1] + ", " + employee_list[-2])

# =============================================

# num = int(input("Введите число: "))
# def dev_by_three(number):
#    print("Да")
#    return "Да" if number % 3 == 0 else "Нет"

# rezult = dev_by_three(num)
# print (f"Делится ли на три {num} ? - {rezult}")

# =============================================
"""import math

num_items = input("Введите количество коробок: ")
x = 21
x = int(num_items)
print(x)

def min_boxes(items):
    y = math.ceil( items / 5 )
    print(items)
    print(y)
    return y

# min_boxes(x)
print(f"Минимальное количество коробок {min_boxes(x)}")"""
# =============================================
"""
x = int(input("Введите число: "))
print(x)

def check_divisibility(n):
    print(n)
    for i in range(1, n + 1):
        if i % 4 == 0:
            print(f"{i} Делится и на 2, и на 4")
        elif i % 2 == 0:
            print(f"{i} Делится и на 2, но не на 4")
        else:
            print(i)

check_divisibility(x)
"""
# =============================================
"""
def quarter_of_year(month):
    if 1 <= month <= 3:
        return "Первый квартал"
    elif 4 <= month <= 6:
        return  "Второй квартал"
    elif 7 <= month <= 9:
        return "Третий квартал"
    elif 10 <= month <= 12:
        return "Четвертый квартал"
    else:
        return "Неправильный номер месяца"

try:
    month = int(input("Введите номер месяца (1-12): "))
    print(quarter_of_year(month))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")
"""
# =============================================
"""
lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]

for i in range( 0, len(lst) ):
    if lst[i] > 15 and lst[i] % 3 == 0:
        print(lst[i])
"""
# =============================================














