q = int(input())
a = []
for i in range(q):
    s = input()
    if 'лук' not in s:
        a.append(s)
print(', '.join(a))