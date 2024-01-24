login = input("Введите логин: ")
email = input("Введите адрес: ")
if '@' in login:
    print('Некорректный логин')
elif '@' not in email:
    print('Некорректный адрес')
else:
    print('OK')