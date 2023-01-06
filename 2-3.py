# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]

# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

num = int(input('Input an integer number: '))
len = 2*num+1
list = [-num]
for i in list:
    if i < num:
        list.append(i+1)
print(list)

indexes = [2, 3, 1, 0, 6]


print(f'Indexes {indexes}')

result = list[indexes[0]] * list[indexes[1]] * list[indexes[2]] * list[indexes[3]] * list[indexes[4]]
print(result)
