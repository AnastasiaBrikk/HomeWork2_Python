# 4)Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

number = int(input('Input an integer number: '))

sum = 0

for i in range(number+1):
    if i%2 == 0:
        sum += i
print(sum)