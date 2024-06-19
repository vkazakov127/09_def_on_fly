# -*- coding: utf-8 -*-

print('-------- Задача 1. Фабрика функций --------')


def calculations(txt_operation):
    if txt_operation == 'add':
        def sum1(x, y):
            return x + y

        return sum1
    elif txt_operation == 'sub':
        def sub1(x, y):
            return x - y

        return sub1

    elif txt_operation == 'mul':
        def mul1(x, y):
            return x * y

        return mul1

    elif txt_operation == 'div':
        def div1(x, y):
            try:
                div = x / y
            except ZeroDivisionError:
                raise
            else:
                return div

        return div1


# Functions to be called
addition = calculations('add')
subtraction = calculations('sub')
multiplication = calculations('mul')
division = calculations('div')

# Calls
print(f'3 + 5 = {addition(3, 5)}')
print(f'3 - 5 = {subtraction(3, 5)}')
print(f'3 * 5 = {multiplication(3, 5)}')
print(f'3 / 5 = {division(3, 5)}')
try:
    print(f'3 / 0 = {division(3, 0)}')
except:
    print(f'3 / 0 : Error')

print('-------- Задача 2. Лямбда -----------------')
square1 = lambda x: x ** 2
print(f'4 ** 2 = {square1(4)} — by Lambda')


def square2(x):
    return x ** 2


print(f'4 ** 2 = {square2(4)} — by Def')

print('-------- Задача 3. Вызываемые объекты -----')


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


my_rect = Rectangle(6, 3)
print(f'area = {my_rect()}')
