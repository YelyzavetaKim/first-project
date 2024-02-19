a = int(input("Введіть a: "))
while a <= 0:
    a = int(input("Введіть ще раз a (повинно бути додатнім): "))
b = int(input("Введіть b: "))
while b <= 0:
    b = int(input("Введіть ще раз b (повинно бути додатнім): "))
if a > b:
    r = a * b + 21
elif a == b:
    r = -5
else:
    r = 3 * a / b + 1
print("Результат обчислення виразу:", r)