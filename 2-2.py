# 2) Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# Пример:

# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

number = int(input('Input an integer number: '))

i = 2

while number% i != 0:
    i += 1
print(i)