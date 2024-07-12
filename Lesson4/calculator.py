# Создание класса Calculator


class Calculator:


    def sum(self, a, b): # Метод для сложения
        result = a+b 
        return result
    
    def sub(self, a, b): # Метод для вычитания
       result = a-b
       return result
    
    def mul(self, a, b): # Метод для умножения
        return a*b
    
    def div(self, a, b): # Метод для деления
        if (b == 0): 
            raise ArithmeticError("На ноль делить нельзя")
        return a/b 

    def pow(self, a, b=2): # Метод для степени
        return a**b
    
    def avg(self, nums): # Метод для среднего арифметического
        if (len(nums) == 0):
            return 0

        s = 0
        for num in nums:
             s = s + num

        l = len(nums)
        return self.div(s, l)