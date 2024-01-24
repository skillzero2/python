n = -1
c = 0
c1 = 0
while n != 0:
    n = int(input())
    c += 1
    c1 += n
    if c1 == 10:
        print(c)
        break