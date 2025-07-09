# 1. Usa un bucle while para imprimir los nÃºmeros del 1 al 10.
number = 1
while number <= 10:
    print(number)
    number +=1
# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero.
list = [10, 20, 30, 40, 50]
for i in list:
    print(i)
# 3. Escribe un programa que use un bucle while para sumar los nÃºmeros del 1 al 100 e imprime el resultado.
number = 1
sum = 0
while number <= 100:
    sum += number
    number += 1
print(f"La suma de los numeros del 1 al 100 es: {sum}")
# 4. Escribe un bucle for que imprima cada carÃ¡cter de la cadena "Python".
cadena = "Python"
for i in cadena:
    print(i)
# 5. Usa un bucle while para encontrar el primer nÃºmero divisible por 7 entre 1 y 50.
number = 1
while number <= 50:
    if number %7 == 0:
        print(f"El primer numero divisible por 7 entre 1 y 50 es: {number}")
        break
    number += 1

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
dic = {"name": "Brais", "age": 37, "country": "Galicia"}
for i in dic:
    print(i)
# 7. Escribe un programa que use un bucle while para imprimir los nÃºmeros pares entre 1 y 20.
while number <= 20:
    if number %2 == 0:
        print(number)
    number +=1
# 8. Usa un bucle for con la funciÃ³n range() para imprimir los nÃºmeros del 1 al 10 en orden inverso.
for i in range(10,0, -1):
    print(i)
# 9. Escribe un programa que use un bucle for para contar cuÃ¡ntas veces aparece el nÃºmero 30 en la lista[30, 10, 30, 20, 30, 40].
list = [30, 10, 30, 20, 30, 40]
count = 0
for i in list:
    if i == 30:
        count += 1
print(f"El numero 30 aparece {count} veces en la lista")
# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
names = ["Ana", "Brais", "Carlos", "Diana"]
for name in names:
    if name == "Brais":
        print("Nombre encontrado:", name)
        break