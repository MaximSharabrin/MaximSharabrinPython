
x = int(input("Введите год: "))


def is_year_leap(y):
    if y % 4 == 0:
        return True
    else:
        return False


fin = is_year_leap(x)

print(f"Год {x}: {fin}")
