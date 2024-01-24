n = int(input())
cat = False
for i in range(n):
    fraza = input()
    if 'КОТ' in fraza or 'кот' in fraza or 'Кот' in fraza:
        cat = True
if cat:
    print('МЯУ')
else:
    print('НЕТ')