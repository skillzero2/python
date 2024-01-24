n = int(input("Введите натуральное число n: "))

numbers = []
for i in range(n):
    number = int(input("Введите число: "))
    numbers.append(number)

sign = 1
result = 0
for number in numbers:
    result += sign * number
    sign *= -1

print("Знакочередующаяся сумма ряда:", result)