#№%%
from termcolor import colored

# список цветов (последовательность будет циклически повторяться)
colors = ['black', 'green', 'blue']

lines = [
    "Первая строка текста",
    "Вторая строка текста",
    "Третья строка текста",
    "Четвёртая строка текста",
    "Пятая строка текста",
]

for i, line in enumerate(lines):
    color = colors[i % len(colors)]
    print(colored(line, color, "on_yellow"))