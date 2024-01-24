n = int(input("Введите количество тестируемых людей: "))

iq_list = []
for i in range(n):
    iq = int(input("Введите IQ человека: "))
    iq_list.append(iq)

average_iq = sum(iq_list) / n

for i in range(n):
    if i == 0:
        print("0")
    elif iq_list[i] > average_iq:
        print(">")
    elif iq_list[i] < average_iq:
        print("<")
    else:
        print("0")