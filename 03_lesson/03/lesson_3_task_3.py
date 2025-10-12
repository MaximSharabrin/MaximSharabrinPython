from address01 import Address
from mailing02 import Mailing

to_address = Address("614568", "Самара", "Кутякова", "54", "87")
from_address = Address("468297", "Волгоград", "Тельмана", "37", "12")

mailing = Mailing(to_address="Московская",
                  from_address="Кирова",
                  cost=539,
                  track="Treck861")

print(f"Отправление {mailing.track} из {from_address.index}, {from_address.city}, "
      f"{from_address.street}, {from_address.house} - {from_address.apartment}"
      f" в {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment}."
      f" Стоимость {mailing.cost} рублей.")
