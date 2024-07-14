class StringUtils:

    # 01 Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст   
    def capitalize(self, string: str) -> str:
        return string.capitalize()      
    
    # 02 Принимает на вход текст и удаляет пробелы в начале, если они есть
    def trim(self, string: str) -> str: 
        whitespace = " "
        while (string.startswith(whitespace)):
            string = string.removeprefix(whitespace)
        return string

    # 03 Принимает на вход текст с разделителем и возвращает список строк. \n    
    def to_list(self, string: str, delimeter = ",") -> list[str]: 
        if(self.is_empty(string)):
            return []
        return string.split(delimeter)
    
    # 04 Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n
    def contains(self, string: str, symbol: str) -> bool:
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass
        return res
    
    # 05 Удаляет все подстроки из переданной строки \n
    def delete_symbol(self, string: str, symbol: str) -> str:
        if(self.contains(string, symbol)):
            string = string.replace(symbol, "")    
        return string

    # 06 Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n        
    def starts_with(self, string: str, symbol: str) -> bool:
        return string.startswith(symbol)

    # 07 Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n
    def end_with(self, string: str, symbol: str) -> bool:
        return string.endswith(symbol)
    
    # 08 Возвращает `True`, если строка пустая и `False` - если нет \n
    def is_empty(self, string: str) -> bool:
        string = self.trim(string)
        return string == ""
    
    # 09 Преобразует список элементов в строку с указанным разделителем \n
    def list_to_string(self, lst: list, joiner=", ") -> str:
        string = ""
        length = len(lst)        
        if length == 0: 
            return string         
        for i in range(0, length-1):
            string += str(lst[i]) + joiner        
        return string + str(lst[-1])