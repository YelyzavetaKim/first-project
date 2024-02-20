#Task1
s = input("Введіть речення: ")

result = s[17:-3]

print("Послідовність символів: ", result)

#Task2
word = input("Введіть слово: ")

ascii_sum = 0
for char in word:
    ascii_sum += ord(char)

print("Сума ASCII кодів символів слова:", ascii_sum)

#Task3
sentence = input("Введіть речення: ")

words = sentence.split()

three_e = []
for word in words:
    if word.count('е') == 3:
        three_e.append(word)

if three_e:
    print("Слова з трьома літерами 'е':")
    for word in three_e:
        print(word)
else:
    print("У реченні відсутні слова з трьома літерами 'е' ")
