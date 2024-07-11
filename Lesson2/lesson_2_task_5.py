# Месяц — сезон

# весна начинается 1 марта, лето — 1 июня, осень — 1 сентября, а зима — 1 декабря.

def month_to_season(month):
        if month in [1,2,12]:
            return "Зима"
        elif month in [6,7,8]:
            return "Лето"
        elif month in [9,10,11]:
            return "Осень"
        elif month in [3,4,5]:
            return "Весна"
        else:
            return "Неверный номер"
print(month_to_season(11))
print(month_to_season(7))
print(month_to_season(3))