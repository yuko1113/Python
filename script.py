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