
# Lesson 7 Task 1.
# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.
from abc import ABC, abstractmethod
import copy

class Matrix:
    def __init__(self, matrix):
        try:
            self.matrix = copy.deepcopy(matrix)
        except:
            print('Error __init__')

            
    def __str__(self):
        try:
            return '\n'.join(' '.join(map(str, row)) for row in self.matrix)
        except:
            print('Error __str__')

            
    def __add__(self, other):
        try:
            return Matrix(list(map(
                        lambda x, y: list(map(lambda z, w: z + w, x, y)),
                        self.matrix, other.matrix)))
        except:
            print('Error in __add__()')

    def __mul__(self, other):
            raise NotImplementedError
print()
print('Matrix')
matrix_1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
matrix_2 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(matrix_1)
print()
print(matrix_2)
print()
matrix_3 = matrix_1 + matrix_2
print(matrix_3)


# Lesson 7 Task 2.
# Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: 
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: 
# для пальто (V/6.5 + 0.5), 
# для костюма (2*H + 0.3). 
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Clothes(ABC):

    def __init__(self, size, height):
        try:
            self.size = size
            self.height = height
        except:
            print('Error __init__ Clothes')

    # using property decorator
    # a getter function
    @property
    def size(self):
        try:
            return self._size
        except:
            print('Error! size()')

    # a setter function
    @size.setter
    def size(self, size):
        try:
            if not isinstance(size, (int, float)):
                print('Error! you enter not number')
            if size < 46:
                self._size = 44  # устанавливаем размер xs
            elif 46 <= size <= 48:
                self._size = 48  # устанавливаем размер s
            elif 48 < size <= 50:
                self._size = 50  # устанавливаем размер m
            else:
                self._size = 52  # размер l и выше( к сожалению, оверсайза нет, ищите другой магазин...
        except ValueError:
            print('Error! size.setter')

    # a getter function
    @property
    def height(self):
        return self.__height

    # a setter function
    @height.setter
    def height(self, height):
        try:
            if not isinstance(height, (int, float)):
                print('Error! you enter not number')
            if height < 150:
                self.__height = 150  # устанавливаем рост 150
            elif 150 <= height <= 165:
                self.__height = 165  # устанавливаем рост 165
            elif 165 < height <= 180:
                self.__height = 180  # устанавливаем рост 180
            else:
                self.__height = 200  # устанавливаем рост 200
        except ValueError:
            print('Error! height.setter')

    def __str__(self):
        try:
            return f'Сonsuption fabric on {type(self).__name__} need on your size {str(self.size)} / {str(self.height)} is {self.consumption_fabric():.2f} '
        except:
            print('Error __str__ class Coat') 

    @abstractmethod
    def consumption_fabric(self, size, height):
        pass

class Coat(Clothes):

    __const_coat_6_5 = 6.5
    __const_coat_0_5 = 0.5

    def consumption_fabric(self):
        try:
            return self.size / self.__const_coat_6_5 + self.__const_coat_0_5
        except:
            print('Error in consumption_fabric() class Coat')


class Suit(Clothes):

    __const_suit_2 = 2
    __const_suit_0_3 = 0.3

    def consumption_fabric(self):
        try:
            return self.height / self.__const_suit_2 + self.__const_suit_0_3
        except:
            print('Error in consumption_fabric() class Suit')


print()
print("Clothes")

coat = Coat(44,140) 
print(coat) 

suit = Suit(44,180) 
print(suit) 


# Lesson 7 Task 3.
# Реализовать программу работы с органическими клетками, состоящими из ячеек. 
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
# В классе должны быть реализованы методы перегрузки арифметических операторов: 
#   сложение (__add__()), 
#   вычитание (__sub__()), 
#   умножение (__mul__()), 
#   деление (__truediv__()). 
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) 
# деление клеток, соответственно.
# Сложение.     Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание.    Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, 
#               иначе выводить соответствующее сообщение.
# Умножение.    Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление.      Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    def __init__(self, number_cells):
        self.number_cells = number_cells

    def __add__(self, other):
        return  Cell(self.number_cells + other.number_cells) 

    def __sub__(self, other):
        final_cell = max(self.number_cells, other.number_cells) - min(self.number_cells, other.number_cells)
        if final_cell >= 0:
            return Cell(final_cell) 
        else:
            raise Exception(f'Разница меньше нуля')

    def __mul__(self, other):
        return  Cell(self.number_cells * other.number_cells) 

    def __truediv__(self, other):
        return Cell(self.number_cells // other.number_cells) 

    def __str__(self):
        return f'Cell: {self.number_cells}'

    def make_order(self, num_cells_in_row):
        try:
            print('Make order: ')
            count_cells = divmod(self.number_cells, num_cells_in_row)
            for i in range(count_cells[0]):
                print('*' * num_cells_in_row, end='')
                print()
            for j in range(count_cells[1]):
                print('*', end='')
            print()                
        except:
            print('Error make_order()')

print()
print("Cell order")
a = Cell(22)
b = Cell(11)
print(a)
print(a+b)
print(a-b)
print(b-a)
print(a*b)
print(b / a)
c = Cell(10)
c.make_order(3)
c.make_order(5)
c.make_order(8)