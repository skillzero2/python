my_sets = []
 
n = int(input())
 
for _ in range(n):
    s = set()
    for j in range(int(input())):
        sur = input()
        s.add(sur)
    my_sets.append(s)
 
for i in range(n - 1):
    f = (my_sets[i] & my_sets[i + 1])
    my_sets[i + 1] = f
 
for j in my_sets[-1]:
    print(j)