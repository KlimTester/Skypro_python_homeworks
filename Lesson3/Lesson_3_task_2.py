from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy S20", "+79123456789"))
catalog.append(Smartphone("Apple", "iPhone 12", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 10", "+79345678901"))
catalog.append(Smartphone("OnePlus", "8T", "+79456789012"))
catalog.append(Smartphone("Google", "Pixel 5", "+79567890123"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
