# 1) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) Факториалы числел от 1 до Н

number = int(input("Input an integer number:  "))

def Factorial (number):
    if number < 0: number = -number
    if number != 0:
        lastValue = 1
        list = []

        for i in range(number):
            list.append(i + 1)

        for k in range(number): 
            list[k] = lastValue * list[k]
            lastValue = list[k]

        print(f"Произведение цифр числа от 1 до {number} =  {list}")
        return list
    else:
        print("Error")

Factorial(number)
        