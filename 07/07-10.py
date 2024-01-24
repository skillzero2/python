def encrypt(s, k):
    let = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    rez = ''
    for i in s:
        if i in let:
            c = let.find(i)
            key = c + k
            if key > len(let):
                key = key % 66
            elif key < 0:
                key = key % 66
            rez += let[key]
        else:
            rez += i
    print(rez)
    return rez
 
s = input('CeZ:')
k = int(input('Key:'))
encrypt(s, k)