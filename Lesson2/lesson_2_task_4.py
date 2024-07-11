#FizzBuzz. Задачка с собеседования
n = int(input())
def fizz_buzz(n):
    for n in range(1, n+1): # Функция должна печатать числа от 1 до n
        if (n % 3 == 0) and (n % 5 == 0): # если число делится на 3 и на 5, печатать FizzBuzz
            print("FizzBuzz")
        elif n % 3 == 0: # если число делится на 3, печатать Fizz
            print("Fizz")
        elif n % 5 == 0: # если число делится на 5, печатать Buzz
            print("Buzz")
        else:
            print(n)
fizz_buzz(n)