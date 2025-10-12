from smartphone import Smartphone

catalog = [
    Smartphone("Sony", "A11", "+7911 111 11 11"),
    Smartphone("Samsung", "B12", "+7922 222 22 22"),
    Smartphone("Apple", "C13", "+7933 333 33 33"),
    Smartphone("Xiaomi", "D14", "+7944 444 44 44"),
    Smartphone("Vivo", "E15", "+7955 555 55 55")
]

for x in catalog:
    print(f"{x.marka} {x.model} {x.num}")
