#FIRST
def division(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        return '[������!]\n���... �� ���� ������ ������...'
    return c

k = int(input('����� ����� ������ �����?\n'))
z = int(input('� ������?\n'))
print(f'�� ������� = {division(k, z)}')
#SECOND
def information():
    try:
        name = input('��� - ')
        surname = input('������� - ')
        birth = input('���� �������� - ')
        city = input('����� ���������� - ')
        email = input('����� - ')
        number = input('����� �������� - ')
    except: 
        print('������� ���-�� ���-�� �� ���...')
    return f'���� �� {name} {surname}, �������� {birth}, ������ � ������ {city}, ���� ����� {email} � ����� �������� {number}\n ���� ��� ��������� ������� Enter'

print(information())
#THIRD
def my_func(a, b, c):
    maxx_1 = max(a, b, c)
    maxx_2 = [a, b, c]
    maxx_2.remove(maxx_1)
    maxx_2 = max(maxx_2)
    sum = ord(maxx_1) + ord(maxx_2)
    return sum

a1 = input('������� ������ - ')
b1 = input('������� ������ - ')
c1 = input('������� ������ - ')
print(f'����� ������������ ������ ����� {my_func(a1, b1, c1)}' )
#FOURTH
def my_func(x, y):
    x **= y
    return x
def my_func2(x, y):
    z = 1
    for i in range(y):
        z *= x
    return z

x1 = int(input('����� ����� �������� � �������? '))
y1 = int(input('� ����� �������? '))
print(f'�����: {my_func(x1, y1)}')
print(f'�����: {my_func2(x1, y1)}')
#FIFTH
#print('������� ����� ����� ������ ��� �������� �����. ���� ����� - STOP')
#summ = 0
#c = ''
#while c != 'STOP':
#    b = list(input())
#    for i in range(len(b)):
#        if b[i] != ' ' and b[i] != 'STOP':
 #           a = int(b[i])
#            summ += a
 #       elif b[i] == 'STOP':
#            c = 'STOP'
 #   print(summ)
#SIXTH
def int_func(a):
    return a.title()
b = input('�������� ����� - ')
print(int_func(b))
c = input('�������� ����� - ')
print(int_func(c))