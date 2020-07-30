#FIRST
a = [25, 'Hello', 2.5, False, 'Bye']
print('Сначала напиши число от 1 до 5 (включительно)')
b = int(input()) - 1
print(type(a[b]))
#SECOND
a.clear()
b = ''
print('Добавляйте слова в список. Когда вам надоест напишите "STOP". В конце я поменяю слова местами')
while b != 'STOP':
    b = input()
    a.append(b)
print(a)
for i in range(len(a)):
    if len(a) >= i + 2:
        a[i], a[i+1] = a[i+1], a[i]
        i += 1
print(a)
#THIRD
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9,10, 11]
a = int(input())
if a  == winter[0] or a == winter[1] or a == winter[2]:
    print('winter')
elif a  == spring[0] or a == spring[1] or a == spring[2]:
    print('spring')
elif a  == summer[0] or a == summer[1] or a == summer[2]:
    print('summer')
elif a  == autumn[0] or a == autumn[1] or a == autumn[2]:
    print('autumn')
#FOURTH
a = list(input())
b = ''
for i in range(len(a)):
    b += a[i]
    if a[i] == ' ':
        print(b)
        b = ''
#FIVTH
print('write rusults')
print('write "stop" if you want')
a = int(input())
b = [a]
c = 0
while a != 'stop':
    a = int(input())
    for i in range(len(b)):
        for j in range(len(b)):
            if a == b[i]:
                c = 1
        if c == 1:
            break
        if a > b[i]:
            b.insert(i-1, a)
        elif a < b[i]:
            b.insert(i+1, a)
        elif a == b[i]:
            b.insert(i+1, a)
    c = 0
    print(b)