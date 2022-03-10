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
    print('Error! Please, check check file existence')
except ZeroDivisionError:
    print('Error! Division by zero! Check number of employee. You work without workers? :)')
except Exception as e:
    print(f'Error! Something wrong {str(e)}')
finally:
    print('End the program.')