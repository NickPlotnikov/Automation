# Банковское приложение
###
def bank (x,y):
    return x*((1.1)**y)
print(round(bank(x = int(input("Введите сумму вклада:")), y = int(input("Введите срок вклада (год):")))))
####
def bank(x,y):
    for i in range(1, y+1):
        count = x+(x/10)
        x = count
    print(round(count, 4))
bank(1000, 10)
