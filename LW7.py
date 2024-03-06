students = [
    {"Учень": "Іванченко" "Іван", "вул.": "Луківська, 10", "школа": 1, "клас": 10},
    {"Учень": "Пономаренко" "Петро", "вул.": "Заводська, 5", "школа": 2, "клас": 11},
    {"Учень": "Сидоренко" "Марія", "вул.": "Петропавлівська, 15", "школа": 1, "клас": 11},
    {"Учень": "Коваленко" "Олексій", "вул.": "Центральна, 20", "школа": 3, "клас": 10},
    {"Учень": "Михайленко" "Ірина",  "вул.": "Перша, 3", "школа": 2, "клас": 10},
    {"Учень": "Шевченко" "Олег", "вул.": "Троїцька, 8", "школа": 1, "клас": 11},
    {"Учень": "Кузьмін" "Анна", "вул.": "Заводська, 12", "школа": 3, "клас": 11},
    {"Учень": "Ткаченко" "Данил", "вул.": "Шевчено, 6", "школа": 2, "клас": 10},
    {"Учень": "Савченко" "Олена", "вул.": "Південна, 2", "школа": 1, "клас": 11},
    {"Учень": "Клименко" "Артем", "вул.": "Горького, 4", "школа": 3, "клас": 10}
]

def Print(student):
    print("Учень: {}, вул.: {}, школа: {}, клас: {}".format(student["Учень"], student["вул."], student["школа"], student["клас"]))

school_number = int(input("Введіть номер школи (№1-3): "))

print("Учні школи {}:".format(school_number))
for student in students:
    if student["школа"] == school_number:
        Print(student)
