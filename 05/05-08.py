a = ''
w = 0
h = 0
f = 0
flag = True
while a != 'СТОП':
    a = input()
    w = w + 1
    if ('кот' in a or 'Кот' in a):
        if flag:
            h = w
        flag = False
        f = f + 1
if h == 0:
    print(f, -1)
else:
    print(f, h)