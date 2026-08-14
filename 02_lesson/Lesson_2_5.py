def month_to_season(месяц):
    if месяц in (1, 2, 12):
        return "Зима"
    elif месяц in (3, 4, 5):
        return "Весна"
    elif месяц in (6, 7, 8):
        return "Лето"
    elif месяц in (9, 10, 11):
        return "Осень"
    else:
        return "Такого месяца не сущестувует"


print(month_to_season(16))
