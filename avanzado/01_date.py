from datetime import time, datetime, date, timedelta
# 1. Crea una variable con la fecha y hora actual.
now = datetime.now()
print("Fecha y hora actual:", now)
# 2. Imprime solo el aÃ±o, mes y dÃ­a de la fecha actual.
print(f"Año: {now.year}, Mes: {now.month}, Dia: {now.day}")

# 3. Crea una fecha especÃ­fica: 25 de diciembre de 2025 y muÃ©strala.
fecha_especifica = date(2030, 1, 17)
print(fecha_especifica)
# 4. Muestra solo la hora, los minutos y los segundos de un objeto time.
hora_especifica = time(14, 30, 45)

# 5. Calcula cuÃ¡ntos dÃ­as faltan para el 1 de enero del aÃ±o siguiente.
fecha_siguiente = date(now.year +1,1,1)
print(diferencia := fecha_siguiente - now.date())

# 6. Crea una funciÃ³n que reciba una fecha y devuelva su timestamp.
def obtener_timestamp(fecha):
    fecha = datetime(fecha.year, fecha.month, fecha.day)
    return fecha.timestamp()
print(obtener_timestamp(fecha_especifica))

# 7. Suma 30 dÃ­as a la fecha actual usando timedelta.
fecha_mas = now + timedelta(days=30)
print(fecha_mas)
# 8. Crea una fecha y aÃ±ade 1 mes (consejo: hazlo sumando 30 dÃ­as como simplificaciÃ³n).
fecha_mas_mes = now + timedelta(days=30)
print(fecha_mas_mes)

# 9. Compara dos fechas y muestra cuÃ¡l es anterior.
fecha_otra = date(2025, 12, 25)
if fecha_especifica < fecha_otra:
    print(f"{fecha_especifica} es anterior a {fecha_otra}")
else:
    print(f"{fecha_especifica} no es anterior a {fecha_otra}")

# 10. Crea una lista con varias fechas y ordÃ©nalas cronolÃ³gicamente.
fechas = [date(2023,5,20), date(2022,3,15), date(2024,7,10)]
fechas.sort()
for fecha in fechas:    
    print(fecha)