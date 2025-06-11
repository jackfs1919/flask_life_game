import json
import os
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data_workers.json')
with open(file_path, 'r') as file:
    workers = json.load(file)
x = 'firefighter'
blank = dict.fromkeys(('20-29', '30-39', '40-49', '50-59', '60-69', 'FEMALE', 'MALE'), 0)

print('---------------------')
print(f'| 20-29  | {blank['20-29']}')
print(f'| 30-39  | {blank['30-39']}')
print(f'| 40-49  | {blank['40-49']}')
print(f'| 50-59  | {blank['60-69']}')
print(f'| 60-69  | {blank['FEMALE']}')
print('---------------------')
print(f'| FEMALE | {blank['MALE']}')
print(f'| MALE   | {blank['MALE']}')
print('---------------------')
print(blank)