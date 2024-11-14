##%%
class SparseArray:
    def __init__(self, *args):
        # Инициализируем массив с переданными аргументами
        self.values = list(args)

    def __getitem__(self, index):
        # Если индекс больше или равен длине массива, расширяем массив
        if index >= len(self.values):
            self.values.extend([None] * (index + 1 - len(self.values)))
        return self.values[index]

    def __setitem__(self, index, value):
        # Если индекс больше или равен длине массива, расширяем массив
        if index >= len(self.values):
            self.values.extend([None] * (index + 1 - len(self.values)))
        self.values[index] = value

    def __delitem__(self, index):
        # Если индекс в пределах текущего диапазона массива, устанавливаем значение по индексу на None
        if index < len(self.values):
            self.values[index] = None

    def __len__(self):
        # Возвращаем длину массива (включая разреженные элементы)
        return len(self.values)

    @property
    def values(self):
        # Возвращаем кортеж значений массива
        return tuple(self._values)

    @values.setter
    def values(self, value):
        # Устанавливаем значения массива
        self._values = list(value)

array = SparseArray(1, 2, 3)
print(array.values)
print(array[7])
print(array.values)
array[6] = 100
print(array.values)
array[10] = 200
print(array.values)
del array[1]
print(array.values)
print(len(array))