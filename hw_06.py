from itertools import cycle, islice
from time import sleep
from random import randint

# Задание 1
# Создать класс TrafficLight (светофор).
# Определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, 
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

class TrafficLight:
    __color_times = {   'Красный':  7,
                        'Желтый':   2,
                        'Зеленый':  7}
    def __init__(self):
        pass

    def running(self, countnumber = 3):
          for color in islice(cycle(self.__color_times.keys()), int(countnumber)):
            print(color)
            #sleep(self.__color_times.get(color)) 
            t = self.__color_times.get(color)
            while t:
                #timer = datetime.timedelta(seconds = t)
                mins, secs = divmod(t, 60)
                print(f"{mins:02d}:{secs:02d}", end="\r")
                sleep(1)
                t -= 1   


print("Press Ctrl-C to terminate")
try:
    tl = TrafficLight()
    tl.running(7)
except KeyboardInterrupt:
    print('Terminate!')
else:
    print('End the program.')


# Задание 2
# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, 
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 cm = 12500 т.

class Road:
    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def calculating_mass_asphalt(self):
        return self._length * self._width * 25 * 0.05 / 1000


print('Program "Calculating mass of asphalt"')
try:
    avtodor_crimea = Road(20, 5000)
    print(f'asphalt mass = {avtodor_crimea.calculating_mass_asphalt()}')
except ValueError:
    print('Road!Please enter a digits!')
except:
    print('Road!Error')

# Задание 3
# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, 
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и 
# дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, 
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}
        self.separator = ' '

class Position(Worker):

    def get_full_name(self):
        return self.name + self.separator + self.surname

    def get_total_income(self):
        return  self._income['wage'] + self._income['bonus']

print('Program "Get total income of worker"')

try:
    director = Position('Ivan', 'Ivanov', 'director',100, 100.45567)

    print(f"Full name is : {director.get_full_name()}")
    print(f"Sallary of : {director.get_total_income():.4f}")

except ValueError:
    print('Please enter a digits!')
except:
    print('get_total_income()')


# Задание 4
# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, 
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, 
# выведите результат. 
# Вызовите методы и покажите результат.

class Car:
    color_car = {'чёрный': '\033[30m', 'красный': '\033[31m', 'зелёный': '\033[32m', 'жёлтый': '\033[33m',
               'синий': '\033[34m', 'фиолетовый': '\033[35m', 'бирюзовый': '\033[36m',
                 'black': '\033[30m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m',
                'blue': '\033[34m', 'purple': '\033[35m', 'turquoise': '\033[36m'}

    direction_list = ['left', 'right', 'straight ahead']

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self.show_speed()

    def go(self):
        return print(f'car {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]}\033[00m is going.')

    def stop(self):
        return print(f'car {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]}\033[00m is stop.')

    def turn(self, direction):
        return print(f'car {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]}\033[00m is going to {direction}.')

    def show_speed(self):
        return print(f'speed of car {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]}\033[00m is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            if_high_speed_info = f'speed {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]}\033[00m to high!' \
                                 f' Above than 60! Now speed is {self.speed}'
            return print(if_high_speed_info)
        if_normal_speed_info = f'speed {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]}\033[00m is {self.speed}'
        return print(if_normal_speed_info)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            if_high_speed_info = f'speed {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]}\033[00m to high! ' \
                                 f'Above than 60! Now speed is {self.speed}'
            return print(if_high_speed_info)
        if_normal_speed_info = f'speed {self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]}\033[00m is {self.speed} '
        return print(if_normal_speed_info)


class PoliceCar(Car):
    def turn(self):
        return print(f'car \033[6m{self.color_car[self.color]}"{self.name}"{self.color_car["чёрный"]}\033[00m is going to'
                     f' {self.direction_list[randint(0, 2)]}.\033[00m')

    def go(self):
        for t in range(20):
            print(f'\033[{"31" if t%2 == 0 else "34"}m{self.name}\033[00m is going', end='\r')
            sleep(.1)
        return print(f'\033[34m{self.name}\033[00m is going')


print('Program "Type of cars"')
# town_car
town_car = TownCar('Town car', 50, 'purple', False)
town_car = TownCar('Town car', 80, 'зелёный', False)
# work_car
work_car = WorkCar('Work car', 130, 'жёлтый', False)
work_car = WorkCar('Work car', 30, 'синий', False)
work_car.go()
work_car.turn('left')
# police_car
car_police = PoliceCar('Police car', 110, 'красный', True)
print(f'name car is: {car_police.name}')
car_police.show_speed()
# sport_car
sport_car = SportCar('Sport car', 300, 'turquoise', False)
# police_car мигает
car_police.turn()
car_police = PoliceCar('Patrol police car', 110, 'красный', True)
car_police.go()


# Задание 5
# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery():
    _title = 'канцелярская принадлежность'
    def draw(self):
        return print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        return print(f'Запуск отрисовки {self._title}: ручка')


class Pencil(Stationery):
    def draw(self):
        return print(f'Запуск отрисовки {self._title}: карандаш')


class Handle(Stationery):
    def draw(self):
        return print(f'Запуск отрисовки {self._title}: маркер')

print('Program "Stationery"')
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()

