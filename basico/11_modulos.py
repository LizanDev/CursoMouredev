from statistics import calcular_mediana, media

from archivos import escribir_archivo, leer_archivo
from calculator import dividir, multiplicar, restar, sumar
from coche import car
from contar_palabras import contar_palabras
from converter import convertir_celsius_a_fahrenheit
from dates import diferencia_fechas, fecha_actual
from geometry import area_circulo, area_cuadrado
from lista_estudiente import mostrar_estudiantes
from sumatorio import sumar_todo

print(sumar(5, 3))
print(restar(10, 4))
print(multiplicar(2, 6))
print(dividir(8, 2))

# 2. Crea un mÃ³dulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit.
# Escribe un programa que importe este mÃ³dulo y realice conversiones.
print(convertir_celsius_a_fahrenheit(25))
# 3. Crea un mÃ³dulo que contenga una lista de nombres de estudiantes y una funciÃ³n que imprima todos los nombres.
# Importa este mÃ³dulo en otro archivo y usa la funciÃ³n para mostrar la lista.
mostrar_estudiantes()
# 4. Crea un mÃ³dulo llamado "geometry" que tenga una funciÃ³n para calcular el Ã¡rea de un cÃ­rculo y un cuadrado.
# Usa este mÃ³dulo en otro archivo para calcular Ã¡reas.
print(area_circulo(5))
print(area_cuadrado(5))
# 5. Escribe un mÃ³dulo que contenga una funciÃ³n que acepte cualquier nÃºmero de argumentos y devuelva su suma.
# Importa y usa la funciÃ³n en otro archivo.
print(sumar_todo(1, 2, 3, 4, 5))
# 6. Crea un mÃ³dulo que defina una clase llamada "Car" con propiedades como marca, modelo y aÃ±o. Importa este mÃ³dulo en otro
# archivo y crea una instancia de la clase "Car".
mi_coche = car("Toyota", "Chr", 2018)
mi_coche.mostrar_info()
# 7. Escribe un mÃ³dulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones
#  para escribir y leer datos.
contenido = "Estoy haciendo una prueba de escritura y lectura de archivos"
escribir_archivo("prueba.txt", contenido)
print(leer_archivo("prueba.txt"))
# 8. Crea un mÃ³dulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de nÃºmeros. Usa este
# mÃ³dulo para calcular estos valores en una lista dada.
numeros = [10, 20, 30, 40, 50]
print(media(numeros))
print(calcular_mediana(numeros))
# 9. Crea un mÃ³dulo que contenga una funciÃ³n para contar cuÃ¡ntas veces aparece una palabra en un texto. Escribe un programa que importe
# el mÃ³dulo y lo use para contar palabras en una cadena.
texto = "Hola que tal, hola es un saludo, hola prueba de contar palabras"
print(contar_palabras(texto, "hola"))
# 10 Crea un mÃ³dulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas.
# Usa este mÃ³dulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas especÃ­ficas.
print(fecha_actual())
print(diferencia_fechas("23-10-01", "23-10-15"))
