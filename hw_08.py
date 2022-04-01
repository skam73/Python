# Урок 8.1
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
# В рамках класса реализовать два метода. 
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
# Проверить работу полученной структуры на реальных данных.

class MyDate:
    def __init__(self, string):
        self.date = string
    
    @classmethod
    def date_extraction(cls, obj):
        return list(map(int, obj.date.split('-')))

    @staticmethod 
    def is_valid_date(date_as_string): 
        day, month, year = map(int, date_as_string.split('-')) 
        return day > 0 and day <= 31 and month > 0 and month <= 12 and year > 20 and year <= 30


print('Class data with use classmethod, staticmethod')

to_date = input('Please , enter data in format DD-MM-YY: ')
my_dt = MyDate(to_date)
print(f"{to_date} to list {MyDate.date_extraction(my_dt)}")
print(f"{to_date} is {MyDate.is_valid_date(to_date)}")

# Урок 8.2
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя 
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyDivisionByZero(Exception):
    pass

print('MyDivisionByZero')
dividend = input('Enter dividend: ')
divider = input('Enter divider: ')
try:
    if int(divider) == 0:
        raise MyDivisionByZero
    result = int(dividend) / int(divider) 
except MyDivisionByZero:
    print("Ситуация деления на ноль")
except ValueError:
    print('Value error!')
else:
    print(f'Result: {result}')
# finally:
#     print('End MyDivisionByZero.')

# Урок 8.3
# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами. 
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, 
# введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода пользователем 
# очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если введено число. 
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. 
# При этом работа скрипта не должна завершаться.

class NotDigitError(Exception):
    def __init__(self, text):
        self.txt = text

final_list = []

print('8.3 "My NotDigitError"')
while True:
    try:
        input_text = input('Input numbers to write to list. To "Quit" please enter - q: ')
        if input_text == 'q':
            break
        if not input_text.isdigit():
            raise NotDigitError('You enter not digits!')
        final_list.append(int(input_text))
    except NotDigitError as MyErr:
        print(MyErr)

print(f'8.3 Final list is: {final_list}')

# Урок 8.4-8.6
# Начните работу над проектом «Склад оргтехники». 
# Создайте класс, описывающий склад. 
# А также класс «Оргтехника», который будет базовым для классов-наследников. 
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
# В базовом классе определите параметры, общие для приведённых типов. 
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании. 
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, 
# можно использовать любую подходящую структуру (например, словарь).

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Sklad:
    def __init__(self):
        self._dict = {}
 
    def add_to(self, equipment):
        ''' добавляем в словарь обьект по его названию, в значении
        будет список экземпляров этого оборудования'''
        self._dict.setdefault(equipment.group_name(), []).append(equipment)
 
    def extract(self, name):
        ''' извлекаем из значения обьект по названию группы.'''
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)
            
 
 
class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.group = self.__class__.__name__
 
    def group_name(self):
        return f'{self.group}'
 
    def __repr__(self):
        return f'{self.name} {self.make} {self.year}'
 
        
class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series
 
    def __repr__(self):
        return f'{self.name} {self.series} {self.make} {self.year}'
 
    def action(self):
        return 'Печатает'
    
     
class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)
 
    def action(self):
        return 'Сканирует'
 
class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)
 
    def action(self):
        return 'Копирует'
 
 
 
sklad = Sklad()
# создаем объект и добавляем
scaner = Scaner('hp','321', 90)
sklad.add_to(scaner)
scaner = Scaner('hp','311', 97)
sklad.add_to(scaner)
scaner = Scaner('hp','330', 99)
sklad.add_to(scaner)
printer = Printer('e-320', 'sony', 126,2018)
sklad.add_to(printer)
# выводим склад
print(sklad._dict)
# забираем с склада и выводим склад
sklad.extract('Scaner')
print()
print(sklad._dict)

# Урок 8.7
# Реализовать проект «Операции с комплексными числами». 
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. 
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), 
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

print('8.7 "ComplexNumber"')

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self):
        return f'{self.a} + {self.b}*i'

a = ComplexNumber(1,1)
b = ComplexNumber(2,2)
print(a + b)
print(a * b)
