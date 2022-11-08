def season(month):
    if month ==1 or month == 2 or month == 12:
        return 'Зима'
    elif month >= 3 and month <= 5:
        return 'Весна'
    elif month >= 6 and month <= 8:
        return 'Літо'