def season(month):
    if month ==1 or month == 2 or month == 12:
        return 'Зима'
    elif month >= 3 and month <= 5:
        return 'Весна'
    elif month >= 6 and month <= 8:
        return 'Літо'

def season(month):
    if month in range(1, 3) or month == 12:
        return 'Зима'
    elif month in range(3, 6):
        return 'Весна'
    elif month in range(6, 9):
        return 'Літо'
    elif month in range(9, 12):
        return 'Осінь'
    else:
        return 'Номер місяця повинен бути цілим числом від 1 до 12'

