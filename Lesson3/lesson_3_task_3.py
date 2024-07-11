from address import Address
from mailing import Mailing

# Создание адресов
to_address = Address("123456", "Москва", "Тверская", "1", "101")
from_address = Address("654321", "Санкт-Петербург", "Невский проспект", "10", "15")

# Создание почтового отправления
mailing = Mailing(to_address, from_address, 150.0, "ABC123456")

# Печать информации об отправлении
print(mailing)