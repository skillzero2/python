num = int(input("Введите натуральное число: "))

divisors = []
for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)

if len(divisors) == 2:
    prime_message = "ПРОСТОЕ"
else:
    prime_message = "НЕТ"

divisors_str = " ".join(str(divisor) for divisor in divisors)

print(divisors_str)
print(prime_message)