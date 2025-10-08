import math


x = float(input("Введите длину стороны квадрата: "))

print(x)


def square(y):
    y = y * 2
    return y


fin = square(x)
print(math.ceil(fin))
