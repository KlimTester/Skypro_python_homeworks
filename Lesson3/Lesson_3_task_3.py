from address import Address
from mailing import Mailing

to_address = Address("660077", "Красноярск", "Весны", "1", "2")
from_address = Address("654321", "Москва", "Урванцева", "3", "4")
mailing_instance = Mailing(to_address, from_address, 100, "ПочтаРоссии")

print(f"Отправление {mailing_instance.track} из {mailing_instance.from_address.index}, "
      f"{mailing_instance.from_address.city}, {mailing_instance.from_address.street}, "
      f"{mailing_instance.from_address.house} - {mailing_instance.from_address.apartment} "
      f"в {mailing_instance.to_address.index}, {mailing_instance.to_address.city}, "
      f"{mailing_instance.to_address.street}, {mailing_instance.to_address.house} - "
      f"{mailing_instance.to_address.apartment}. "
      f"Стоимость {mailing_instance.cost} рублей.")

