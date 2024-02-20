import math

def expression(alpha, beta):
    z = math.sin(alpha + beta) * math.sin(alpha - beta)
    return z

def daystogoal(M, K):
    distance = M
    days = 1
    while distance <= 50:
        distance += distance * (K / 100)
        days += 1
    return days

alpha = int(input("Введіть значення alpha: "))
beta = int(input("Введіть значення beta: "))

print("Значення виразу z =", expression(alpha, beta))

M = int(input("Введіть кількість кілометрів, яку спортсмен пробігає за перший день (M): "))
K = int(input("Введіть відсоток збільшення норми пробігу кожного наступного дня (K): "))

days = daystogoal(M, K)
print("Спортсмену знадобиться", days, "днів, щоб пробігти більше 50 км")
