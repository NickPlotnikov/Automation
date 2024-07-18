# Automation
Курс по Python
Less.1

--1
my_name = "Nikolay"
print(my_name)

--2
my_age = 33
my_age = 33 + 3
print(my_age)

--3
user_name = input("Как вас зовут? ")
print("Привет! " + user_name)

--4
First_name = input("Введите ваше имя ")
Last_name = input("Введите вашу фамилию ")
print("Hello! " + First_name + Last_name)

--5
def print_greeting (a, b):
    print (a + b)
print_greeting ("<Привет, ", "мир!>")

--6
def print_a ():
    print("1", end="")

def print_b ():
    print("2", end="")

def print_c ():
    print("3", end="")

def print_d ():
    print("4", end="")

def print_e ():
    print("5", end="")

def print_f ():
    print("6", end="")

def print_g ():
    print("7", end="")

def print_l ():
    print("8", end="")

def print_m ():
    print("9", end="")

def print_n ():
    print("0", end="")

print_l(),
print_l(), 
print_n(), 
print_n(), 
print_e(), 
print_e(), 
print_e(), 
print_c(), 
print_e(), 
print_c(), 
print_e(),

--7
def print_letter(num):
    print(num, end = '')
print_letter(8)
print_letter(8)
print_letter(0)
print_letter(0)
print_letter(5)
print_letter(5)
print_letter(5)
print_letter(3)
print_letter(5)
print_letter(3)
print_letter(5)

--3 HW
# #Типы данных
# from user import User
# from card import Card

# Alex = User("Alex")

# Alex.sayName()
# Alex.setAge(33)
# Alex.sayAge()

# card = Card("3435 3434 3224 4534", "11/28", "Alex F")

# Alex.addCard(card)
# Alex.getCard().pay(1000)


# _____________________


# class Card:
#     number = '0000 0000 0000 0000'
#     validDate = '01/99'
#     holder = 'unknown'

#     def __init__(self, number, date, holder):
#         self.holder = holder
#         self.number = number
#         self.validate = date

#     def pay(self, amount):
#         print("с карты", self.number, "списали", amount)


#_________________________________

# #Пользователь
# class User:
#     age = 0
    
#     def __init__(self, name):
#         print("я создался")
#         self.username = name
        
#     def sayName(self):
#         print("Меня зовут", self.username)

#     def sayAge(self):
#         print(self.age)

#     def setAge(self, newAge):
#         self.age = newAge
    
#     def addCard(self, card):
#         self.card = card

#     def getCard(self):
#         return self.card

##############################################################################

# import pytest
# from calculator import Calculator 

# calculator = Calculator()

# @pytest.mark.parametrize( 'num1, num2, result', [
#     (4, 5, 9), 
#     (-6, -10, -16), 
#     (-6, 6, 0), 
#     (5.61, 4.29, 9.9),
#     (10, 0, 10),
#     (-10.5, 1234, 1223.5)    
#     ] )
# def test_sum_nums(num1, num2, result):
#     calculator = Calculator()
#     res = calculator.sum(num1, num2)
#     assert res == result
    
# @pytest.mark.parametrize( 'nums, result', [ 
#     ([], 0), 
#     ([1, 2, 3, 4, 5, 6, 7, 8, 9, 5], 5)     
#     ] )
# def test_avg_list(nums, result):
#     calculator = Calculator()
#     res = calculator.avg(nums)
#     assert res == result

# def test_div_positive(): #проверка деления чисел
#     calculator = Calculator()
#     res = calculator.div(10, 2)
#     assert res == 5

# def test_div_by_zero(): #проверка деления на ноль
#     calculator = Calculator()
#     with pytest.raises(ArithmeticError):
#         calculator.div(10, 0)

#############################################################################

# # Создание класса Calculator


# class Calculator:


#     def sum(self, a, b): # Метод для сложения
#         result = a+b 
#         return result
    
#     def sub(self, a, b): # Метод для вычитания
#        result = a-b
#        return result
    
#     def mul(self, a, b): # Метод для умножения
#         return a*b
    
#     def div(self, a, b): # Метод для деления
#         if (b == 0): 
#             raise ArithmeticError("На ноль делить нельзя")
#         return a/b 

#     def pow(self, a, b=2): # Метод для степени
#         return a**b
    
#     def avg(self, nums): # Метод для среднего арифметического
#         if (len(nums) == 0):
#             return 0

#         s = 0
#         for num in nums:
#              s = s + num

#         l = len(nums)
#         return self.div(s, l)