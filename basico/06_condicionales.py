# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.
my_nomber = 0
if my_nomber == 0:
    print("el numero el cero")
elif my_nomber >0:
    print("El numero es positivo")
else:
    print("el numero es negativo")
# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.
my_age = int(input("Introduce tu edad: "))
if my_age >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
# 3. Escribe un programa que verifique si una cadena de texto estÃ¡ vacÃ­a y muestre un mensaje en consecuencia.
message = input("Introduce un mrensaje: ")
if message == "":
    print("El mensaje esta vacio")
else:
    print(message)
# 4. Crea un programa que solicite dos nÃºmeros al usuario y compare cuÃ¡l es mayor. Si son iguales, muestra un mensaje indicando 
# la igualdad.
number1 = int(input("Introduce el primer numero: "))
number2 = int(input("Introduce el segundo numero: "))
if number1 > number2:
    print(f"El numero {number1} es mayor que {number2}")
elif number1 < number2:
    print(f"El numero {number2} es mayor que {number1}")
else:
    print(f"Los numeros {number1} y {number2} son iguales")
# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo.
number = int(input("Introduce un numero: "))
if number %3 == 0 and number %5 == 0:
    print(f"El numero {number} es divisible por 3 y por 5")
# 6. Solicita al usuario que ingrese un nÃºmero y verifica si es par o impar.
number = int(input("Introduce un numero: "))
if number %2 == 0:
    print(f"El numero {number} es par")
else:
    print(f"El numero {number} es impar")
# 7. Escribe un programa que determine si una persona puede votar en funciÃ³n de su edad(mayor o igual a 18). Si tiene 16 o 17 aÃ±os,
#  indica que puede votar con permiso especial.
age = int(input("Introduce tu edad: "))
if age >= 18:
    print("Puedes votar")
elif age == 16 or age ==17:
    print("Puedes votar con permiso espeial")
else:
    print("No puedes votar")
# 8. Crea un programa que solicite una contraseÃ±a al usuario y verifique si coincide con una contraseÃ±a predefinida. Si no coincide,
#  muestra un mensaje de error.
password = input("Introduce la contraseña: ")
correct_password = "12345"
if password == correct_password:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
# 9. Escribe un programa que determine si un nÃºmero estÃ¡ entre 10 y 20 (ambos incluidos).
number = int(input("Introduce un numero: "))
if number >= 10 and number <= 20:
    print(f"El numero {number} esta entre 10 y 20")
else:
    print(f"El numero {number} no esta entre 10 y 20")
# 10. Escribe un programa que simule un semÃ¡foro: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje 
# indicando si debe detenerse, estar alerta o avanzar.
luz_semaforo = input ("Introduce el color del semaforo (rojo, amarillo, verde): ").lower()
if luz_semaforo == "rojo":
    print("Detente")
elif luz_semaforo == "amarillo":
    print("Alerta")
elif luz_semaforo == "verde":
    print("Avanza")