
import json

# Задание 1
# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
# Об окончании ввода данных будет свидетельствовать пустая строка.
# File_object.writelines(L) for L = [str1, str2, str3] 

# w – open a file for writing. If the file doesn’t exist, the open() function creates a new file. 
#     Otherwise, it’ll overwrite the contents of the existing file.
# x – open a file for exclusive creation. If the file exists, 
#     the open() function raises an error (FileExistsError). Otherwise, it’ll create the text file.

try:

    with open('hw_05_01.txt', 'w', encoding="UTF-8") as f:
        while True:
            str_to_f = input()
            if len(str_to_f) == 0:
                break
            f.write(str_to_f + "\n")

except Exception as e:
    print(f'Error hw_05_01! Something wrong {str(e)}')


# Задание 2
# Создать текстовый файл (не программно), сохранить в нём несколько строк, 
# выполнить подсчёт строк и слов в каждой строке.
try:


    name_file_05_02 = 'hw_05_02.txt'
    with open(name_file_05_02, 'r', encoding="UTF-8") as f:
        #num_lines = sum(1 for line in f)   
        read_string_list = f.readlines()
        print(f'Total lines in file {name_file_05_02}: {len(read_string_list)}')
        for num, el in enumerate(read_string_list):
            print(f'Words in string {num + 1} is {len(el.split())}')

except Exception as e:
    print(f'Error hw_05_02! Something wrong {str(e)}')


# Задание 3
# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
# Выполнить подсчёт средней величины дохода сотрудников.

# Пример файла:
# Иванов 23543.12
# Петров 13749.32

try:

    name_file_05_03 = 'hw_05_03.txt'
    with open(name_file_05_03, 'r', encoding="UTF-8") as f:
        amount_of_income = 0
        read_string_list = f.readlines()
        number_of_employee = len(read_string_list)
        for line in read_string_list:
            data_in_string = line.split()
            if float(data_in_string[1]) < 20000:
                print(f'Employee {data_in_string[0]} has a salary of less than 20.000')
            amount_of_income += float(data_in_string[1])
        print(f'Average employee income is {(amount_of_income / number_of_employee):.3f}')

except IOError:
    print('Error hw_05_03! Please, check check file existence')
except ZeroDivisionError:
    print('Error hw_05_03! Division by zero! Check number of employee. You work without workers? :)')
except Exception as e:
    print(f'Error hw_05_03! Something wrong {str(e)}')



# Задание 4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские. 
# Новый блок строк должен записываться в новый текстовый файл.

#pip install googletrans==4.0.0-rc1
#from googletrans import Translator

try:

    thisdict = {
    "One":      "Один",
    "Two":      "Два",
    "Three":    "Три",
    "Four":     "Четыре"
    }

    name_file_05_03 = 'hw_05_04.txt'
    with open(name_file_05_03, 'r', encoding="UTF-8") as f_src:
        read_string_list = f_src.readlines()
    with open('hw_05_04_dest.txt', 'w', encoding="UTF-8") as f_dest:
        #translator = Translator()  #  initialization the Translator object
        for string in read_string_list:
            words_string = string.split()
            res = " ".join(thisdict.get(ele, ele) for ele in words_string)
            #
            #trans_to_rus = translator.translate(words_string[0],src='en',  dest='ru')
            #trans_to_rus = thisdict[words_string[0]] if words_string[0] in thisdict else words_string[0]
            #
            f_dest.write(res+"\n")

except Exception as e:
    print(f'Error hw_05_04! Something wrong {str(e)}')



# Задание 6
# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. 
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: 
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

try:
    print('Start hw_05_06')
    name_file_05_06 = 'hw_05_06.txt'
    with open(name_file_05_06, 'r', encoding="UTF-8") as f:
        dict_subjects = {}
        for line in f.readlines():
            dict_subjects["".join(filter(str.isalpha, line.split()[0]))] = sum([int(i) for i in ''.join((ch if ch in '0123456789' else ' ') for ch in line).split()] )
        print(dict_subjects)
except Exception as e:
    print(f'Error hw_05_06! Something wrong {str(e)}')



# Задание 7
# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет 
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь 
# со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

try:
    print('Start hw_05_07')
    name_file_05_07 = 'hw_05_07.txt'
    with open(name_file_05_07, 'r', encoding="UTF-8") as f:
        dict_firms = {}
        average_profit_value = 0
        count_positive_profit = 0

        for line in f.readlines():

            read_words_list = line.split()
            balance_firm = float(read_words_list[2]) - float(read_words_list[3])
            if balance_firm > 0:
                count_positive_profit += 1
                average_profit_value += balance_firm
            dict_firms[read_words_list[0]] = balance_firm

        average_profit_value = round((average_profit_value / count_positive_profit), 4)
        json_list = []
        json_list.append(dict_firms)
        json_list.append({'average_profit': average_profit_value})

        print(f'Final json_list is : {json_list}')        
except Exception as e:
    print(f'Error hw_05_07! Something wrong {str(e)}')
