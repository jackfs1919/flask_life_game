##%%
import numpy as np

numbers = np.array([5, 12, 15, 20, 25, 30, 35])

condition1 = numbers[np.equal(np.greater(numbers, 10), np.less_equal(numbers, 30))] # больше 10 и не больше 30
condition2 = numbers[np.not_equal(numbers, 15)] # и не равны 15

filtered_numbers = numbers[np.isin(condition1, condition2)] # определите, какие числа удовлетворяют заданным критериям

print(f'Числа, удовлетворяющие условиям: {filtered_numbers}')