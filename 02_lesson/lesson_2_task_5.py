
n = int(input("Введите номер месяца: "))


def month_to_season(n):
    if n == 12 or 1 <= n <= 2:
        return "Зима"
    elif 3 <= n <= 5:
        return "Весна"
    elif 6 <= n <= 8:
        return "Лето"
    elif 9 <= n <= 11:
        return "Осень"
    else:
        return "Номер месяца может быть только от 1 до 12"


print(month_to_season(n))
