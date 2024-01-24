n = int(input("Введите количество секунд: "))

if n < 0:
    print("Пуск")
else:
    for i in range(n, -1, -1):
        print(f"Осталось секунд: {i}")

    print("Пуск")