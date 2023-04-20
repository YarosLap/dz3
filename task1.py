# Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.

n = int(input('Введите количество первых элементов последовательности Фибоначчи: '))

def fib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        lst = fib(n-1)
        lst.append(lst[-1] + lst[-2])
        return lst
    
print (fib(n))