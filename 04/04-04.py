product = 1

for _ in range(6):
    num = int(input("Введите целое число: "))
    if num != 0:
        product *= num

print("Произведение чисел без учета нулей:", product)