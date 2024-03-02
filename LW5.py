#Task1
n = int(input("n = "))
print(f"Enter {n} array elements:")
arr = [int(input()) for _ in range(n)]
print("Original array: ", arr)

sum_positive_multiple_of_three = 0

for num in arr:
    if num > 0 and num % 3 == 0:
        sum_positive_multiple_of_three += num
        
print("Сума додатніх елементів, кратних трьом:", sum_positive_multiple_of_three)

#Task2
n=7
a = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if i >= j:
            a[i][j] = n - i + j
        else:
            a[i][j] = n - j + i
            
for r in a:
    print(*r)
