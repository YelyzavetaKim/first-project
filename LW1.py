#Task1
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

#Task2
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

start = 5
end = 25

fib_series = fibonacci(end)
print("Ряд Фібоначчі від", start, "до", end, "члену:")
print(fib_series[start:end])

fib_count = end - start
print("Кількість членів ряду Фібоначчі:", fib_count)

#Task3
N = int(input("Введіть ціле число N (1<N<9): "))
while N <= 1 or N >= 9:
    N = int(input("Введіть ще раз ціле число N (1<N<9): "))
for i in range(1, N + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
    