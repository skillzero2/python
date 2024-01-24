print(*[x for x in [i**2  for i in map(int,input().split()) if i % 2] if x % 10 != 9], sep = ' ')
11 12 13 14 15 16 17 18 19 20
121 225 361