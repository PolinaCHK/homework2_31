sales = {
    "Понедельник": [("капучино", 120, 14), ("латте", 150, 9), ("чай", 60, 21)],
    "Вторник":     [("капучино", 120, 8),  ("эспрессо", 90, 17), ("чай", 60, 12)],
    "Среда":       [("латте", 150, 11), ("эспрессо", 90, 6), ("какао", 110, 13)],
    "Четверг":     [("капучино", 120, 16), ("латте", 150, 7), ("чай", 60, 18)],
    "Пятница":     [("капучино", 120, 10), ("эспрессо", 90, 21), ("какао", 110, 9)],
}

day_forms = {
    "Понедельник": "Понедельника",
    "Вторник": "Вторника",
    "Среда": "Среды",
    "Четверг": "Четверга",
    "Пятница": "Пятницы"
}

def calculate_price(price, qty):
    return price * qty

def total(sales, day):
    total_day = 0
    for name, price, qty in sales[day]:
        total_day += calculate_price(price, qty)

    return total_day

def best(sales, day):
    best_day = ""
    cnt_day = 0
    for name, price, qty in sales[day]:
        if qty > cnt_day:
            cnt_day = qty
            best_day = name
    return f"Хит {day_forms[day]}: {best_day}"


def format_money(money):
    rub = int(money)
    kop = round((money - rub) * 100)
    # return f"{rub} руб {kop:02d} коп."
    return rub


for name_day in sales:
    print( f'{name_day}: выручка { format_money(total( sales, name_day))}')
    print( best( sales, name_day))


week_total = 0
max_total = -1
max_day = ''

for day in sales:
    day_total = total(sales,day)
    week_total += day_total

    if day_total > max_total:
        max_total = day_total
        max_day = day


print("Итоговая выручка за неделю:", format_money(week_total))
print("День с максимальной выручкой:", max_day)
print("Средняя выручка за день:", format_money(round(week_total / len(sales))))