def season(month):
    if month ==1 or month == 2 or month == 12:
        return 'Зима'
    elif month >= 3 and month <= 5:
        return 'Весна'
    elif month >= 6 and month <= 8:
        return 'Літо'
        elif month >= 9 and month <= 11:
        return 'Осінь'
    else:
        return 'Номер місяця повинен бути цілим числом від 1 до 12'

month = 1
print(season(month))