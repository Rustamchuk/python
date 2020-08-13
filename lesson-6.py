# FIRST
from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            print(self.__color[0])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            print(self.__color[2])
            sleep(10)
            print(self.__color[1])
            sleep(2)


a = TrafficLight()
print(a.running())

# SECOND


class Road:
    _length = 5000
    _width = 20

    def weight(self, one_weight, depth):
        print(f'weight = {self._length * self._width * one_weight * (depth / 100)}')


a = Road()
b = int(input('Write weight ih 1 metre(in kg)'))
c = int(input('Write depth(in sm)'))
print(a.weight(b, c))

# THIRD


class Worker:
    name = 'Vladimir'
    surname = 'Ivanov'
    position = 'policeman'
    money = {'wage': 50000, 'bonus': 0}
    _income = money.get('wage') + money.get('bonus')


class Position(Worker):

    def get_full_name(self, name, surname):
        print(f'{name} {surname} got ', end='')

    def get_total_income(self, bonus):
        self._income += bonus
        print(self._income, 'rub.')


a = Position()
b = input('Name - ')
c = input('Surname - ')
prize = int(input('Bonus - '))
a.get_full_name(b, c)
a.get_total_income(prize)

# FOURTH
class Car:
    speed = 0
    color = 'black'
    name = 'mercedes'
    is_police = False
    situation = 'town'
    chellange = 0

    def go(self):
        print("Let's go!")
        if self.situation == 'town':
            self.speed = 50
        elif self.situation == 'work':
            self.speed = 25
        elif self.situation == 'sport':
            self.speed = 100

    def stop(self):
        self.speed = 0
        print('finish?')

    def turn(self, direction):
        if direction == 'right':
            self.speed -= 15
            print('turned right')
        elif direction == 'left':
            self.speed -= 15
            print('turned left')
        elif direction == 'forward':
            print('ok, forward')

    def show_speed(self):
        while True:
            self.go()
            print(self.speed)
            self.speed += 5
            self.turn(input('Where? (right, left, forward)'))
            print(self.speed)
            self.speed += 30
            if self.situation == 'town':
                self.TownCar.town_allow()
            elif self.situation == 'work':
                self.WorkCar.work_allow()
            elif self.situation == 'sport':
                self.SportCar.sport_allow()
            print(self.speed)
            self.speed += 10
            self.chellange += 1
            if self.chellange == 4:
                print('Congratulations! You are good driver! Now you are policeman!')
                self.is_police = True
                self.PoliceCar.check()
            print(self.speed)
            if self.speed == 8:
                print("It's time to stop")
                break
        self.stop()


class TownCar(Car):
    def town_allow(self):
        if self.speed > 60:
            print('Calm down! limited = 60')
            self.speed = 40


class SportCar(Car):
    def sport_allow(self):
        if self.speed > 130:
            print('Calm down! limited = 130')
            self.speed = 80


class WorkCar(Car):
    def work_allow(self):
        if self.speed > 40:
            print('Calm down! limited = 40')
            self.speed = 20


class PoliceCar(Car):
    def check(self):
        print("You don't have limits!")
        self.speed += 200


a = Car()
a.show_speed()

# FIVTH


class Stationary:
    title = 'school'

    def draw(self):
        print('Запуск отрисовки.')
        if self.title == 'pen':
            print('You have a pen')
        elif self.title == 'pencil':
            print('You have a pencil')
        elif self.title == 'handle':
            print('You have a handle')


class Pen(Stationary):
    title = 'pen'


class Pencil(Stationary):
    title = 'pencil'


class Handle(Stationary):
    title = 'handle'

a = input('Карандаш, Ручка или Маркер?')
if a == 'Карандаш':
    b = Pen()
    b.draw()
elif a == 'Ручка':
    b = Pencil()
    b.draw()
elif a == 'Маркер':
    b = Handle()
    b.draw()
