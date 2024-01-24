s = input().split()
s_1 = []
s_2 = []
summa = 0
 
for i in range(int(s[0])):
    row = []
    k = input().split()
    summa += int(k[0]) * int(k[1].lstrip('*'))
    for j in k:
        if j[0] not in '123456789':
            row.append(int(j[1:]))
        else:
            row.append(int(j))
    s_2.append(row)
 
r = int(s[1]) - summa
print(r)
 
if r != 0:
    for i in range(int(s[0])):
        if s_2[i][0] * s_2[i][1] != s_2[i][2]:
            s_1.append(str(i + 1))
    print(' '.join(s_1))
