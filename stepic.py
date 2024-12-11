##%%
# from itertools import permutations
# from pprint import pprint as print
# x = ('исправить', 'создать', 'указать', 'добавить nk', 'добавить')
# y = ('init', 'CMake', 'secur', 'einit', 'например')
# print(list(permutations(y)))
# def find_different_indexes(s1: str, s2: str) -> list[int]:
#     pass

# print(find_different_indexes('abcd', 'artd'))

def find_different_indexes(str1, str2):
    # Проверка на равенство длины строк
    if len(str1) != len(str2):
        raise ValueError("Строки должны быть одной длины.")
    
    # Инициализация списка для хранения индексов
    different_indexes = []

    # Использование enumerate для перебора символов и индексов
    for index, (char1, char2) in enumerate(zip(str1, str2)):
        if char1 != char2:
            different_indexes.append(index)

    return different_indexes

print(find_different_indexes('abcd', 'artd'))



