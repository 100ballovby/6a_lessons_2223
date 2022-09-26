num = int(input('Введи число: '))
summa = 0
summa = summa + num % 10
num = num // 10
summa = summa + num % 10
num = num // 10
summa = summa + num % 10
num = num // 10
summa = summa + num % 10
num = num // 10
print(summa)
