# Високосный год
#year = int(2023)
year = int(input("Введите год: "))
def is_year_leap(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):        
        return True
    else:        
        return False
year_res = is_year_leap(year)
print (f"год {year}: {year_res}")