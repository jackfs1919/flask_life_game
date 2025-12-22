#№%%
from itertools import permutations
# from pprint import pprint as print
lst = ['Тестирование новых', 'Бета-тестирование', 'Основной', 'стабильного билда']
with open('stepic.txt', 'w', encoding="utf8") as f:
    print(list(permutations(lst)), file=f)
