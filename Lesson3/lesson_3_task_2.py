# Список, экземпляров класса Smartphone

from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "iPhone 13", "+79123456789")
phone2 = Smartphone("Samsung", "Galaxy S21", "+79234567890")
phone3 = Smartphone("Xiaomi", "Redmi Note 11", "+79345678901")
phone4 = Smartphone("OnePlus", "9 Pro", "+79456789012")
phone5 = Smartphone("Google", "Pixel 6", "+79567890123")

# добавляем новый элемент в список

catalog.extend([phone1, phone2, phone3, phone4, phone5])

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")

