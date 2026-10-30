# Требуется написать следующий функции

# books_grouped_by_genre(catalog) — словарь вида 
# {жанр: список названий книг этого жанра, 
# которые можно взять в библиотеке 
# на данный момент (on_loan = False)}; 
# жанры в словаре идут в порядке их первого появления в каталоге.


# catalog = [
# {"title": "Мастер и Маргарита", "author": "Булгаков",
# "year": 1967, "genre": "роман", "on_loan": True},
# {"title": "Евгений Онегин", "author": "Пушкин",
# "year": 1833, "genre": "роман", "on_loan": False},
# {"title": "Стихотворения", "author": "Есенин",
# "year": 1926, "genre": "поэзия", "on_loan": False},
# {"title": "Вишнёвый сад", "author": "Чехов",
# "year": 1904, "genre": "пьеса", "on_loan": True},
# {"title": "Руслан и Людмила", "author": "Пушкин",
# "year": 1820, "genre": "поэма", "on_loan": False},
# {"title": "Три сестры", "author": "Чехов",
# "year": 1901, "genre": "пьеса", "on_loan": False},
# ]

# def find_by_author(catalog, author): #возвращает список названий книг данного автора
# 	books=[]
# 	for i in range (0, len(catalog)):
# 		if catalog[i]['author'] == author:
# 			books.append(catalog[i]['title'])
# 	return books


# def available_titles(catalog): #список названий книг, которые сейчас можно взять
# 	can_take = []
# 	for i in range (0, len(catalog)):
# 		if catalog[i]['on_loan'] == False:
# 			can_take.append(catalog[i]['title'])
# 	return can_take


# def books_grouped_by_genre(catalog):
# 	genre_of_books={}
# 	for i in range (0, len(catalog)):
# 		if catalog[i]["genre"] not in genre_of_books:
# 			genre_of_books[catalog[i]["genre"]] =[catalog[i]["title"]]
# 		else:
# 			genre_of_books[catalog[i]["genre"]].append(catalog[i]["title"])
# 	return genre_of_books
	
# print(books_grouped_by_genre(catalog))

sales = {
    "Понедельник": [("капучино", 120, 14), ("латте", 150, 9), ("чай", 60, 21)],
    "Вторник":     [("капучино", 120, 8),  ("эспрессо", 90, 17), ("чай", 60, 12)],
    "Среда":       [("латте", 150, 11), ("эспрессо", 90, 6), ("какао", 110, 13)],
    "Четверг":     [("капучино", 120, 16), ("латте", 150, 7), ("чай", 60, 18)],
    "Пятница":     [("капучино", 120, 10), ("эспрессо", 90, 21), ("какао", 110, 9)],
}

total_pon = 0
for name, price, qty in sales["Понедельник"]:
    total_pon += price * qty
print("Понедельник: выручка", total_pon)

best_pon = ""
cnt_pon = 0
for name, price, qty in sales["Понедельник"]:
    if qty > cnt_pon:
        cnt_pon = qty
        best_pon = name
print("Хит Понедельника:", best_pon)

total_vt = 0
for name, price, qty in sales["Вторник"]:
    total_vt += price * qty
print("Вторник: выручка", total_vt)

best_vt = ""
cnt_vt = 0
for name, price, qty in sales["Вторник"]:
    if qty > cnt_vt:
        cnt_vt = qty
        best_vt = name
print("Хит Вторника:", best_vt)

total_sr = 0
for name, price, qty in sales["Среда"]:
    total_sr += price * qty
print("Среда: выручка", total_sr)

best_sr = ""
cnt_sr = 0
for name, price, qty in sales["Среда"]:
    if qty > cnt_sr:
        cnt_sr = qty
        best_sr = name
print("Хит Среды:", best_sr)

total_cht = 0
for name, price, qty in sales["Четверг"]:
    total_cht += price * qty
print("Четверг: выручка", total_cht)

best_cht = ""
cnt_cht = 0
for name, price, qty in sales["Четверг"]:
    if qty > cnt_cht:
        cnt_cht = qty
        best_cht = name
print("Хит Четверга:", best_cht)

total_pt = 0
for name, price, qty in sales["Пятница"]:
    total_pt += price * qty
print("Пятница: выручка", total_pt)

best_pt = ""
cnt_pt = 0
for name, price, qty in sales["Пятница"]:
    if qty > cnt_pt:
        cnt_pt = qty
        best_pt = name
print("Хит Пятницы:", best_pt)