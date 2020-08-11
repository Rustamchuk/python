#FIRST
a = open('lesson.txt', 'w', encoding="utf-8")
b = ''
c = []
while b != '\n':
    b = input('Вводите слова, когда надоест нажмите enter - ') + '\n'
    c.append(b)
a.writelines(c)
a.close()
#SECOND
a = open('text.txt', 'r', encoding='utf-8')
b = list(a.read())
c = b.count('\n') + 1
print(f"Количество строк - {c}")
print(f"Количество слов - {c + b.count(' ')}")
a.close()
'''#THIRD
a = open('text.txt', 'r', encoding='utf-8')
b = list(a.read())
c = ''
d = []
money = []
for i in range(b.count('\n')+1):
    e = a.readline(i)
    for j in e:
        try:
            j = int(j)
            c += str(j)
            d.append(i)
        except:
            d = []
            c = []
        if int(c) < 20000:
            print(d)
    d = []
    c = []'''
#Не получилось решить...
#FOURTH
a = open('text.txt', 'r', encoding='utf-8')
b = ['Один - 1\n', 'Два - 2\n', 'Три - 3\n', 'Четыре - 4']
c = open('text2.txt', 'w', encoding='utf-8')
c.writelines(b)
#FIVTH
a = open("text.txt", 'w', encoding='utf-8')
b = ''
d = []
summ = 0
while b != '0':
    b = input('Вводите числа, для остановки наберите 0 - ')
    d.append(b)
a.writelines(d)
a.close()
a = open('text.txt', 'r', encoding='utf-8')
for line in a.read():
    summ += int(line)
print(summ)
a.close()
#SIXTH
a = open('text.txt', 'r', encoding='utf-8')
b = list(a.read())
d = {}
summ = 0
f = 0
for i in range(b.count('\n')+1):
    c = a.readline(i)
    e = list(c)
    if 'Информатика' in c:
        for j in e:
            try:
                j = int(j)
                f = ''
                f += str(j)
            except:
                summ += int(f)
                f = 0
        k = {'Информатика': summ}
        d.update(k)
        summ = 0
    if 'Физкультура' in c:
        for j in e:
            try:
                j = int(j)
                f =''
                f += str(j)
            except:
                summ += int(f)
                f = 0
        k = {'Физкультура': summ}
        d.update(k)
        summ = 0
    if 'Физика' in c:
        for j in e:
            try:
                j = int(j)
                f = ''
                f += str(j)
            except:
                summ += int(f)
                f = 0
        k = {'Физика': summ}
        d.update(k)
        summ = 0
print(d.copy())
a.close()
'''#SEVENTH
a = open('text.txt', 'r', encoding='utf-8')
money = 0
f = 0
s = 0
for i in a:
    c = a.readline()
    for j in c:
        try:
            j = int(j)
            f = str(f)
            f += str(j)
        except:
            money += int(f)
            s = int(f)
            f = 0
    money -= s*2
    print(money)
    money = 0
a.close()'''