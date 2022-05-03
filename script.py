print('Hello, world!')
print(1 + 2)

hello = [n for n in 'Hello' if n in 'hello']
print(hello)

multiple = [i * j for i in range(1, 3) for j in range(1, 4)]
print(multiple)

NISHIN = [0,0,0,0,0,0,0,0]
j = int(167)
for k in range(0, 8, 1):
    NISHIN[k] = j % 2
    j = j //2   
print(NISHIN)

# ２章
fp = open('sample.txt', 'wt')
fp.write('Hello\n')
fp.write('Good morning\n')
print('hello', file=fp)
fp.close()

with open ('sample.txt', 'rt') as fp:
    data = fp.read()

for line in data:
    print(line, end='')

try:
    d = int(input('数字を入れてください >'))
    print(d * 2)
except ValueError:
    print('それは数字ではありません')

import datetime
print(datetime.date.today())

def triangle_area(base, height):
    area = base * height / 2
    return area

print(triangle_area(5, 3))

print(int(5))

sample = [1, 2, 3, 4, 5]
print(tuple(sample))

drinklist = ['coffee', 'tea', 'water']
print(list(enumerate(drinklist)))

for i, drink in enumerate(drinklist):
    print(i, drink)

meallist = ['steak', 'salad', 'dessert']
print(list(zip(meallist, drinklist)))

dict_a = dict(steak=1, salad=2, dessert=3)
print(dict_a)

def article(title, number=1, content='content'):
    content = 'default content'
    print(title, end=' ')
    print(number, end=' ')
    print(content)

article('Python tutorial', content='Python Love')

def double(x):
    return x * 2
fruitlist = ['kiwi', 'papaya', 'mango']

print(list(map(double, fruitlist)))