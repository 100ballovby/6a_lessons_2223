num = int(input('Введи число: '))

units = num % 10  # найти последнюю цифру числа
tens = num % 100 // 10  # десятки (вторая с конца цифра)
hundreds = num // 100 % 10  # сотни
thousands = num // 1000  # разряд тысяч

print(num, '=', units + tens + hundreds + thousands)


