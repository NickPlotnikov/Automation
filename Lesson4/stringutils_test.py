from stringutils import StringUtils

stringutils = StringUtils()
  
# 01 Тестирование метода capitalize Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
#print(stringutils.capitalize("skypro"))  # "Skypro"
capitalize_text = stringutils.capitalize("skypro")
print(capitalize_text)
assert capitalize_text == ("Skypro")
    
# 02 Тестирование метода trim Принимает на вход текст и удаляет пробелы в начале, если они есть
#print(stringutils.trim("  skypro"))  # "skypro"
trimmed_text = stringutils.trim("   skypro")
print(trimmed_text)
assert trimmed_text == ("skypro")
    
# 03 Тестирование метода to_list Принимает на вход текст с разделителем и возвращает список строк. \n 
# print(stringutils.to_list("a,b,c,d"))  # ["a", "b", "c", "d"]
# print(stringutils.to_list("1:2:3", ":"))  # ["1", "2", "3"]
list_from_string = stringutils.to_list("a,b,c,d")
print(list_from_string)
assert list_from_string == (["a", "b", "c", "d"])
    
# 04 Тестирование метода contains Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n
# print(stringutils.contains("SkyPro", "S"))  # True
# print(stringutils.contains("SkyPro", "U"))  # False
contains_symbol = stringutils.contains("skypro", "s")
print(contains_symbol)
assert contains_symbol == True
    
# 05 Тестирование метода delete_symbol Удаляет все подстроки из переданной строки \n
# print(stringutils.delete_symbol("SkyPro", "k"))  # "SyPro"
# print(stringutils.delete_symbol("SkyPro", "Pro"))  # "Sky"
deleted_symbol_text = stringutils.delete_symbol("skypro", "k")
print(deleted_symbol_text)
assert deleted_symbol_text == ("sypro")
    
# 06Тестирование метода starts_with Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n
# print(stringutils.starts_with("SkyPro", "S"))  # True
# print(stringutils.starts_with("SkyPro", "P"))  # False
starts_with_symbol = stringutils.starts_with("skypro", "s")
print(starts_with_symbol)
assert starts_with_symbol == True
    
# 07 Тестирование метода end_with Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n
# print(stringutils.end_with("SkyPro", "o"))  # True
# print(stringutils.end_with("SkyPro", "y"))  # False
ends_with_symbol = stringutils.end_with("skypro", "o")
print(ends_with_symbol)
assert ends_with_symbol == True
    
# 08 Тестирование метода is_empty Возвращает `True`, если строка пустая и `False` - если нет \n
# print(stringutils.is_empty(""))  # True
# print(stringutils.is_empty(" "))  # True
# print(stringutils.is_empty("SkyPro"))  # False
is_text_empty = stringutils.is_empty("   ")
print(is_text_empty)
assert is_text_empty == True
    
# 09 Тестирование метода list_to_string Преобразует список элементов в строку с указанным разделителем \n
# print(stringutils.list_to_string([1, 2, 3, 4]))  # "1, 2, 3, 4"
# print(stringutils.list_to_string(["Sky", "Pro"]))  # "Sky, Pro"
# print(stringutils.list_to_string(["Sky", "Pro"], "-"))  # "Sky-Pro"
string_from_list = stringutils.list_to_string([1, 2, 3, 4])
print(string_from_list)
assert string_from_list == ("1, 2, 3, 4")

    
    
   