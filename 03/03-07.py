a1 = 1
a2 = 1000
b = ''
d = 0
c = d
 
print('Загадайте число от 1 до 1000.')
while b != '=':
    c = (a1 + a2) // 2
    if c == d:
        c == c - 1
    print(c, '?')
    b = input('>, <, = :')
    if b == '>':
        a1 = c
    elif b == '<':
        a1 = c
    elif b == '=':
        print('Угадал')
d = c