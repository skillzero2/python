c = 'НЕТ'
for i in range(int(input())): 
    if 'кот' in input().lower():
        c = 'МЯУ'
        break
print(c)