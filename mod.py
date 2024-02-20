def daystogoal(M, K):
    distance = M
    days = 1
    while distance <= 50:
        distance += distance * (K / 100)
        days += 1
    return days
