#Task1
def delete():

    A = list(map(int,input('Елементи списку: ').split()))

    print(A)

    k = int(input('Оберіть індекс для видалення елементу: '))

    result = []

    for x in range(len(A)):

        if x != k:

            result.append(A[x])

    print('Оновлений спикок:', result)

    return result

delete()

#Task2
def average():

    A = list(map(int,input('Елементи списку: ').split()))
    
    A = [num for num in A if num < 0]
    print(A)

    avr = sum(A) / len(A)

    print ("Середнє арифметичне  від'ємних елементів:",avr)

    return avr

average()

#Task3
def add(input):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    input.update(vowels)
    return input

input = {'c', 'd'}

input = add(input)

print("Результат:", input)
