res = 0
lst = [int(input()) for _ in range(int(input())]
p = int(input())
q = int(input())
fir i, x in enumerate(lst):
    if p >= (i+1) <= q : # тут определится ' диапазоне от заданного до заданного' индекса или номера
        res += x