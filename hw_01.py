# Урок 1. Знакомство с Python

# Задание 1
# Поработайте с переменными, создайте несколько, выведите на экран, запросите у
# пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

print('Задание 1 "Work with variables"')

var_int = 123
var_float = 123.123
var_complex = complex(1, 2)
var_str_digits = "123"
var_str = "one two tree"
var_none = None
var_bool = True

print(f'var_int = {var_int}')
print(f'var_float = {var_float}')
print(f'var_complex = {var_complex}')
print(f'var_str_digits = {var_str_digits}')
print(f'var_str = {var_str}')
print(f'var_none = {var_none}')
print(f'var_bool = {var_bool}')

var_int = int(input('\nВведите десятичное число: '))
var_float = float(input('Введите вещественное число: '))
var_complex = complex(input('Введите комплексное число: '))
var_str = input('Введите строку: ')

print()

print(f'var_int = {var_int}')
print(f'var_float = {var_float}')
print(f'var_complex = {var_complex}')
print(f'var_str = {var_str}')



# Задание 2
# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

print('Задание 2 "Time Format"')

input_seconds = int(input('Введите время в секундах: '))
hours = input_seconds // 3600
minutes = input_seconds//60%60
seconds = input_seconds%60

print(f'Секунды в часы, минуты и секунды (чч:мм:cc) : {hours:02}:{minutes:02}:{seconds:02}')

print(f'Секунды в часы, минуты и секунды (чч:мм:cc) : {input_seconds//3600:02}:{input_seconds//60%60:02}:{input_seconds%60:02}')



# Задание 3
# Программа "Sum Number"
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

print('Задание 3 "Sum number"')

number = int(input('Введите целое число: '))
n1 = number
n2 = int(str(number) * 2)
n3 = int(str(number) * 3)
print(n1 + n2 + n3)



# Задание 4
# Пользователь вводит целое положительное число. Найдите самую
# большую цифру в числе. Для решения используйте цикл while и арифметические операции. 612345   61

max_digit = 0
print('Задание 4 "Maximum digit in number"')
positive_int_num = int(input('Введите положительное целое число: '))


while positive_int_num > 0:
    
    digit = positive_int_num % 10

    if digit > max_digit:
        max_digit = digit
    positive_int_num = positive_int_num // 10

print(f'Самая большая цифра в числе = {max_digit}')



# Задание 5
# Запросите у пользователя значения выручки и издержек фирмы. Определите, 
# с каким финансовым результатом работает фирма. Например, прибыль — выручка больше издержек, 
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.

print('Задание 5 "Financial result of a firm"')
proceed = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
fin_res = proceed - costs

if fin_res > 0:
    print('Фирма работает с прибылью (выручка больше издержек)')
elif fin_res < 0:
    print('Фирма работает в убыток (издержки больше выручки)')
else:
    print('Фирма работает в ноль')



# Задание 6
# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

print('Задание 6 "Financial result of a firm"')
proceed = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
fin_res = proceed - costs

if fin_res > 0:
    rentability = fin_res / proceed
    print(f'Фирма работает с прибылью. Рентабельноть (соотношение прибыли к выручке): {rentability}')
    number_employees = int(input('Введите количество сотрудников фирмы: '))
    one_employee_proceed = proceed / number_employees
    print(f'Прибыль фирмы в расчете на одного сотрудника равна: {one_employee_proceed}')
elif fin_res < 0:
    print('Фирма работает в убыток')
else:
    print('Фирма работает в ноль')



# Задание 7.
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня. Например: a = 2, b = 3. Результат:
#
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

day = 1
print('Задание 7 "Run training"')
first_run = int(input('Введите результат бега в первый день, км: '))
final_run = int(input('Введите цель бега, км: '))

while first_run <= final_run:
    day += 1
    first_run = first_run + first_run * 0.1
    print(f'{day}-й день: {first_run:.3} км')

print(f'Ответ: на {day}-й день спортсмен достиг результата - не менее {final_run} км')
