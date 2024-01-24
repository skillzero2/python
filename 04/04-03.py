num = int(input("Введите число. \n"))
count = 0
for i in range(num+1):
 i = count ** 3
 print("Куб числа", count, "равен", i)
 count +=1