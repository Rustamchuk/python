#FIRST
a = 'hello'
print(a, 'World', sep = ', ', end='!')
b = input()
c = int(input())
print('\n', b, c)
#SECOND
a = int(input())
b = a // 360
c = (a - b * 360) // 60
a -= b * 360 - c * 60
print(b, c, a, sep=':')
#THIRD
a = input()
b = int(a + a)
c = int(a * 3)
print(int(a) + b + c)
#FOURTH
a = int(input())
max = 0
while a != 0:
    b = a % 10
    if max < b:
        max = b
    a //= 10
print(max)