# Задание 1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div_func(numerator, denominator): 
    return numerator / denominator

print()
print('Задание 1. "Деление"')
try:
    #result = div_func(numerator=float(input('Делимое: ')), denominator=float(input('Делитель: ')))
    print ("Результат", f"{ div_func(numerator=float(input('Делимое: ')), denominator=float(input('Делитель: '))):.2f}")
except ValueError:
    print("Ошибка ввода значений!")
except ZeroDivisionError:
    print("Деление на ноль!")
#else:
#    print ("Результат", f'{result:.2f}')

# Задание 2
# Выполнить функцию, которая принимает несколько параметров, 
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
# Функция должна принимать параметры как именованные аргументы. 
# Осуществить вывод данных о пользователе одной строкой.

print()
print('Задание 2. "Вывод данных о пользователе"')

def user_data(name, surname, year_of_birth, current_city, email, phone):
    print(f'{name}, {surname}, {year_of_birth}, {current_city}, {email}, {phone}')

user_data(surname=input('Enter your surname: '), name=input('Enter your name: '), year_of_birth=input('Enter your year of birth: '),
          current_city=input('Enter your current_city: '), email=input('Enter your email: '), phone=input('Enter your phone: '))


# Задание 3
#Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
print()
print('Задание 3. "Сумма наибольших двух аргументов из трех"')
def my_func_sum(arg_1, arg_2, arg_3):
    return sum(sorted([arg_1, arg_2, arg_3],reverse=True)[:2])

print(f'Сумма двух наибольших элементов {my_func_sum(10, 3, 9)}')

# Задание 4
# Программа принимает действительное положительное число x и целое отрицательное число y. 
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). 
# При решении задания нужно обойтись без встроенной функции возведения числа в степень
print()
print('Задание 4. "Возведение числа x в степень -y"')

def my_func_exponentiation(x, y):
    exponentiation = 1
    for i in range(abs(y)):
        exponentiation = exponentiation * x
    return 1 / exponentiation

print(my_func_exponentiation(x=int(input('Enter positive number: ')), y=int(input('Enter negative number: '))))

# Задание 5
# Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, 
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. 
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел 
# к полученной ранее сумме и после этого завершить программу.
print()
print('Задание 5. "Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме"')

sum = 0
isRun = True
while isRun:
    for el in input("Строка чисел :").split():
        if el == "*":
            isRun = False
            break
        sum += int(el)
    print(f"Сумма : {sum}") 


# Задание 6
# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, 
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
print()
print('Задание 6. "print(int_func(\'text\')) -> Text"')
def int_func(lower_str):
    return lower_str.title()

print(f'Word in title case: {int_func(input("Enter a word in lower case: "))}')


# Задание 7
# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, 
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. 
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, 
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().
print()
print('Задание 7. "\'text test\' -> Text Test"')
#def int_func(lower_str):
#    return lower_str.title()

#print(' '.join([(lambda str: str.title())(el) for el in input("Строка :").split()]))
print(' '.join([int_func(el) for el in input("Строка :").split()]))
