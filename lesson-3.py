#FIRST
def division(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        return '[Ошибка!]\nЭмм... На ноль делить нельзя...'
    return c

k = int(input('Какая будет первая цифра?\n'))
z = int(input('А вторая?\n'))
print(f'Их деление = {division(k, z)}')
#SECOND
def information():
    try:
        name = input('Имя - ')
        surname = input('Фамилия - ')
        birth = input('Дата рождения - ')
        city = input('Город проживания - ')
        email = input('Почта - ')
        number = input('Номер телефона - ')
    except: 
        print('Кажется где-то что-то не так...')
    return f'Итак Вы {name} {surname}, родились {birth}, живете в городе {city}, ваша почта {email} и номер телефона {number}\n Если все правильно нажмите Enter'

print(information())
#THIRD
def my_func(a, b, c):
    maxx_1 = max(a, b, c)
    maxx_2 = [a, b, c]
    maxx_2.remove(maxx_1)
    maxx_2 = max(maxx_2)
    sum = ord(maxx_1) + ord(maxx_2)
    return sum

a1 = input('Введите символ - ')
b1 = input('Введите символ - ')
c1 = input('Введите символ - ')
print(f'Сумма максимальных членов равна {my_func(a1, b1, c1)}' )
#FOURTH
def my_func(x, y):
    x **= y
    return x
def my_func2(x, y):
    z = 1
    for i in range(y):
        z *= x
    return z

x1 = int(input('Какое число возводим в степень? '))
y1 = int(input('В какую степень? '))
print(f'Ответ: {my_func(x1, y1)}')
print(f'Ответ: {my_func2(x1, y1)}')
#FIFTH
#print('Вводите числа через пробел для подсчета суммы. Стоп число - STOP')
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
b = input('Напишите слово - ')
print(int_func(b))
c = input('Напишите слова - ')
print(int_func(c))