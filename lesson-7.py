# FIRST
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end='   ')
            print()
        return '\n'

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j] + other.matrix[i][j], end='   ')
            print()


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 13]])
print(matrix_1)
summ = matrix_1 + matrix_2
print()

# SECOND
from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def formula(self):
        print('You need ', end='')


class Coat(Clothes):
    def __init__(self, v):
        super().__init__(self)
        self.v = v

    def formula(self):
        super(Coat, self).formula()
        coat = round(self.v / 6.5 + 0.5)
        return coat


class Costume(Clothes):
    def __init__(self, h):
        super().__init__(self)
        self.h = h

    def formula(self):
        super(Costume, self).formula()
        costume = round(2 * self.h + 0.3)
        return costume


a = input('coat or costume? ').lower()
b = Clothes(a)
if a == 'coat':
    d = int(input('V = '))
    c = Coat(d)
    print(c.formula(), 'cloths')
elif a == 'costume':
    d = int(input('H = '))
    c = Costume(d)
    print(c.formula(), 'cloths')

# THIRD


class Ceil:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        if self.number < other.number:
            pass
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        if self.number < other.number:
            pass
        return self.number / other.number

    def make_order(self, rows):
        a = self.number // rows
        for i in range(a):
            for j in range(int(rows)):
                print('*', end='')
                self.number -= j
            print()
        print('*' * (self.number % rows))


ceil_1 = Ceil(16)
ceil_2 = Ceil(5)
print()
print(f'сумма = {ceil_1 + ceil_2}')
print()
print(f'вычитание = {ceil_1 - ceil_2}')
print()
print(f'умножение = {ceil_1 * ceil_2}')
print()
print(f'деление = {ceil_1 / ceil_2}')
print()
print(ceil_1.make_order(3))
print()
print(ceil_2.make_order(1))
