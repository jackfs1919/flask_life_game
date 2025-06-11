import json
import os
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data_workers.json')
with open(file_path, 'r') as file:
    workers = json.load(file)
x = 'firefighter'
print('---------------------')
print(f'| 20-29  | {68}')
print(f'| 30-39  | {136}')
print(f'| 40-49  | {170}')
print(f'| 50-59  | {170}')
print(f'| 60-69  | {170}')
print('---------------------')
print(f'| FEMALE | {14}')
print(f'| MALE   | {15}')
print('---------------------')
print(workers[0])