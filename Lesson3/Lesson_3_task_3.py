from address import Address
from mailing import Mailing

# Создаем экземпляр класса Address для адреса назначения
to_address = Address("660077", "Красноярск", "Весны", "1", "2")

# Создаем экземпляр класса Address для адреса отправителя
from_address = Address("654321", "Москва", "Урванцева", "3", "4")

# Создаем экземпляр класса Mailing
mailing_instance = Mailing(to_address, from_address, 100, "ПочтаРоссии")

# Выводим информацию о почтовом отправлении
print(f"Отправление {mailing_instance.track} из {mailing_instance.from_address.index}, {mailing_instance.from_address.city}, {mailing_instance.from_address.street}, {mailing_instance.from_address.house} - {mailing_instance.from_address.apartment} "
      f"в {mailing_instance.to_address.index}, {mailing_instance.to_address.city}, {mailing_instance.to_address.street}, {mailing_instance.to_address.house} - {mailing_instance.to_address.apartment}. "
      f"Стоимость {mailing_instance.cost} рублей.")
