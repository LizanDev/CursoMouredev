from datetime import datetime

def fecha_actual():
    return datetime.now().strftime("%y-%m-%d")

def diferencia_fechas(date1, date2):
    date_format = "%y-%m-%d"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    return abs((d2 - d1).days)







