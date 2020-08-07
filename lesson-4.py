#FIRST
from sys import argv

a, t, v = argv

def money():
    s = int(t) * int(v)
    return s
print(f'Р’Р°С€ Р·Р°СЂРѕР±РѕС‚РѕРє - {money()}')

#SECOND
a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
b = [i for i in a[1:] if i > a[a.index(i) - 1]]
print(b)

#THIRD
c = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(c)

#FOURTH
a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
b = []
for i in a:
    if a.count(i) == 1:
        b.append(i)
print(b)

#FIVTH
from functools import reduce
def total(c, b):
    return c * b
print(reduce(total, [i for i in range(100, 1001, 2)]))

#SIXTH
#A
from sys import argv
s, a, b = argv
c = [i for i in range(int(a), int(b)+1)]
print(f'Число от {a} до {b}: {c}')
#B
from itertools import cycle, count
d = cycle(c)
k = []
for i in range(100):
    k.append(next(d))
print(k)
print(f'Получилось {k.count(20)} цифры 20')

#SEVENTH
def fact(a):
    total = 1
    for i in range(1, a+1):
        total *= i
    yield total
n = int(input('Введите число - '))
for el in fact(n):
     print(el)