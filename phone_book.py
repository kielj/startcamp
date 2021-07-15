menu = ['한식', '일식', '중식', '양식']

import random

lunch = random.choice(menu)

# print(lunch)

# print(random.choice(menu))

number = {'한식' : '111-222', '일식' : '333-444', '중식' : '555-666', '양식' : '777-888'}

# print(number[lunch])
print('오늘의 점심은 ',lunch,'입니다. 전화번호는 ',number[lunch],'입니다.')
print(f'오늘의 점심은 {lunch}입니다. 전화번호는 {number[lunch]}입니다.')
