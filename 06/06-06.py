n,m = list(map(int,input().split()))
houm = [input() for _ in range(n)]
for _ in range(m):
    print(('NO','YES')[input() in houm])